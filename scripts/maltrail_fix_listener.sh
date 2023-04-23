#!/bin/bash


### fix error 'listener frozen/not responding'
##########################################################################################################################

data=$(date +"%Y-%m-%d")

# Prevent the listener from entering to a frozen state by creating a loop
while
 
 timeout 10m tail -n0 -f /var/log/maltrail/"$data".log >>'/opt/auto-clamIPS/maltrail/logs/scan.log'
 
 sleep 1
 
do
    :
done
 
##########################################################################################################################
