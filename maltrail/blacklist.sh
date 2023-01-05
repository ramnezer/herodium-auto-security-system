#!/bin/bash
sudo python3 /opt/auto-clamIPS/notify-clamMA/notify-reset-boot.py
IPSCAN=$(cat /opt/auto-clamIPS/maltrail/logs/ipset.log)
ipset_log="/opt/auto-clamIPS/maltrail/logs/ipset.log"
dig_log="/opt/auto-clamIPS/maltrail/logs/dig.log"
user=$(echo $(users) | cut -d ' ' -f 1)
dig=$(dig $IPSCAN +short >> $dig_log && dig AAAA $IPSCAN +short >> $dig_log && cat $dig_log)

echo $(cat $ipset_log) >> /home/$user/Desktop/maltrail-found-$(date +'%Y-%m-%d').log
echo $(cat $ipset_log) >> /root/maltrail-found-$(date +'%Y-%m-%d').log

printf  "\n#############################################################\nfound malicious traffic check with\n[sudo ipset list blacklists && sudo ipset list blacklists2]\nif the malicious addresses have been blocked\n#############################################################\n" >> /home/$user/Desktop/maltrail-found-$(date +'%Y-%m-%d').log

printf  "\n#############################################################\nfound malicious traffic check with\n[sudo ipset list blacklists && sudo ipset list blacklists2]\nif the malicious addresses have been blocked\n#############################################################\n" >> /root/maltrail-found-$(date +'%Y-%m-%d').log


for S in ${IPSCAN}; do
IPADD=$(du -sh "$S" 2>/dev/null | cut -f1)
echo "scan address "$S" .
scan address "$IPADD"."
# ipv4
sudo ipset add blacklists "$S" 2> /dev/null
# ipv6
sudo ipset add blacklists2 "$S" 2> /dev/null

done

# make sure url addresses are identified and blocked

for S in ${dig}; do
IPADD=$(du -sh "$S" 2>/dev/null | cut -f1)
echo "scan address "$S" .
scan address "$IPADD"."
# ipv4
sudo ipset add blacklists "$S" 2> /dev/null
# ipv6
sudo ipset add blacklists2 "$S" 2> /dev/null

done

sudo -i truncate -s 0 /opt/auto-clamIPS/maltrail/logs/dig.log

sudo -i ipset save blacklists > /etc/ipset_maltrail.conf
sudo -i ipset save blacklists2 > /etc/ipset_maltrail2.conf

sudo echo "(malware)" >> /opt/auto-clamIPS/notify-clamMA/logs/notify2.log

exit 0
