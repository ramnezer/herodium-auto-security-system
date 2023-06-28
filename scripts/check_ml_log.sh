#!/bin/bash


while
 
 check=$(ls /var/log/maltrail/$(date +"%Y-%m-%d").log)

 if [ "$check" == "" ]
 then

 systemctl restart maltrail-sensor
 touch /var/log/maltrail/$(date +"%Y-%m-%d").log
 timeout  10m tail -n0 -f /var/log/maltrail/$(date +"%Y-%m-%d").log >>'/opt/auto-clamIPS/maltrail/logs/scan.log'
 
 fi

sleep 5
 
do
    :
done
