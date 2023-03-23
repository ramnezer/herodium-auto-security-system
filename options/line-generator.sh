#!/bin/bash 



##################################
### clamscan-root-week options ###
##################################


#################################################################################################################################

full_scan1=$(grep -E 'scheduler full-scan = 1|scheduler full-scan= 1|scheduler full-scan =1|scheduler full-scan=1' /opt/auto-clamIPS/auto-clamav/options/options.conf)
full_scan2=$(grep -E 'scheduler full-scan = 2|scheduler full-scan= 2|scheduler full-scan =2|scheduler full-scan=2' /opt/auto-clamIPS/auto-clamav/options/options.conf)
full_scan3=$(grep -E 'scheduler full-scan = 3|scheduler full-scan= 3|scheduler full-scan =3|scheduler full-scan=3' /opt/auto-clamIPS/auto-clamav/options/options.conf)
full_scan4=$(grep -E 'scheduler full-scan = 4|scheduler full-scan= 4|scheduler full-scan =4|scheduler full-scan=4' /opt/auto-clamIPS/auto-clamav/options/options.conf)
take_number1="/etc/systemd/system/clamscan-root-week.timer"


number1=$(sed '/^$/d' $take_number1 | cat $take_number1 | echo $(grep  -Fn 'OnCalendar=' $take_number1) | cut -d':' -f-1)

if [ "$full_scan1" ]
then

awk  'NR=="'$number1'" {$0="OnCalendar=*-*-* 00,12:00:00"} 1'  $take_number1 > tmp && mv tmp $take_number1 

systemctl daemon-reload
systemctl restart clamscan-root-week.timer
###

elif [ "$full_scan2" ]
then

awk  'NR=="'$number1'" {$0="OnCalendar=*-*-* 3:00:00"} 1'  $take_number1 > tmp && mv tmp $take_number1 

systemctl daemon-reload
systemctl restart clamscan-root-week.timer
###

elif [ "$full_scan3" ]
then

awk  'NR=="'$number1'" {$0="OnCalendar=Sat 3:00:00"} 1'  $take_number1 > tmp && mv tmp $take_number1 

systemctl daemon-reload
systemctl restart clamscan-root-week.timer
###

elif [ "$full_scan4" ]
then

awk  'NR=="'$number1'" {$0="OnCalendar=*-*-15 03:00:00"} 1'  $take_number1 > tmp && mv tmp $take_number1 

systemctl daemon-reload
systemctl restart clamscan-root-week.timer
###

fi

###

full_scan_e=$(grep -E 'full-scan = enable|full-scan= enable|full-scan =enable|full-scan=enable' /opt/auto-clamIPS/auto-clamav/options/options.conf)
full_scan_d=$(grep -E 'full-scan = disable|full-scan= disable|full-scan =disable|full-scan=disable' /opt/auto-clamIPS/auto-clamav/options/options.conf)

if [ "$full_scan_e" ]
then

systemctl start clamscan-root-week.timer
systemctl enable clamscan-root-week.timer

elif [ "$full_scan_d" ]
then

systemctl stop clamscan-root-week.timer
systemctl disable clamscan-root-week.timer

fi

#################################################################################################################################
#################################################################################################################################


#############################
### clamscan-home options ###
#############################


#################################################################################################################################

home_scan1=$(grep -E 'scheduler home-scan = 1|scheduler home-scan= 1|scheduler home-scan =1|scheduler home-scan=1' /opt/auto-clamIPS/auto-clamav/options/options.conf)
home_scan2=$(grep -E 'scheduler home-scan = 2|scheduler home-scan= 2|scheduler home-scan =2|scheduler home-scan=2' /opt/auto-clamIPS/auto-clamav/options/options.conf)
home_scan3=$(grep -E 'scheduler home-scan = 3|scheduler home-scan= 3|scheduler home-scan =3|scheduler home-scan=3' /opt/auto-clamIPS/auto-clamav/options/options.conf)
home_scan4=$(grep -E 'scheduler home-scan = 4|scheduler home-scan= 4|scheduler home-scan =4|scheduler home-scan=4' /opt/auto-clamIPS/auto-clamav/options/options.conf)
take_number2="/etc/systemd/system/clamscan-home-day.timer"

###
number2=$(sed '/^$/d' $take_number2 | cat $take_number2 | echo $(grep  -Fn 'OnCalendar=' $take_number2) | cut -d':' -f-1)


if [ "$home_scan1" ]
then

awk  'NR=="'$number2'" {$0="OnCalendar=*-*-* 00,06,12,18:00:00"} 1'  $take_number2 > tmp && mv tmp $take_number2 

systemctl daemon-reload
systemctl restart clamscan-home-day.timer
###

elif [ "$home_scan2" ] 
then

awk  'NR=="'$number2'" {$0="OnCalendar=*-*-* 00,12:00:00"} 1'  $take_number2 > tmp && mv tmp $take_number2 

systemctl daemon-reload
systemctl restart clamscan-home-day.timer
###

elif [ "$home_scan3" ]
then

