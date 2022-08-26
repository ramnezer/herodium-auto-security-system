#!/bin/bash
sudo python3 /opt/auto-clamIPS/notify-clamMA/notify-reset-boot.py
DIRTOSCAN=$(cat /opt/auto-clamIPS/maltrail/logs/ipset.log)
ipset_log="/opt/auto-clamIPS/maltrail/logs/ipset.log"
user=$(echo $(users) | cut -d ' ' -f 1)


echo $(cat $ipset_log) >> /home/$user/Desktop/maltrail-found-$(date +'%Y-%m-%d').log
echo $(cat $ipset_log) >> /root/maltrail-found-$(date +'%Y-%m-%d').log

printf  "\n#############################################################\nfound malicious traffic check with\n[sudo ipset list blacklists && sudo ipset list blacklists2]\nif the malicious addresses have been blocked\n#############################################################\n" >> /home/$user/Desktop/maltrail-found-$(date +'%Y-%m-%d').log

printf  "\n#############################################################\nfound malicious traffic check with\n[sudo ipset list blacklists && sudo ipset list blacklists2]\nif the malicious addresses have been blocked\n#############################################################\n" >> /root/maltrail-found-$(date +'%Y-%m-%d').log


for S in ${DIRTOSCAN}; do
DIRSIZE=$(du -sh "$S" 2>/dev/null | cut -f1)
echo "Starting a scan of "$S" directory.
Amount of data to be scanned is "$DIRSIZE"."
# ipv4
sudo ipset add blacklists "$S" 2> /dev/null
# ipv6
sudo ipset add blacklists2 "$S" 2> /dev/null

sudo -i ipset save blacklists > /etc/ipset_maltrail.conf
sudo -i ipset save blacklists2 > /etc/ipset_maltrail2.conf

sudo echo "(malware)" >> /opt/auto-clamIPS/notify-clamMA/logs/notify2.log

done
exit 0
