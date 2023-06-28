#!/bin/bash

chmod +x auto-clam-antivirus.py
chmod +x uninstall.py
chmod +x scripts/fix.sh
chmod +x scripts/freshclam_fix/freshclam_fix.py
chmod +x scripts/freshclam_fix/freshclam_fix.sh
chmod +x scripts/notify_send.sh
chmod +x scripts/maltrail-clear-symbols.sh
chmod +x clamav-scan/auto_update_clamav/freshclam_fix.sh
chmod +x clamav-scan/clamav-root-scan.sh
chmod +x clamav-scan/clamav-scan-home.sh
chmod +x clamav-scan/change_service/if-change.sh
chmod +x clamav-scan/change_service/if-change-scan.py
chmod +x clamav-scan/auto_update_clamav/auto-update-clamav.py
chmod +x clamav-scan/change_service/clamav-scan-if.sh
chmod +x clamav-scan/change_service/clamav-scan-if2.sh
chmod +x clamav-scan/change_service/change-li.sh
chmod +x clamav-scan/change_service/cpulimit-chack.sh
chmod +x clamav-scan/change_service/cpulimit_inotifywait.sh
chmod +x clamav-scan/change_service/integral_cpulimit.sh
chmod +x clamav-scan/media_scan/check_media.sh
chmod +x clamav-scan/media_scan/media_if-change.sh
chmod +x clamav-scan/media_scan/media-li.sh
chmod +x maltrail/blacklist.sh
chmod +x maltrail/listener_maltrail.sh
chmod +x maltrail/maltrail_scan.py
chmod +x maltrail/flush_blacklists.sh
chmod +x notify-send/notify-send.py
chmod +x notify-send/notify-reset-boot.py
chmod +x options/edit-options.sh
chmod +x options/line-generator.sh
chmod +x scripts/optimize_maltrail.sh
chmod +x scripts/fix_update_rkhunter.sh
chmod +x scripts/check_ml_log.sh
chmod +x scripts/maltrail_loop_listener.sh
chmod +x scripts/check_user.sh
chmod +x rkhunter/rkhunter_scanner.sh
 


### *Prepare the system for installation* ###


###### check for missing and broken packages and repair if necessary.
sudo apt-get --fix-broken install -y
sudo apt-get update --fix-missing
sudo dpkg --configure -a
sudo apt-get install -f
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
BACKTITLE="https://github.com/ramner98/herodium-auto-security-system.git"
TITLE="herodium-auto-security-system"
MENU="Choose one of the following options:"

OPTIONS=(1 "install herodium"
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
