#!/bin/bash

### fix the service if the value(correct user) 
### is not true or target line is not appear 

user=$( users | cut -d ' ' -f 1)

notify_reset=$(grep -F 'XAUTHORITY=/home/'"$user"'/.Xauthority' '/etc/systemd/system/notify-send.service')

if [ "$notify_reset" ==  "" ]
then

python3 /opt/auto-clamIPS/notify-clamMA/notify-reset-boot.py


fi
