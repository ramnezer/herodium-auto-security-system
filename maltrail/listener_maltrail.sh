#!/bin/bash

ipset restore -f -! /etc/ipset_maltrail.conf
ipset restore -f -! /etc/ipset_maltrail2.conf


ipset create blacklists hash:ip timeout 0 maxelem 150000
ipset create blacklists2 hash:ip timeout 0 family inet6 maxelem 150000

iptables -C INPUT  -m set  --match-set blacklists  src -j DROP 2> /dev/null || iptables -I INPUT 1  -m set  --match-set blacklists src -j  DROP 2> /dev/null
ip6tables -C INPUT  -m set  --match-set blacklists2  src -j DROP 2> /dev/null || ip6tables -I INPUT 1  -m set  --match-set blacklists2 src -j DROP 2> /dev/null

touch /var/log/maltrail/$(date +"%Y-%m-%d").log

### To avoid an unnecessary warning after system reboot tail will only listen to new results from the target log file
data=$(date +"%Y-%m-%d")
timeout 10m tail -n0 -f "/var/log/maltrail/$data.log" >>"/opt/auto-clamIPS/maltrail/logs/scan.log"


/opt/auto-clamIPS/maltrail/check_ml_log.sh & /opt/auto-clamIPS/maltrail/maltrail_loop_listener.sh
 
#############################################################################################################################
