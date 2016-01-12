#!/bin/bash

snpcall_output_dir="/home/ubuntu/gcloud_1000g_streaming/snpcall/outputs/exome_sra/"
gotcloudroot="/home/ubuntu/gotcloud/"
vcfs=$(ls ${snpcall_output_dir}*/vcfs/chr*/chr*.hardfiltered.vcf.gz)
output=${snpcall_output_dir}"recalled_variants.vcf"

tempdir=$(mktemp -d)
for f in $vcfs; do
  region=$(echo $f | cut -d '/' -f 8)
  cp $f ${tempdir}/${region}.vcf.gz
  #${gotcloudroot}bin/bgzip ${tempdir}/${region}.vcf;
  ${gotcloudroot}bin/tabix -p vcf ${tempdir}/${region}.vcf.gz
done

vcfcombine ${tempdir}/*vcf.gz > $output  
#vcfintersect -r ${gotcloudroot}gotcloud.ref/hs37d5.fa -i /home/ubuntu/gcloud_1000g_streaming/data/exac_common_lof_snps_no-1000G.vcf.gz > ${tempdir}/${region}.vcf;

rm -rf $tempdir
