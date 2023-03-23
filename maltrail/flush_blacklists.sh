#!/bin/bash

ipset flush blacklists 

ipset flush blacklists2 

truncate -s 0 /etc/ipset_maltrail.conf
truncate -s 0 /etc/ipset_maltrail2.conf
