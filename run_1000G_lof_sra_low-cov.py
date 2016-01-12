#!/usr/bin/env python

import os
import gzip as gz


root = '/home/ubuntu/gcloud_1000g_streaming/'
snpcall_template_sh = root + 'snpcall/snpcall_scripts/template.sh'
snpcall_template_conf = root + 'snpcall/snpcall_conf/template.conf'
target_vcf = root + 'data/exac_common_lof_snps_no-1000G.vcf.gz'

call_window = 1
experiment_type = 'low-cov_sra'
sample_list = root + 'data/1000G_phase3_low-coverage_SRR.list'

output_dir = root + 'snpcall/outputs/{0}/'.format(experiment_type)

gotcloud_root = '/home/ubuntu/gotcloud/'

def return_region(line):
    if line.startswith('#'):
        return None
    else:
        return line.strip().split()[0:2]

def __main__():
    regions = [ return_region(line) for line in gz.open(target_vcf) if return_region(line) ]
    ## extract the variant of interest with tabix
    for (chrom, pos) in regions:
        run_id = chrom + '-' + pos + '_' + experiment_type
        extractVcf = root + 'data/single_variant_vcfs/' + chrom + '-' + pos + '.vcf'
        ## zip and index the extracted vcf
        os.system(' '.join([gotcloud_root + '/bin/tabix -h -f', target_vcf, chrom+':'+pos, '>', extractVcf ]))
        os.system(' '.join([gotcloud_root + '/bin/bgzip -f', extractVcf]))
        os.system(' '.join([gotcloud_root + '/bin/tabix -p vcf', extractVcf + '.gz']))

        ## format the execution and configuration templates
        run_script = snpcall_template_sh.replace("template", run_id)
        run_conf = snpcall_template_conf.replace("template", run_id)
        with open(snpcall_template_sh) as snpcall_template_shConn:
            template = snpcall_template_shConn.read()
            template = template.format(REGION = chrom+':'+str(int(pos)-call_window)+'-'+str(int(pos)+call_window),
                                            CONF = run_conf,
                                            SAMPLE_LIST = sample_list)
        with open(run_script, 'w') as execScript:
            execScript.write(template)
        with open(snpcall_template_conf) as snpcall_template_confConn:
            template = snpcall_template_confConn.read()
            template = template.format(OUTPUT = output_dir + run_id,
                                            CHROMOSOME = chrom,
                                            VCFEXTRACT = extractVcf + '.gz')
        with open(run_conf, 'w') as confFile:
            confFile.write(template)

        ## submit the script via slurm
        print "Starting: {}:{}".format(chrom, pos)
        os.system('chmod u+x {}'.format(run_script))
        os.system(run_script)

if __name__ == '__main__':
    __main__()
