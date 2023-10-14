#!/bin/bash

sleep 5

mkdir -p /opt/auto-clamIPS/auto-clamav/media_scan/logs
check=$(pgrep -f  "/usr/sbin/clamd")

while

 if [ "$check" ]
 then
  
  user1=$( users | cut -d ' ' -f 1)

  inotifywait  -ecreate -m -q   "/media/$user1/" >> "/opt/auto-clamIPS/auto-clamav/media_scan/logs/media_check.log"
  
 fi

sleep 3

do
    :
done







