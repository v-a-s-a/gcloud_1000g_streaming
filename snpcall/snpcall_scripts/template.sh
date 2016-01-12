#!/bin/bash

/home/ubuntu/gotcloud/gotcloud snpcall \
  --bamlist {SAMPLE_LIST} \
  --region {REGION} \
  --numjobs 5 \
  --conf {CONF}

