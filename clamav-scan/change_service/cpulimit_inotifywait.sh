#!/bin/bash

### inotifywait

sleep 1

while
 
 inotifywait=$(pgrep -f  "inotifywait")
 inotifywait_cpu=$(pgrep -f  "cpulimit -l 15 -p $inotifywait")

 if [ "$inotifywait" ] && [ "$inotifywait_cpu" == "" ]
 then
 
 cpulimit -l 15 -p $inotifywait
  
 fi

sleep 5

do
    :
done
