#!/bin/bash

sudo ipset flush blacklists 

sudo ipset flush blacklists2 

sudo -i truncate -s 0 /etc/ipset_maltrail.conf
sudo -i truncate -s 0 /etc/ipset_maltrail2.conf
