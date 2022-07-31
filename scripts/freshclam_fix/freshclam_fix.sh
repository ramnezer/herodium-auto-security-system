#!/bin/bash 

sudo systemctl stop clamav-freshclam
sudo freshclam  >freshclam_error.log 2>&1
sudo systemctl start clamav-freshclam
