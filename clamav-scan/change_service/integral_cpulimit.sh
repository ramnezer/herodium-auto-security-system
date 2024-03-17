#!/bin/bash

### help the first script identify the
### required change autonomously to match
### the correct limit


while
 
# 
 run_time=$(ps -o etime -p $(pgrep -f  "clamdscan") 2> /dev/null | grep -E '[0-9]' | tail --lines=1 | sed -r 's/\s+//g')
 check=$(pgrep -f  "/usr/sbin/clamd")
# 
 check_cpu5=$(pgrep -f  "cpulimit -l 5 -p $check")
 check_cpu15=$(pgrep -f  "cpulimit -l 15 -p $check")
 check_cpu20=$(pgrep -f  "cpulimit -l 20 -p $check")
 check_cpu25=$(pgrep -f  "cpulimit -l 25 -p $check")
 check_cpu30=$(pgrep -f  "cpulimit -l 30 -p $check")
 check_cpu35=$(pgrep -f  "cpulimit -l 35 -p $check")
 check_cpu40=$(pgrep -f  "cpulimit -l 40 -p $check")
 check_cpu45=$(pgrep -f  "cpulimit -l 45 -p $check")
 check_cpu50=$(pgrep -f  "cpulimit -l 50 -p $check")
 check_cpu55=$(pgrep -f  "cpulimit -l 55 -p $check")
 check_cpu60=$(pgrep -f  "cpulimit -l 60 -p $check")
 check_cpu65=$(pgrep -f  "cpulimit -l 65 -p $check")
 check_cpu70=$(pgrep -f  "cpulimit -l 70 -p $check")
 check_cpu75=$(pgrep -f  "cpulimit -l 75 -p $check") 
# 
 kill_correct=$(pgrep  -uroot -f  "cpulimit -l   $()   | -p $(pgrep -f  "/usr/sbin/clamd")")
#

###
 
 if [ "$run_time" == "" ]
 then 

# 
  if [ "$check" ] && [ "$check_cpu5" == "" ]
  then
 
### Although it is possible to kill the process more efficiently by 
### [kill "$kill_correct"] variable it is better to use a less efficient
### but more accurate list to avoid the theoretical possibility of killing
### other processes.
  kill  "$check_cpu15" "$check_cpu20" "$check_cpu25" "$check_cpu30" "$check_cpu35" "$check_cpu40" 2> /dev/null
  kill  "$check_cpu45" "$check_cpu50" "$check_cpu55" "$check_cpu60" "$check_cpu65" "$check_cpu70" "$check_cpu75" 2> /dev/null
 
  fi
#

###
 
 elif [[ "$run_time" > "00:00" ]] && [[ "$run_time" < "00:03" ]]
 then 

# 
  if [ "$check" ] && [ "$check_cpu15" == "" ]
  then
 
  kill  "$check_cpu5" "$check_cpu20" "$check_cpu25" "$check_cpu30" "$check_cpu35" "$check_cpu40" 2> /dev/null
  kill  "$check_cpu45" "$check_cpu50" "$check_cpu55" "$check_cpu60" "$check_cpu65" "$check_cpu70" "$check_cpu75" 2> /dev/null
 
  fi
#

###

 elif [[ "$run_time" > "00:03" ]] && [[ "$run_time" < "00:06" ]]
 then 

# 
  if [ "$check" ] && [ "$check_cpu20" == "" ]
  then
 
  kill "$check_cpu5" "$check_cpu15" "$check_cpu25" "$check_cpu30" "$check_cpu35" "$check_cpu40" 2> /dev/null
  kill "$check_cpu45" "$check_cpu50" "$check_cpu55" "$check_cpu60" "$check_cpu65" "$check_cpu70" "$check_cpu75" 2> /dev/null
 
  fi
#

###

#
 elif [[ "$run_time" > "00:06" ]] && [[ "$run_time" < "00:10" ]]
 then 

 
  if [ "$check" ] && [ "$check_cpu25" == "" ]
  then
 
  kill "$check_cpu5" "$check_cpu15" "$check_cpu20" "$check_cpu30" "$check_cpu35" "$check_cpu40" 2> /dev/null
  kill "$check_cpu45" "$check_cpu50" "$check_cpu55" "$check_cpu60" "$check_cpu65" "$check_cpu70" "$check_cpu75" 2> /dev/null

  fi
#

###

#
 elif [[ "$run_time" > "00:10" ]] && [[ "$run_time" < "00:15" ]]
 then 

 
  if [ "$check" ] && [ "$check_cpu30" == "" ]
  then
 
  kill "$check_cpu5" "$check_cpu15" "$check_cpu20" "$check_cpu25" "$check_cpu35" "$check_cpu40" 2> /dev/null
  kill "$check_cpu45" "$check_cpu50" "$check_cpu55" "$check_cpu60" "$check_cpu65" "$check_cpu70" "$check_cpu75" 2> /dev/null

  fi
#

###

