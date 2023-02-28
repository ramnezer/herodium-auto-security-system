#!/bin/bash

sudo python3 /opt/auto-clamIPS/notify-clamMA/notify-reset-boot.py
mkdir -p /opt/auto-clamIPS/rkhunter/logs/
truncate -s 0 /opt/auto-clamIPS/rkhunter/logs/ROOTKITS_WARNING-$(date +'%Y-%m-%d').log
ROOTKITS_LOG="/opt/auto-clamIPS/rkhunter/logs/ROOTKITS_WARNING-$(date +'%Y-%m-%d').log"
user=$(echo $(users) | cut -d ' ' -f 1)
###

rkhunter --check --enable rootkits --disable malware --report-warnings-only >> $ROOTKITS_LOG
ROOTKITS_CHECK=$(grep -F 'Warning:' $ROOTKITS_LOG)

sleep 1

if [ "$ROOTKITS_CHECK" ]
then

cp $ROOTKITS_LOG /home/$user/Desktop/
cp $ROOTKITS_LOG /root/

echo "Warning:" >> /opt/auto-clamIPS/notify-clamMA/logs/notify3.log

fi

