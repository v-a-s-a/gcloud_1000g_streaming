# gcloud_1000g_streaming
Experimental recalling from the Sequence Read Archive using instances on google cloud.

**Goal**: Recall all common LoF variants that are found in ExAC, but not found in 1000G.

Setup:
- Start up a n1-highcpu-16 machine
- Log into the VM
- Install the streaming version of gotcloud 
    - build gotcloud and dependencies
    - download reference data
- clone down this repository

Running:
- Run `run_1000G_lof_sra_exomes.py`
- Record the runtime
- Collect the results and check them against the locally called variants
