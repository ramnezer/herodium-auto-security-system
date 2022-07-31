#!/bin/bash


##### fix error ("`Could not get lock /var") if it exists.
sudo rm -rf /var/lib/dpkg/updates/*
sudo rm -rf /var/lib/dpkg/lock-frontend
sudo rm -rf /var/lib/apt/lists/lock
sudo rm -rf /var/lib/apt/lists/lock-frontend
sudo rm -rf /var/cache/apt/archives/lock
sudo rm -rf /var/lib/dpkg/lock
sudo dpkg --configure -a
sudo apt-get install -f
###### check for missing and broken packages and repair if necessary.
sudo apt-get --fix-broken install -y
sudo apt-get update --fix-missing
sudo dpkg --configure -a
sudo apt-get install -f
