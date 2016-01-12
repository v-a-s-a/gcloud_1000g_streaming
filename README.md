
## Goal: ##
Recall all common LoF variants that are found in ExAC, but not found in 1000G.

## Setting Up a Compute VM on GCloud ##
1. Start up a n1-highcpu-16 machine
2. Log into the VM
3. Install the streaming version of gotcloud:
    - Clone the streaming fork of gotcloud
    - Build gotcloud and dependencies
    - Download reference data
4. clone down this repository


### installing streaming gotcloud on a compute VM:

I'm using a ubuntu 14.04 LTS image with a n1-standard-1 machine and a 50GB standard persistent disk. The `VM_IP` variable is found in the console when starting up the machine.

Commands:

    ssh ubuntu@${VM_IP}
    sudo apt-get update
    sudo apt-get install git
    git clone https://github.com/statgen/gotcloud.git
    cd gotcloud/
    git checkout stream
    sudo apt-get install java-common default-jre make gcc g++ cmake
    sudo apt-get install zlib1g-dev libncurses5-dev openssl libcurl4-openssl-dev
    cd src/
    make
    cd ..
    make
    cd
    git clone https://github.com/vtrubets/gcloud_1000g_streaming.git
    scp -r trubetsk@snowwhite.sph.umich.edu:/net/snowwhite/home/trubetsk/gotcloud/gotcloud.ref/ /home/ubuntu/gotcloud/gotcloud.ref
    cd ~/gcloud_1000g_streaming/
    time run_....
    

linking and compilation in stream branch still fails!
    
    
    

## Running: ##
1. Run `run_1000G_lof_sra_exomes.py`
2. Record the runtime
3. Collect the results and check them against the locally called variants
