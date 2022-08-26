#!/bin/bash

sudo mkdir -p /var/log/clamav/
LOGFILE="/var/log/clamav/clamav-found-malware-$(date +'%Y-%m-%d').log"
LOGS_HISTORY="/opt/auto-clamIPS/auto-clamav/logs/logs_history/real-time-history/real-time-history-$(date +'%Y-%m-%d').log"
LOGFILE2="/opt/auto-clamIPS/notify-clamMA/logs/notify.log"
user=$(echo $(users) | cut -d ' ' -f 1)

cat "$LOGFILE" >> "$LOGS_HISTORY"
cat "$LOGFILE" >> "$LOGFILE2"
cat $LOGFILE >> /home/$user/Desktop/clamav-found-malware-$(date +'%Y-%m-%d').log
cat $LOGFILE >> /root/clamav-found-malware-$(date +'%Y-%m-%d').log
rm -rf "/var/log/clamav/clamav-found-malware-$(date +'%Y-%m-%d').log" 