awk  'NR=="'$number2'" {$0="OnCalendar=*-*-* 00:00:00"} 1'  $take_number2 > tmp && mv tmp $take_number2

systemctl daemon-reload
systemctl restart clamscan-home-day.timer
###

elif [ "$home_scan4" ]
then

awk  'NR=="'$number2'" {$0="OnCalendar=Sat 3:00:00"} 1'  $take_number2 > tmp && mv tmp $take_number2 

systemctl daemon-reload
systemctl restart clamscan-home-day.timer
###

fi

###
home_scan_e=$(grep -E 'home-scan = enable|home-scan= enable|home-scan =enable|home-scan=enable' /opt/auto-clamIPS/auto-clamav/options/options.conf)
home_scan_d=$(grep -E 'home-scan = disable|home-scan= disable|home-scan =disable|home-scan=disable' /opt/auto-clamIPS/auto-clamav/options/options.conf)

if [ "$home_scan_e" ]
then

systemctl start clamscan-home-day.timer
systemctl enable clamscan-home-day.timer
###

elif [ "$home_scan_d" ]
then
###

systemctl stop clamscan-home-day.timer
systemctl disable clamscan-home-day.timer

fi


#################################################################################################################################
#################################################################################################################################


##################################
###   clam-real-time-options   ###
##################################


clam_real_time_e=$(grep -E 'clam-real-time = enable|clam-real-time= enable|clam-real-time =enable|clam-real-time=enable' /opt/auto-clamIPS/auto-clamav/options/options.conf)
clam_real_time_d=$(grep -E 'clam-real-time = disable|clam-real-time= disable|clam-real-time =disable|clam-real-time=disable' /opt/auto-clamIPS/auto-clamav/options/options.conf)

if [ "$clam_real_time_e" ]
then

systemctl start if-change-scan.timer
systemctl enable if-change-scan.timer

elif [ "$clam_real_time_d" ]
then

systemctl stop if-change-scan.timer
systemctl disable if-change-scan.timer

fi


#################################################################################################################################
#################################################################################################################################


#####################################
###   auto-move-malware-options   ###
#####################################


move_malware_e=$(grep -E 'move-malware = enable|move-malware= enable|move-malware =enable|move-malware=enable' /opt/auto-clamIPS/auto-clamav/options/options.conf)
move_malware_d=$(grep -E 'move-malware = disable|move-malware= disable|move-malware =disable|move-malware=disable' /opt/auto-clamIPS/auto-clamav/options/options.conf)
take_number3="/opt/auto-clamIPS/auto-clamav/clamav-scan-if.sh"
take_number4="/opt/auto-clamIPS/auto-clamav/clamav-scan-home2.sh"
move=$(echo '--move=/home/$user/auto-clamIPS/VIRUS-FOUND/')
move2=$(echo '$option_move')

number3=$(sed '/^$/d' $take_number3 | cat $take_number3 | echo $(grep  -Fn 'clamscan --infected --recursive' $take_number3) | cut -d':' -f-1)
number4=$(sed '/^$/d' $take_number4 | cat $take_number4 | echo $(grep  -Fn 'clamscan --infected --recursive' $take_number4) | cut -d':' -f-1)

if [ "$move_malware_e" ]
then


awk  'NR=="'$number3'" {$8="'$move'"} 1'  $take_number3 > tmp && mv tmp $take_number3
awk  'NR=="'$number4'" {$9="'$move'"} 1'  $take_number4 > tmp && mv tmp $take_number4

elif [ "$move_malware_d" ]
then

awk  'NR=="'$number3'" {$8="'$move2'"} 1'  $take_number3 > tmp && mv tmp $take_number3
awk  'NR=="'$number4'" {$9="'$move2'"} 1'  $take_number4 > tmp && mv tmp $take_number4


fi



#################################################################################################################################
#################################################################################################################################


######################################
###   maltrail-real-time-opition   ###
######################################


maltrail_real_e=$(grep -E 'maltrail-real-time = enable|maltrail-real-time= enable|maltrail-real-time =enable|maltrail-real-time=enable' /opt/auto-clamIPS/auto-clamav/options/options.conf)
maltrail_real_d=$(grep -E 'maltrail-real-time = disable|maltrail-real-time= disable|maltrail-real-time =disable|maltrail-real-time=disable' /opt/auto-clamIPS/auto-clamav/options/options.conf)

if [ "$maltrail_real_e" ]
then

systemctl start maltrail-sensor
systemctl enable maltrail-sensor
###

elif [ "$maltrail_real_d" ]
then
###

systemctl stop maltrail-sensor
systemctl disable maltrail-sensor

fi


###################################
### maltrail-blacklist-cleaning ###
###################################


maltrail_blacklist1=$(grep -E 'blacklist-cleaning = 1|blacklist-cleaning= 1|blacklist-cleaning =1|blacklist-cleaning=1' /opt/auto-clamIPS/auto-clamav/options/options.conf)
maltrail_blacklist2=$(grep -E 'blacklist-cleaning = 2|blacklist-cleaning= 2|blacklist-cleaning =2|blacklist-cleaning=2' /opt/auto-clamIPS/auto-clamav/options/options.conf)

