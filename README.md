# gcloud_1000g_streaming #
Experimental recalling from the Sequence Read Archive using instances on google cloud.

**Goal**: Recall all common LoF variants that are found in ExAC, but not found in 1000G.

## Setting Up a Compute VM on GCloud ##
1. Start up a n1-highcpu-16 machine
2. Log into the VM
3. Install the streaming version of gotcloud 
    a. Clone the streaming fork of gotcloud
    b. Build gotcloud and dependencies
    c. Download reference data
4. clone down this repository

## Running: ##
1. Run `run_1000G_lof_sra_exomes.py`
2. Record the runtime
3. Collect the results and check them against the locally called variants
