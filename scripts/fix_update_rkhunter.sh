#!/bin/bash 

############################
### fix update rkhunter  ###
############################

###
UPDATE_MIRRORS=$(grep -E 'UPDATE_MIRRORS=0' /etc/rkhunter.conf)
take_number1="/etc/rkhunter.conf"
number1=$(echo $(grep  -Fn 'UPDATE_MIRRORS=' $take_number1) | cut -d':' -f-1)
###

if [ "$UPDATE_MIRRORS" ]
then

awk  'NR=="'$number1'" {$0="UPDATE_MIRRORS=1"} 1'  $take_number1 > tmp && mv tmp $take_number1 

fi

###
MIRRORS_MODE=$(grep -E 'MIRRORS_MODE=1' /etc/rkhunter.conf)
take_number2="/etc/rkhunter.conf"
number2=$(echo $(grep  -Fn 'MIRRORS_MODE=' $take_number2) | cut -d':' -f-1)
###

if [ "$MIRRORS_MODE" ]
then

awk  'NR=="'$number2'" {$0="MIRRORS_MODE=0"} 1'  $take_number2 > tmp && mv tmp $take_number2 

fi

###

WEB_CMD=$(grep -E 'WEB_CMD="/bin/false"' /etc/rkhunter.conf)
take_number3="/etc/rkhunter.conf"
number3=$(echo $(grep  -Fn 'WEB_CMD="/bin/false"' $take_number3) | cut -d':' -f-1)

if [ "$WEB_CMD" ]
then

awk  'NR=="'$number3'" {$0="WEB_CMD=" } 1'  $take_number3 > tmp && mv tmp $take_number3 


fi




