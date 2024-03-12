#!/bin/bash

###
### fuzzy-logic-smart-system-cpulimit
### this script is one of two parts coordinated together
### with '/opt/auto-clamIPS/auto-clamav/integral_cpulimit.sh'
###


# Limit 'clamdscan' to a defined work level,
# prevent duplicate activation attempts if 
# the limit has already run

while

 run_time=$(ps -o etime -p $(pgrep -f  "clamdscan") 2> /dev/null | grep -E '[0-9]' | tail --lines=1 | sed -r 's/\s+//g')
 
 if [ "$run_time" == "" ]
 then

  check=$(pgrep -f  "/usr/sbin/clamd")
  check_cpu5=$(pgrep -f  "cpulimit -l 5 -p $check")

  if [ "$check" ] && [ "$check_cpu5" == "" ]
  then
 
  cpulimit -l 5 -p $check
 
  fi

###

 elif [[ "$run_time" > "00:00" ]] && [[ "$run_time" < "00:03" ]]
 then

  check=$(pgrep -f  "/usr/sbin/clamd")
  check_cpu15=$(pgrep -f  "cpulimit -l 15 -p $check")

  if [ "$check" ] && [ "$check_cpu15" == "" ]
  then
 
  cpulimit -l 15 -p $check
  
  fi

###

 elif [[ "$run_time" > "00:03" ]] && [[ "$run_time" < "00:06" ]]
 then 
  
  check=$(pgrep -f  "/usr/sbin/clamd")
  check_cpu20=$(pgrep -f  "cpulimit -l 20 -p $check")

  if [ "$check" ] && [ "$check_cpu20" == "" ]
  then
 
  cpulimit -l 20 -p $check

  fi

###

 elif [[ "$run_time" > "00:06" ]] && [[ "$run_time" < "00:10" ]]
 then 
  
  check=$(pgrep -f  "/usr/sbin/clamd")
  check_cpu25=$(pgrep -f  "cpulimit -l 25 -p $check")

  if [ "$check" ] && [ "$check_cpu25" == "" ]
  then
 
  cpulimit -l 25 -p $check
 
  fi

###

 elif [[ "$run_time" > "00:10" ]] && [[ "$run_time" < "00:15" ]]
 then 
  
  check=$(pgrep -f  "/usr/sbin/clamd")
  check_cpu30=$(pgrep -f  "cpulimit -l 30 -p $check")

  if [ "$check" ] && [ "$check_cpu30" == "" ]
  then
 
  cpulimit -l 30 -p $check
 
  fi

###

 elif [[ "$run_time" > "00:15" ]] && [[ "$run_time" < "00:20" ]]
 then 
  
  check=$(pgrep -f  "/usr/sbin/clamd")
  check_cpu35=$(pgrep -f  "cpulimit -l 35 -p $check")

  if [ "$check" ] && [ "$check_cpu35" == "" ]
  then
 
  cpulimit -l 35 -p $check
 
  fi

###

 elif [[ "$run_time" > "00:20" ]] && [[ "$run_time" < "00:25" ]]
 then 
  
  check=$(pgrep -f  "/usr/sbin/clamd")
  check_cpu40=$(pgrep -f  "cpulimit -l 40 -p $check")

  if [ "$check" ] && [ "$check_cpu40" == "" ]
  then
 
  cpulimit -l 40 -p $check
 
  fi

###

 elif [[ "$run_time" > "00:25" ]] && [[ "$run_time" < "00:35" ]]
 then 
  
  check=$(pgrep -f  "/usr/sbin/clamd")
  check_cpu45=$(pgrep -f  "cpulimit -l 45 -p $check")

  if [ "$check" ] && [ "$check_cpu45" == "" ]
  then
 
  cpulimit -l 45 -p $check
 
  fi

###

 elif [[ "$run_time" > "00:35" ]] && [[ "$run_time" < "00:45" ]]
 then 
  
  check=$(pgrep -f  "/usr/sbin/clamd")
  check_cpu50=$(pgrep -f  "cpulimit -l 50 -p $check")

  if [ "$check" ] && [ "$check_cpu50" == "" ]
  then
 
  cpulimit -l 50 -p $check
 
  fi

###

 elif [[ "$run_time" > "00:45" ]] && [[ "$run_time" < "01:05" ]]
 then 
  
  check=$(pgrep -f  "/usr/sbin/clamd")
  check_cpu55=$(pgrep -f  "cpulimit -l 55 -p $check")

  if [ "$check" ] && [ "$check_cpu55" == "" ]
  then
 
  cpulimit -l 55 -p $check
 
  fi

###

 elif [[ "$run_time" > "01:05" ]] && [[ "$run_time" < "01:35" ]]
 then 
  
  check=$(pgrep -f  "/usr/sbin/clamd")
  check_cpu60=$(pgrep -f  "cpulimit -l 60 -p $check")

  if [ "$check" ] && [ "$check_cpu60" == "" ]
  then
 
  cpulimit -l 60 -p $check
 
  fi

###

 elif [[ "$run_time" > "01:35" ]] && [[ "$run_time" < "02:15" ]]
 then 
  
  check=$(pgrep -f  "/usr/sbin/clamd")
  check_cpu65=$(pgrep -f  "cpulimit -l 65 -p $check")

  if [ "$check" ] && [ "$check_cpu65" == "" ]
  then
 
  cpulimit -l 65 -p $check
 
  fi

###

 elif [[ "$run_time" > "02:15" ]] && [[ "$run_time" < "03:35" ]]
 then 
  
  check=$(pgrep -f  "/usr/sbin/clamd")
  check_cpu70=$(pgrep -f  "cpulimit -l 70 -p $check")

  if [ "$check" ] && [ "$check_cpu70" == "" ]
  then
 
  cpulimit -l 70 -p $check
 
  fi

###

 elif [[ "$run_time" > "03:35" ]]
 then 
  
  check=$(pgrep -f  "/usr/sbin/clamd")
  check_cpu75=$(pgrep -f  "cpulimit -l 75 -p $check")

  if [ "$check" ] && [ "$check_cpu75" == "" ]
  then
 
  cpulimit -l 75 -p $check
 
  fi

###

###

 fi


do
    :
done
