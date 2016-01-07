#!/bin/bash

/net/snowwhite/home/trubetsk/projects/gotcloud_development/gotcloud/gotcloud snpcall \
  --bamlist {SAMPLE_LIST} \
  --region {REGION} \
  --numjobs 10 \
  --conf {CONF}

