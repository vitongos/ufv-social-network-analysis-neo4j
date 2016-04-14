#!/bin/bash

cd ~/Downloads

sudo yum -y install libjpeg libjpeg-devel
sudo R -e "install.packages(c('mapproj','jpeg','ggmap','networktools','maps'), repos = 'http://cran.cnr.berkeley.edu/', dependencies=T)" --verbose
