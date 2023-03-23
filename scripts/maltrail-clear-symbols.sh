#!/bin/bash

# make sure that the value does not come with unnecessary symbols
# this command will be repeated several times to make sure the process was successful

seq 3 | xargs -I -- sudo sed -i -e 's/^"//' -i -e 's/"$//' -i -e 's/^(//' -i -e 's/)$//' /opt/auto-clamIPS/maltrail/logs/clean2.log

cat /opt/auto-clamIPS/maltrail/logs/clean2.log | tr -d '""()' >> /opt/auto-clamIPS/maltrail/logs/clean3.log
