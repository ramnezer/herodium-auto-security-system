#!/bin/bash

mkdir -p /var/log/clamav/
LOGFILE="/var/log/clamav/clamav-found-malware-$(date +'%Y-%m-%d').log"
LOGS_HISTORY="/opt/auto-clamIPS/auto-clamav/logs/logs_history/real-time-history/real-time-history-$(date +'%Y-%m-%d').log"
LOGFILE2="/opt/auto-clamIPS/notify-clamMA/logs/notify.log"
user=$(cat /etc/group | grep $(id -u $(w -s | grep "tty7" | cut -d ' ' -f 1)) | cut -d: -f1)

### For distributions with non-english languages,get the correct desktop name 
### and convert it to universal(for english and non-english distro)variable
desktop1=$(cat /home/$user/.config/user-dirs.dirs | grep "XDG_DESKTOP_DIR" | cut -d'/' -f2- | tr -d '"')

cat "$LOGFILE" >> "$LOGS_HISTORY"
cat "$LOGFILE" >> "$LOGFILE2"
cat $LOGFILE >> "/home/$user/$desktop1/clamav-found-malware-$(date +'%Y-%m-%d').log"
cat $LOGFILE >> "/root/clamav-found-malware-$(date +'%Y-%m-%d').log"
rm -f "/var/log/clamav/clamav-found-malware-$(date +'%Y-%m-%d').log"
