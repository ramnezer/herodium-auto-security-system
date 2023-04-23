#!/bin/bash
/opt/auto-clamIPS/notify-clamMA/check_user.sh
IPSCAN=$(cat /opt/auto-clamIPS/maltrail/logs/ipset.log)
ipset_log="/opt/auto-clamIPS/maltrail/logs/ipset.log"
dig_log="/opt/auto-clamIPS/maltrail/logs/dig.log"
user=$( users | cut -d ' ' -f 1)
dig=$(dig "$IPSCAN" +short >> "$dig_log" && dig AAAA "$IPSCAN" +short >> "$dig_log" && cat "$dig_log")

### For distributions with non-english languages,get the correct desktop name 
### and convert it to universal(for english and non-english distro)variable
desktop1=$(cat /home/"$user"/.config/user-dirs.dirs | grep "XDG_DESKTOP_DIR" | cut -d'/' -f2- | tr -d '"')

echo $(cat "$ipset_log") >> "/home/"$user"/"$desktop1"/maltrail-found-$(date +'%Y-%m-%d').log"
echo $(cat "$ipset_log") >> "/root/maltrail-found-$(date +'%Y-%m-%d').log"

printf  "\n#############################################################\nfound malicious traffic check with\n[sudo ipset list blacklists && sudo ipset list blacklists2]\nif the malicious addresses have been blocked\n#############################################################\n" >> "/home/"$user"/"$desktop1"/maltrail-found-$(date +'%Y-%m-%d').log"

printf  "\n#############################################################\nfound malicious traffic check with\n[sudo ipset list blacklists && sudo ipset list blacklists2]\nif the malicious addresses have been blocked\n#############################################################\n" >> "/root/maltrail-found-$(date +'%Y-%m-%d').log"


for S in ${IPSCAN}; do
IPADD=$(du -sh "$S" 2>/dev/null | cut -f1)

# ipv4
ipset add blacklists "$S" 2> /dev/null
# ipv6
ipset add blacklists2 "$S" 2> /dev/null

done

# make sure url addresses are identified and blocked

for S in ${dig}; do
IPADD=$(du -sh "$S" 2>/dev/null | cut -f1)

# ipv4
ipset add blacklists "$S" 2> /dev/null
# ipv6
ipset add blacklists2 "$S" 2> /dev/null

done

truncate -s 0 /opt/auto-clamIPS/maltrail/logs/dig.log

ipset save blacklists > /etc/ipset_maltrail.conf
ipset save blacklists2 > /etc/ipset_maltrail2.conf

echo "(malware)" >> /opt/auto-clamIPS/notify-clamMA/logs/notify2.log

exit 0
