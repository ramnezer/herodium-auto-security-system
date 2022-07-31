#!/bin/bash

sudo -i ipset restore -f -! /etc/ipset.conf

sudo iptables -C INPUT  -m set  --match-set blacklists  src -j DROP 2> /dev/null || sudo iptables -I INPUT 1  -m set  --match-set blacklists src -j  DROP 2> /dev/null
sudo ip6tables -C INPUT  -m set  --match-set blacklists2  src -j DROP 2> /dev/null || sudo ip6tables -I INPUT 1  -m set  --match-set blacklists2 src -j DROP 2> /dev/null

sudo touch /var/log/maltrail/$(date +"%Y-%m-%d").log
### To avoid an unnecessary warning after system reboot tail will only listen to new results from the target log file
sudo -i tail -n0 -f /var/log/maltrail/$(date +"%Y-%m-%d").log >>'/opt/auto-clamIPS/maltrail/logs/scan.log'
