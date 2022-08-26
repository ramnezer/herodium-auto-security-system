#!/bin/bash

chmod +x auto-clam-antivirus.py
chmod +x uninstall.py
chmod +x scripts/fix.sh
chmod +x scripts/freshclam_fix/freshclam_fix.py
chmod +x scripts/freshclam_fix/freshclam_fix.sh
chmod +x scripts/notify_send.sh
chmod +x clamav-scan/auto_update_clamav/freshclam_fix.sh
chmod +x clamav-scan/clamav-root-scan.sh
chmod +x clamav-scan/clamav-scan-home.sh
chmod +x clamav-scan/change_service/if-change.sh
chmod +x clamav-scan/change_service/if-change-scan.py
chmod +x clamav-scan/auto_update_clamav/auto-update-clamav.py
chmod +x clamav-scan/change_service/clamav-scan-if.sh
chmod +x clamav-scan/change_service/clamav-scan-if2.sh
chmod +x clamav-scan/change_service/clamav-scan-home2.sh
chmod +x maltrail/blacklist.sh
chmod +x maltrail/listener_maltrail.sh
chmod +x maltrail/maltrail_scan.py
chmod +x maltrail/flush_blacklists.sh
chmod +x notify-send/notify-send.py
chmod +x notify-send/notify-reset-boot.py



### *Prepare the system for installation* ###

##### The program will perform necessary
##### Steps to ensure the success of the installation 

##### fix error ("`Could not get lock /var") if it exists.
sudo rm -rf /var/lib/dpkg/updates/*
sudo rm -rf /var/lib/dpkg/lock-frontend
sudo rm -rf /var/lib/apt/lists/lock
sudo rm -rf /var/lib/apt/lists/lock-frontend
sudo rm -rf /var/cache/apt/archives/lock
sudo rm -rf /var/lib/dpkg/lock
sudo dpkg --configure -a
sudo apt install -f
######

###### check for missing and broken packages and repair if necessary.
sudo apt-get --fix-broken install -y
sudo apt-get update --fix-missing
sudo dpkg --configure -a
sudo apt-get install -f
######

###### check if python3.8 is installed
sudo apt-get install python3.8 -y 
######

###### install make
sudo apt-get install make
######

###### install dialog
sudo apt-get install dialog
######

##### make sure git is install
sudo apt-get install git -yy

HEIGHT=15
WIDTH=76
CHOICE_HEIGHT=4
BACKTITLE="https://github.com/ramner98/auto-clamIPS.git"
TITLE="auto-clamIPS"
MENU="Choose one of the following options:"

OPTIONS=(1 "install auto-clamIPS"
         2 "uninstall")

CHOICE=$(dialog --clear \
                --backtitle "$BACKTITLE" \
                --title "$TITLE" \
                --menu "$MENU" \
                $HEIGHT $WIDTH $CHOICE_HEIGHT \
                "${OPTIONS[@]}" \
                2>&1 >/dev/tty)

clear
case $CHOICE in
        1)
            sudo python3 auto-clam-antivirus.py
            echo ""
	        echo ""
            echo ""
             sleep 3
                exit
            ;;
        2)
            sudo python3 uninstall.py
            echo ""
	        echo ""
            echo ""
             sleep 3
                exit
            ;;

esac
