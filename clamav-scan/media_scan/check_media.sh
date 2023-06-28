#!/bin/bash

### Allow the scanning system to detect
### drives that do not mount after starting
### the system such as usb and other hard disks


while

 check_log=$(cat "/opt/auto-clamIPS/auto-clamav/media_scan/logs/media_check.log")

 if [ "$check_log" ]
 then
 
 systemctl restart media_scan.service

 truncate -s 0 "/opt/auto-clamIPS/auto-clamav/media_scan/logs/media_check.log"

 fi

sleep 3

do
    :
done