#
 elif [[ "$run_time" > "00:15" ]] && [[ "$run_time" < "00:20" ]]
 then 

 
  if [ "$check" ] && [ "$check_cpu35" == "" ]
  then
 
  kill "$check_cpu5" "$check_cpu15" "$check_cpu20" "$check_cpu25" "$check_cpu30" "$check_cpu40" 2> /dev/null
  kill "$check_cpu45" "$check_cpu50" "$check_cpu55" "$check_cpu60" "$check_cpu65" "$check_cpu70" "$check_cpu75" 2> /dev/null

  fi
#

###

#
 elif [[ "$run_time" > "00:20" ]] && [[ "$run_time" < "00:25" ]]
 then 

 
  if [ "$check" ] && [ "$check_cpu40" == "" ]
  then
 
  kill "$check_cpu5" "$check_cpu15" "$check_cpu20" "$check_cpu25" "$check_cpu30" "$check_cpu35" 2> /dev/null
  kill "$check_cpu45" "$check_cpu50" "$check_cpu55" "$check_cpu60" "$check_cpu65" "$check_cpu70" "$check_cpu75" 2> /dev/null

  fi
#

###

#
 elif [[ "$run_time" > "00:25" ]] && [[ "$run_time" < "00:35" ]]
 then 

 
  if [ "$check" ] && [ "$check_cpu45" == "" ]
  then
 
  kill "$check_cpu5" "$check_cpu15" "$check_cpu20" "$check_cpu25" "$check_cpu30" "$check_cpu35" 2> /dev/null
  kill "$check_cpu40" "$check_cpu50" "$check_cpu55" "$check_cpu60" "$check_cpu65" "$check_cpu70" "$check_cpu75" 2> /dev/null

  fi
#

###

#
 elif [[ "$run_time" > "00:35" ]] && [[ "$run_time" < "00:45" ]]
 then 

 
  if [ "$check" ] && [ "$check_cpu50" == "" ]
  then
 
  kill "$check_cpu5" "$check_cpu15" "$check_cpu20" "$check_cpu25" "$check_cpu30" "$check_cpu35" 2> /dev/null
  kill "$check_cpu40" "$check_cpu45" "$check_cpu55" "$check_cpu60" "$check_cpu65" "$check_cpu70" "$check_cpu75" 2> /dev/null

  fi
#

###

#
 elif [[ "$run_time" > "00:45" ]] && [[ "$run_time" < "01:05" ]]
 then 

 
  if [ "$check" ] && [ "$check_cpu55" == "" ]
  then
 
  kill "$check_cpu5" "$check_cpu15" "$check_cpu20" "$check_cpu25" "$check_cpu30" "$check_cpu35" 2> /dev/null
  kill "$check_cpu40" "$check_cpu45" "$check_cpu50" "$check_cpu60" "$check_cpu65" "$check_cpu70" "$check_cpu75" 2> /dev/null

  fi
#

###

#
 elif [[ "$run_time" > "01:05" ]] && [[ "$run_time" < "01:35" ]]
 then 

 
  if [ "$check" ] && [ "$check_cpu60" == "" ]
  then
 
  kill "$check_cpu5" "$check_cpu15" "$check_cpu20" "$check_cpu25" "$check_cpu30" "$check_cpu35" 2> /dev/null
  kill "$check_cpu40" "$check_cpu45" "$check_cpu50" "$check_cpu55" "$check_cpu65" "$check_cpu70" "$check_cpu75" 2> /dev/null

  fi
#

###

#
 elif [[ "$run_time" > "01:35" ]] && [[ "$run_time" < "02:15" ]]
 then 

 
  if [ "$check" ] && [ "$check_cpu65" == "" ]
  then
 
  kill "$check_cpu5" "$check_cpu15" "$check_cpu20" "$check_cpu25" "$check_cpu30" "$check_cpu35" 2> /dev/null
  kill "$check_cpu40" "$check_cpu45" "$check_cpu50" "$check_cpu55" "$check_cpu60" "$check_cpu70" "$check_cpu75" 2> /dev/null

  fi
#

###

#
 elif [[ "$run_time" > "02:15" ]] && [[ "$run_time" < "03:35" ]]
 then 

 
  if [ "$check" ] && [ "$check_cpu70" == "" ]
  then
 
  kill "$check_cpu5" "$check_cpu15" "$check_cpu20" "$check_cpu25" "$check_cpu30" "$check_cpu35" 2> /dev/null
  kill "$check_cpu40" "$check_cpu45" "$check_cpu50" "$check_cpu55" "$check_cpu60" "$check_cpu65" "$check_cpu75" 2> /dev/null

  fi
#

###

#
 elif [[ "$run_time" > "03:35" ]]
 then 


  if [ "$check" ] && [ "$check_cpu75" == "" ]
  then
 
  kill "$check_cpu5" "$check_cpu15" "$check_cpu20" "$check_cpu25" "$check_cpu30" "$check_cpu35" 2> /dev/null
  kill "$check_cpu40" "$check_cpu45" "$check_cpu50" "$check_cpu55" "$check_cpu60" "$check_cpu65" "$check_cpu70" 2> /dev/null

  fi
#

###

#

 fi
 
sleep 1

do
    :
done
