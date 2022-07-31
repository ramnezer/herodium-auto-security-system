#!/bin/bash 

sudo systemctl stop clamav-freshclam
sudo freshclam  >clamav-scan/auto_update_clamav/freshclam_error.log 2>&1
sudo systemctl start clamav-freshclam
