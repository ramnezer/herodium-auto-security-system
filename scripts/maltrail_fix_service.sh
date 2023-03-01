#!/bin/bash 

### prevents unnecessary load on the RAM memory during repeated unreported alerts
### such as a suspicious website that remains open for a long time

while
 
 sleep 12h
 sudo systemctl restart maltrail-sensor 
 sleep 5
 
do
    :
done
