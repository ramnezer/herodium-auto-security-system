#!/bin/bash

#
sysctl fs.inotify.max_user_instances=8192
sysctl fs.inotify.max_user_watches=524288
#

#
### give high priority to the following processes
renice -10 -p $(pgrep -f  "/opt/auto-clamIPS/auto-clamav/if-change-scan.py") 2>  /dev/null
renice -10 -p $(pgrep -f  "/usr/sbin/clamd") 2> /dev/null
#

data=$(cat /opt/auto-clamIPS/auto-clamav/logs/data_scan.log)

inotifywait  -ecreate,attrib -m -r -q  --format  '%Xe %w%f' $data  >> '/opt/auto-clamIPS/auto-clamav/logs/change.log' /&
inotifywait  -emove,close_write -m -r -q  --format  '%Xe %w%f' $data  >> '/opt/auto-clamIPS/auto-clamav/logs/change_entangl.log'
