#!/bin/bash


OPTIONS_FILE="options.conf"

SCRIPT_NAME="edit-options.sh"

###

if [[ $EUID -ne 0 ]]
then
	echo "you need to run the script with superuser (root) privileges."
	echo "try with: \"sudo ./${SCRIPT_NAME}\""
	exit 1
fi

nano /opt/auto-clamIPS/auto-clamav/options/${OPTIONS_FILE}

###

read -p "do you want to apply the new options now ? [y/N] " -n 1 -r
echo ''
if [[ $REPLY =~ ^[Yy]$ ]]
then

bash /opt/auto-clamIPS/auto-clamav/options/line-generator.sh

echo ''
echo 'update options done'
echo ''

else

echo ''
echo 'options update is denied'
echo ''

fi

exit 0
