#!/bin/bash

##########################################################################################################################


# Prevent the listener from entering to a frozen state by creating a loop
while
 
 touch /var/log/maltrail/$(date +"%Y-%m-%d").log
 timeout  10m tail -n0 -f /var/log/maltrail/$(date +"%Y-%m-%d").log >>'/opt/auto-clamIPS/maltrail/logs/scan.log'
 
sleep 1
 
do
    :
done
 
##########################################################################################################################
