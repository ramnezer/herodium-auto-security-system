#!/bin/bash
sudo -i perl -pi -e 'if($.==6){s/\n/\/.Xauthority"\n/g}if(eof){$.=0}' /etc/systemd/system/notify-send.service*
