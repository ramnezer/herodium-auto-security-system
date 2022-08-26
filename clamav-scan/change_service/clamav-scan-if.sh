#!/bin/bash
sudo mkdir -p /var/log/clamav/
rm -rf "/var/log/clamav/clamav-found-malware-$(date +'%Y-%m-%d').log" 
sudo python3 /opt/auto-clamIPS/notify-clamMA/notify-reset-boot.py
LOGFILE="/var/log/clamav/clamav-found-malware-$(date +'%Y-%m-%d').log"
LOGS_HISTORY="/opt/auto-clamIPS/auto-clamav/logs/logs_history/real-time-history/real-time-history-$(date +'%Y-%m-%d').log"
LOGFILE2="/opt/auto-clamIPS/notify-clamMA/logs/notify.log"
exclude=$(echo $(cat "/opt/auto-clamIPS/auto-clamav/ignore_list.txt"))
user=$(echo $(users) | cut -d ' ' -f 1)
mkdir -p /home/$(echo $(users) | cut -d ' ' -f 1)/auto-clamIPS/VIRUS-FOUND/
chown -R $(echo $(users) | cut -d ' ' -f 1):$(echo $(users) | cut -d ' ' -f 1) /home/$(echo $(users) | cut -d ' ' -f 1)/auto-clamIPS/
clamscan --infected --recursive --exclude=/home/$user/auto-clamIPS/VIRUS-FOUND/ --exclude=/home/$user/Desktop/clamav-found-malware-$(date +'%Y-%m-%d').log $exclude --file-list="/opt/auto-clamIPS/auto-clamav/logs/auto.log" >> "$LOGFILE" 
zip -m -j /home/$(echo $(users) | cut -d ' ' -f 1)/auto-clamIPS/VIRUS-FOUND/VIRUS-FOUND.zip /home/$(echo $(users) | cut -d ' ' -f 1)/auto-clamIPS/VIRUS-FOUND/* 1> /dev/null
mkdir -p /opt/auto-clamIPS/auto-clamav/logs/logs_history/real-time-history/

cat "$LOGFILE" >> "$LOGS_HISTORY"
cat "$LOGFILE" >> "$LOGFILE2"
