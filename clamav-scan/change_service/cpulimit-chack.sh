#!/bin/bash

### Limit 'clamdscan' to a defined work level,
### prevent duplicate activation attempts if 
### the limit has already run

sleep 1

while
 
 sleep 1
 check=$(pgrep -f  "/usr/sbin/clamd")
 check_cpu=$(pgrep -f  "cpulimit -l 50 -p")
 if [ "$check" ] && [ "$check_cpu" == "" ]
 then
 cpulimit -l 50 -p $check
 sleep 2

 fi

do
    :
done

