#!/bin/bash

sysctl fs.inotify.max_user_watches=524288

inotifywait  -ecreate,move,close_write -m -r -q  --format  '%Xe %w%f' /media/  >> '/opt/auto-clamIPS/auto-clamav/logs/change.log'


