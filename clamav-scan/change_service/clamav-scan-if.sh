#!/bin/bash
mkdir -p /var/log/clamav/
rm -f "/var/log/clamav/clamav-found-malware-$(date +'%Y-%m-%d').log" 
/opt/auto-clamIPS/notify-clamMA/check_user.sh
LOGFILE="/var/log/clamav/clamav-found-malware-$(date +'%Y-%m-%d').log"
LOGS_HISTORY="/opt/auto-clamIPS/auto-clamav/logs/logs_history/real-time-history/real-time-history-$(date +'%Y-%m-%d').log"
LOGFILE2="/opt/auto-clamIPS/notify-clamMA/logs/notify.log"
user=$( users | cut -d ' ' -f 1)
option_remove=$(echo "")

### For distributions with non-english languages,get the correct desktop name 
### and convert it to universal(for english and non-english distro)variable
desktop1=$(cat /home/"$user"/.config/user-dirs.dirs | grep "XDG_DESKTOP_DIR" | cut -d'/' -f2- | tr -d '"')

clamdscan --fdpass --infected $option_remove --file-list="/opt/auto-clamIPS/auto-clamav/logs/auto.log" >> "$LOGFILE"
mkdir -p /opt/auto-clamIPS/auto-clamav/logs/logs_history/real-time-history/

cat "$LOGFILE" >> "$LOGS_HISTORY"
cat "$LOGFILE" >> "$LOGFILE2"
