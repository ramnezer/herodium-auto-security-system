#!/bin/bash

### fix the service if the value(correct user) 
### is not true or target line is not appear 

user=$(cat /etc/group | grep $(id -u $(w -s | grep "tty7" | cut -d ' ' -f 1)) | cut -d: -f1)

notify_reset=$(grep -F 'XAUTHORITY=/home/'"$user"'/.Xauthority' '/etc/systemd/system/notify-send.service')

if [ "$notify_reset" ==  "" ]
then

python3 /opt/auto-clamIPS/notify-clamMA/notify-reset-boot.py


fi
