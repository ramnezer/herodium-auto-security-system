#!/bin/bash

### help the first script identify the
### required change autonomously to match
### the correct limit


while
 
 check=$(pgrep -f  "/usr/sbin/clamd")
 check_cpu=$(pgrep -f  "cpulimit -l 25 -p $check")
 check_cpu3=$(pgrep -f  "cpulimit -l 75 -p $check")
 check_root=$(pgrep -f  "clamdscan --fdpass --infected /")
 
if [ "$check" ] && [ "$check_cpu" == "" ] && [ "$check_root" == "" ]
 then
 
 kill  "$check_cpu3"
 
 elif [ "$check" ] && [ "$check_cpu3" == "" ] && [ "$check_root" ]
 then
 
 kill  "$check_cpu"

 fi

sleep 5

do
    :
done
