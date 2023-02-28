#!/bin/bash

sudo -i ipset restore -f -! /etc/ipset_maltrail.conf
sudo -i ipset restore -f -! /etc/ipset_maltrail2.conf


sudo ipset create blacklists hash:ip timeout 0 maxelem 150000
sudo ipset create blacklists2 hash:ip timeout 0 family inet6 maxelem 150000

sudo iptables -C INPUT  -m set  --match-set blacklists  src -j DROP 2> /dev/null || sudo iptables -I INPUT 1  -m set  --match-set blacklists src -j  DROP 2> /dev/null
sudo ip6tables -C INPUT  -m set  --match-set blacklists2  src -j DROP 2> /dev/null || sudo ip6tables -I INPUT 1  -m set  --match-set blacklists2 src -j DROP 2> /dev/null

sudo touch /var/log/maltrail/$(date +"%Y-%m-%d").log

### To avoid an unnecessary warning after system reboot tail will only listen to new results from the target log file
timeout  10m  sudo -i tail -n0 -f /var/log/maltrail/$(date +"%Y-%m-%d").log >>'/opt/auto-clamIPS/maltrail/logs/scan.log'


sudo bash /opt/auto-clamIPS/maltrail/maltrail_fix_listener.sh & sudo bash /opt/auto-clamIPS/maltrail/maltrail_fix_service.sh
 
#############################################################################################################################
