#!/bin/bash


### fix error 'listener frozen/not responding'
##########################################################################################################################

# Prevent the listener from entering to a frozen state by creating a loop
while
 
 timeout  10m  sudo -i tail -n0 -f /var/log/maltrail/$(date +"%Y-%m-%d").log >>'/opt/auto-clamIPS/maltrail/logs/scan.log'

### Prevent 'zombie' processes if it is true
 sudo kill -9 $(pgrep -f  "tail -n0 -f /var/log/maltrail/$(date +"%Y-%m-%d").log")
 sudo kill -9 $(pgrep -f  "timeout  10m  sudo -i tail -n0 -f /var/log/maltrail/$(date +"%Y-%m-%d").log")
 sudo kill -9 $(pgrep -f  "timeout  10m  tail -n0 -f /var/log/maltrail/$(date +"%Y-%m-%d").log")
 sudo kill -9 $(pgrep -f  "sudo -i tail -n0 -f /var/log/maltrail/$(date +"%Y-%m-%d").log")
 sudo kill -9 $(pgrep -f  "timeout  10m  sudo -i tail -n0 -f /var/log/maltrail/$(date +"%Y-%m-%d").log")
 
 sleep 0
 
do
    :
done
 
##########################################################################################################################

