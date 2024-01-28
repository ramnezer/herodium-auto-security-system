#!/bin/bash

sleep 10

/opt/auto-clamIPS/auto-clamav/change-li.sh /&
/opt/auto-clamIPS/auto-clamav/media_scan/media_if-change.sh /&
/opt/auto-clamIPS/auto-clamav/media_scan/check_media.sh /&
/opt/auto-clamIPS/auto-clamav/cpulimit-chack.sh /&
/opt/auto-clamIPS/auto-clamav/integral_cpulimit.sh
