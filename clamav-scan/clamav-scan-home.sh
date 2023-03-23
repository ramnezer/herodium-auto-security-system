#!/bin/bash
python3 /opt/auto-clamIPS/notify-clamMA/notify-reset-boot.py
mkdir -p /var/log/clamav/
rm -rf "/var/log/clamav/clamav-found-malware-$(date +'%Y-%m-%d').log" 
LOGFILE="/var/log/clamav/clamav-found-malware-$(date +'%Y-%m-%d').log"
LOGFILE2="/opt/auto-clamIPS/notify-clamMA/logs/notify1.log"
LOGS_HISTORY="/opt/auto-clamIPS/auto-clamav/logs/logs_history/home-scan-history/home-scan-history-$(date +'%Y-%m-%d').log"
exclude=$(echo $(cat "/opt/auto-clamIPS/auto-clamav/ignore_list.txt"))
DIRTOSCAN="/home/ /root/ /boot/ /etc/ /opt/ /dev/"
user=$(echo $(users) | cut -d ' ' -f 1)

### For distributions with non-english languages,get the correct desktop name 
### and convert it to universal(for english and non-english distro)variable
desktop1=$(cat /home/$user/.config/user-dirs.dirs | grep "XDG_DESKTOP_DIR" | cut -d'/' -f2- | tr -d '"')

for S in ${DIRTOSCAN}; do
DIRSIZE=$(du -sh "$S" 2>/dev/null | cut -f1)
echo "Starting a scan of "$S" directory.
Amount of data to be scanned is "$DIRSIZE"."
clamscan --infected --recursive $exclude "$S" >> "$LOGFILE"
mkdir -p /opt/auto-clamIPS/auto-clamav/logs/logs_history/home-scan-history/
cat "$LOGFILE" >> "$LOGS_HISTORY"
cat "$LOGFILE" >> "$LOGFILE2"
# get the value of "Infected lines"
MALWARE=$(tail "$LOGFILE"|grep Infected|cut -d" " -f3)
# 
if [ "$MALWARE" -ne "0" ];then
# using file below

cat "$LOGFILE" >> "$LOGS_HISTORY"
cat "$LOGFILE" >> "$LOGFILE2"
cp $LOGFILE "/home/$user/$desktop1/"
cp $LOGFILE /root/


fi

done
exit 0
