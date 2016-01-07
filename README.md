# gcloud_1000g_streaming
Experimental recalling from the Sequence Read Archive using instances on google cloud.

Goal: Recall all common LoF variants that are found in ExAC, but not found in 1000G

Before starting:

- Compressed and indexed VCF of these variants
- List of 1000G SRR accession numbers for exome experiments

Setup:

- Start up a n1-highcpu-16 machine
- install gotcloud on the machine (streaming fork)
    - clone streaming fork
    - build gotcloud and dependencies
    - download reference data
- clone down the repository with scripts and configuration files

Running:

- Run the recalling script
- Record the runtime
- Collect the results and check them against the locally called variants
