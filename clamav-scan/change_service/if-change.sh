#!/bin/bash

sleep 10

exc=$(echo "'|.cache|.mozilla|.local|.config|.gnupg|snap/\.|auto-clamIPS/VIRUS-FOUND/|'")

sudo -i inotifywait  -ecreate,move -m -r -q --format  '%Xe %w%f' --exclude $exc /home/ >> '/opt/auto-clamIPS/auto-clamav/logs/change.log'

