#!/bin/bash 

#########################
### optimize maltrail ###
#########################

###
UPDATE_TRAILS=$(grep -E 'USE_SERVER_UPDATE_TRAILS false' /opt/maltrail/maltrail.conf)
take_number1="/opt/maltrail/maltrail.conf"
number1=$(sed '/^$/d' $take_number1 | cat $take_number1 | echo $(grep  -Fn 'USE_SERVER_UPDATE_TRAILS' $take_number1) | cut -d':' -f-1)
###

if [ "$UPDATE_TRAILS" ]
then

awk  'NR=="'$number1'" {$0="USE_SERVER_UPDATE_TRAILS true"} 1'  $take_number1 > tmp && mv tmp $take_number1 

fi

###
ENABLE_FEEDS=$(grep -E 'DISABLED_FEEDS turris' /opt/maltrail/maltrail.conf)
take_number2="/opt/maltrail/maltrail.conf"
number2=$(sed '/^$/d' $take_number2 | cat $take_number2 | echo $(grep  -Fn 'DISABLED_FEEDS' $take_number2) | cut -d':' -f-1)
###

if [ "$ENABLE_FEEDS" ]
then

awk  'NR=="'$number2'" {$0="# DISABLED_FEEDS turris, ciarmy, policeman, myip, alienvault"} 1'  $take_number2 > tmp && mv tmp $take_number2 

fi

###

# if value of one or both variables was false ,restart the service. else ignore 
if [ "$UPDATE_TRAILS" ==  'USE_SERVER_UPDATE_TRAILS false' ] ||  [ "$ENABLE_FEEDS" == 'DISABLED_FEEDS turris, ciarmy, policeman, myip, alienvault' ]
then

systemctl restart maltrail-sensor

fi