take_number5="/etc/systemd/system/flush_blacklists.timer"


number5=$(sed '/^$/d' $take_number5 | cat $take_number5 | echo $(grep  -Fn 'OnCalendar=' $take_number5) | cut -d':' -f-1)

if [ "$maltrail_blacklist1" ]
then

awk  'NR=="'$number5'" {$0="OnCalendar=Sat 2:00:00"} 1'  $take_number5 > tmp && mv tmp $take_number5 

systemctl daemon-reload
systemctl restart flush_blacklists.timer
###

elif [ "$maltrail_blacklist2" ]
then

awk  'NR=="'$number5'" {$0="OnCalendar=*-*-15 02:00:00"} 1'  $take_number5 > tmp && mv tmp $take_number5 

systemctl daemon-reload
systemctl restart flush_blacklists.timer
###


fi

###

blacklist_cleaning_e=$(grep -E 'maltrail-blacklist-cleaning = enable|maltrail-blacklist-cleaning= enable|maltrail-blacklist-cleaning =enable|maltrail-blacklist-cleaning=enable' /opt/auto-clamIPS/auto-clamav/options/options.conf)
blacklist_cleaning_d=$(grep -E 'maltrail-blacklist-cleaning = disable|maltrail-blacklist-cleaning= disable|maltrail-blacklist-cleaning =disable|maltrail-blacklist-cleaning=disable' /opt/auto-clamIPS/auto-clamav/options/options.conf)

if [ "$blacklist_cleaning_e" ]
then

systemctl start flush_blacklists.timer
systemctl enable flush_blacklists.timer
###

elif [ "$blacklist_cleaning_d" ]
then
###

systemctl stop flush_blacklists.timer
systemctl disable flush_blacklists.timer

fi



#############################
### rkhunter-auto-scanner ###
#############################


#################################################################################################################################

rkhunter_scan1=$(grep -E 'rkhunter-scan = 1|rkhunter-scan= 1|rkhunter-scan =1|rkhunter-scan=1' /opt/auto-clamIPS/auto-clamav/options/options.conf)
rkhunter_scan2=$(grep -E 'rkhunter-scan = 2|rkhunter-scan= 2|rkhunter-scan =2|rkhunter-scan=2' /opt/auto-clamIPS/auto-clamav/options/options.conf)
rkhunter_scan3=$(grep -E 'rkhunter-scan = 3|rkhunter-scan= 3|rkhunter-scan =3|rkhunter-scan=3' /opt/auto-clamIPS/auto-clamav/options/options.conf)
rkhunter_scan4=$(grep -E 'rkhunter-scan = 4|rkhunter-scan= 4|rkhunter-scan =4|rkhunter-scan=4' /opt/auto-clamIPS/auto-clamav/options/options.conf)
take_number6="/etc/systemd/system/rkhunter_scanner.timer"


number6=$(sed '/^$/d' $take_number6 | cat $take_number6 | echo $(grep  -Fn 'OnCalendar=' $take_number6) | cut -d':' -f-1)

if [ "$rkhunter_scan1" ]
then

awk  'NR=="'$number6'" {$0="OnCalendar=*-*-* 00,06,12,18:00:00"} 1'  $take_number6 > tmp && mv tmp $take_number6 

systemctl daemon-reload
systemctl restart rkhunter_scanner.timer
###

elif [ "$rkhunter_scan2" ]
then

awk  'NR=="'$number6'" {$0="OnCalendar=*-*-* 00,12:00:00"} 1'  $take_number6 > tmp && mv tmp $take_number6 

systemctl daemon-reload
systemctl restart rkhunter_scanner.timer
###

elif [ "$rkhunter_scan3" ]
then

awk  'NR=="'$number6'" {$0="OnCalendar=*-*-* 00:00:00"} 1'  $take_number6 > tmp && mv tmp $take_number6 

systemctl daemon-reload
systemctl restart rkhunter_scanner.timer
###

elif [ "$rkhunter_scan4" ]
then

awk  'NR=="'$number6'" {$0="OnCalendar=Sat 3:00:00"} 1'  $take_number6 > tmp && mv tmp $take_number6 

systemctl daemon-reload
systemctl restart rkhunter_scanner.timer
###

fi

###

rkhunter_scan_e=$(grep -E 'rkhunter-auto-scanner = enable|rkhunter-auto-scanner= enable|rkhunter-auto-scanner =enable|rkhunter-auto-scanner=enable' /opt/auto-clamIPS/auto-clamav/options/options.conf)
rkhunter_scan_d=$(grep -E 'rkhunter-auto-scanner = disable|rkhunter-auto-scanner= disable|rkhunter-auto-scanner =disable|rkhunter-auto-scanner=disable' /opt/auto-clamIPS/auto-clamav/options/options.conf)

if [ "$rkhunter_scan_e" ]
then

systemctl start rkhunter_scanner.timer
systemctl enable rkhunter_scanner.timer

elif [ "$rkhunter_scan_d" ]
then

systemctl stop rkhunter_scanner.timer
systemctl disable rkhunter_scanner.timer

fi

#################################################################################################################################
