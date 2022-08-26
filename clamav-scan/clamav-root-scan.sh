#!/bin/bash
sudo python3 /opt/auto-clamIPS/notify-clamMA/notify-reset-boot.py
sudo mkdir -p /var/log/clamav/
rm -rf "/var/log/clamav/clamav-found-malware-$(date +'%Y-%m-%d').log" 
LOGFILE="/var/log/clamav/clamav-found-malware-$(date +'%Y-%m-%d').log";
LOGFILE2="/opt/auto-clamIPS/notify-clamMA/logs/notify1.log"
LOGS_HISTORY="/opt/auto-clamIPS/auto-clamav/logs/logs_history/root-scan-history/root-sacn-history-$(date +'%Y-%m-%d').log"
exclude=$(echo $(cat "/opt/auto-clamIPS/auto-clamav/ignore_list.txt"))
DIRTOSCAN="/"
user=$(echo $(users) | cut -d ' ' -f 1)
for S in ${DIRTOSCAN}; do
DIRSIZE=$(du -sh "$S" 2>/dev/null | cut -f1)
echo "Starting a scan of "$S" directory.
Amount of data to be scanned is "$DIRSIZE"."
clamscan --infected --detect-pua=yes --recursive $exclude "$S" >> "$LOGFILE"
mkdir -p /opt/auto-clamIPS/auto-clamav/logs/logs_history/root-sacn-history/
cat "$LOGFILE" >> "$LOGS_HISTORY"
cat "$LOGFILE" >> "$LOGFILE2"
# get the value of "Infected lines"
MALWARE=$(tail "$LOGFILE"|grep Infected|cut -d" " -f3);
# if the value is not equal to zero, send log to desktop and root
if [ "$MALWARE" -ne "0" ];then
# using file below

cat "$LOGFILE" >> "$LOGS_HISTORY"
cat "$LOGFILE" >> "$LOGFILE2"
cp $LOGFILE /home/$user/Desktop/
cp $LOGFILE /root/


fi

done
exit 0

