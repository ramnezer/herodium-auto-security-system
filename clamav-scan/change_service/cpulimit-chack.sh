#!/bin/bash

### Limit 'clamdscan' to a defined work level,
### prevent duplicate activation attempts if 
### the limit has already run

sleep 1

while
 
 check=$(pgrep -f  "/usr/sbin/clamd")
 check_cpu=$(pgrep -f  "cpulimit -l 25 -p $check")
 check_cpu3=$(pgrep -f  "cpulimit -l 75 -p $check")
 check_root=$(pgrep -f  "clamdscan --fdpass --infected /")

 if [ "$check" ] && [ "$check_cpu" == "" ] && [ "$check_root" == "" ]
 then
 
 cpulimit -l 25 -p $check
 
 elif [ "$check" ] && [ "$check_cpu3" == "" ] && [ "$check_root" ]
 then
  
 cpulimit -l 75 -p $check
 

 fi

sleep 1

do
    :
done


