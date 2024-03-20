#!/bin/bash

while
 
 kill_correct=$(pgrep  -uroot -f  "cpulimit -l   $()   | -p $(pgrep -f  "/usr/sbin/clamd")")
 check1=$(pgrep -f  "/opt/auto-clamIPS/auto-clamav/cpulimit-chack.sh")
 
 if [ "$check1" == "" ]
 then
 
 kill -9 $(pgrep  -uroot -f  "cpulimit -l   $()   | -p $(pgrep -f  "/usr/sbin/clamd")") 2> /dev/null

 setsid /opt/auto-clamIPS/auto-clamav/cpulimit-chack.sh &

 fi

sleep 5

do
    :
done

