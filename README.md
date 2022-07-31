
## auto-clamIPS-AntiMalware

auto-clamIPS is an automatic-integrated-protection-system against malware and malicious traffic

The purpose of this tool is to create auto-active-system 
against malware and malicious traffic for debian/ubuntu based distros.
The project was based on a combination of several other open
source projects (clamav,maltrail,apparmor) that will
be managed by scripts in bash,python and systemd to
create a one coordinated system.



Whereas in the past the use of antivirus on
Linux-based distributions was unnecessary.
after all,over the years the situation has
changed and today there are quite a few
threats on the network.

It's true that responsible
linux-users do not have to use antivirus,
but when it comes to less responsible and
less experienced users the situation
is of course different.

Project clamav together with other open
source projects
can give a strong and effective solution but
unfortunately for some users (even advanced)
the use of these programs can be difficult.

This tool wants to solve this problem by combining
between clamav,maltrail and apparmor managed 
by systemd,python and bash scripts to create a single
coordinated system against malicious activity.


#### For debian/ubuntu based distributions
#### like mint,popos,linux-lite,*mx-linux,kali-linux and similar distrio

*******************************************************
At this point, i do not recommend installing
the tool on ubuntu 22.04 based distributions !!
This is because it takes to canonical between half
a year to a year to stabilize new LTS distro.
*******************************************************



#### Before we start the installation ... 
#### Explanation of the program


### auto-clam-antivirus

to prevent unnecessary use of ram memory,the installation will
not install 'clamav-daemon',you can install clamav-daemon
manually if you want and use 'clamdscan' with your shell.

The program will then allow you to perform two types of scans,
each scan includes several scheduling options.
and a third option for real-time-scanner.


*******************************************************************************************************************************

1.

The first option is to perform a full scan of the entire system and
any device connected to it.this scan can take a very long time
and is therefore set as a default once a week.
but if you want you can change it.

every 12 hours

once a day

once a week(default)

once a month

*******************************************************************************************************************************

2.

A full scan of the system can take a very long time, so most users will prefer to perform it once a week.
to give you more security the program will allow you to perform a additional scan that will work in parallel with the main scan
(full scan) Specific to a home directory only which is considered more problematic.

By logic you will need to perform the scan at a lower timing than the full scan.
for example, if you run a full scan once a week, you will want to run a home-scan once a day or 12 hours.

You have 4 options:

every 6 hours

every 12 hours

once a day

once a week

*******************************************************************************************************************************

3.

#### real-time scanner 

To make the program more effective and identify risks immediately.
you have the option to enable real-time scanner for home (by default) or additional target directories.
The system will scan your home directory and all the directories inside her
on a regular basis every 15 seconds and if it detects a change such as
creating,downloading,copying,moving a file or directories with files
it will start scanning the only the specific files added or moved inside the home directory
in case malware is found the program will perform a full scan of home directory.

Note !

**************************************************************************************************
For obvious reasons the service will not listen to changes on Hidden directories that come inside
'home' such ".mozilla" ".cache" ".local"
In addition the scanner partially ignored from snap directory if it is installed,
he will allow only visible files to be scanned within the snap directory.
all other hidden folders and files inside home directory will be scanned
by real-time scanner 
**************************************************************************************************
To avoid duplicate scans while transferring large directories containing multiple files
the program will turn off the execution scanner but will continue to listen for new changes
and if there were new changes while performing the scan the program will perform another scan
after finishing the first.
**************************************************************************************************
#### The real-time scanner is not a substitute for scheduled scans !!!
it is surely not a substitute for the full scan but neither substitute for a home-scan-timer.
this is because if the real-time scanner is failed for any reason,you will be left without
protection of your home directory until the next full system scan,
and the second reason is because real-time scanning is not trying to detect and scan
changes in some of the hidden directories as I mentioned before.

#### all that real-time scanning gives you is an extra layer of protection but no more than that !

**************************************************************************************************
Earlier versions of ubuntu 22.04 come with a directory called "firefox.tmp"
In the downloads directory that creates a problem with real-time-scanner.
To fix this you need to update Firefox via snap.
The program will try to fix this automatically
and do so only on distributions which are
based on ubuntu 22.04 lts.

you can also do it manually

$ sudo snap refresh firefox

and then delete "firefox.tmp" if it exists in the download directory
***************************************************************************************************

Add or change a real-time-scan target directory


#### example for apache web server

go to /opt/auto-clamIPS/auto-clamav/if-change.sh

$ sudo nano /opt/auto-clamIPS/auto-clamav/if-change.sh

change the relevant part that appears in the line

from:
'%Xe %w%f' --exclude $exc /home/ >>

to: 
'%Xe %w%f' --exclude $exc /home/ /var/www/html/ >>


#### You should also change it for 'real-time-scaner-backup-scan'

go to /opt/auto-clamIPS/auto-clamav/clamav-scan-home2.sh

$ sudo nano /opt/auto-clamIPS/auto-clamav/clamav-scan-home2.sh

and change the line

from:
DIRTOSCAN="/home/"

to:
DIRTOSCAN="/home/ /var/www/html/"

#### save the file and reboot the system

***************************************************************************************************
***************************************************************************************************



#### logs files and messages

if the system detects malware
it will do the following steps. 

1.
send a log file with
list of results (only infected files)
to the desktop and root directory

2.
it will send 1 or 2 message by 'notify-send'



3.
the program will create a database of historical
log files(also empty ones)for all types of scans.

Located in: /opt/auto-clamIPS/auto-clamav/logs/logs_history/


Note!
******************************************************
Due to differences in structure between different
distributions,in some cases 'notify-send' may not work
but sending the log files to desktop should work
in any ub/de distribution.
******************************************************

*******************************************************************************************************************************

To ensure that the clamav-database is regularly updated,the system will
run a service that will perform a manual update for you automatically every 6 hours.
updates clamav-database on a daily basis are very small so they will
not interfere with network usage.

*******************************************************************************************************************************




### Option to experienced users only

#### auto-move-malwares with real-time-scaner for home(default) or target directory

If you want to make the detection system mor autonomous 
you have the option to automatically move threats 
with real-time-home-scaner to a special test directory
named 'virus-found'
Located in: /home/user_name/auto-clamMA-antivirus/VIRUS-FOUND/

Within this directory a zip file will be created that will include
all the infected files and will allow the user to make a selection
between the files.if you come to the conclusion that there is
nothing important in the zip file you can just delete it,
Deleting the zip will not have a negative effect on the program,
The program will create a new zip as soon as needed again.

To prevent unwanted loop of the detection system after
malware detection,the program will put the directory
'VIRUS-FOUND' in ignore mode.this ignore command 
will not include the scheduled scanners.


#### !!! Note !!!

auto-move-malwares will not include the regular schedulers
(full scan and home)for the reason that sometimes 'auto-move'
may be too aggressive.the real-time-scaner includes a backup scan
in case it fails or in case malware is found,the backup scan will
include the entire home directory and if you choose to enable
'auto-move' its settings will also be included in this scan !

#### !!! Warning !!!

If there are files in your home or target directory
that are compatible with windows that have undergone reverse
engineering with tools like wine to run on linux distro,the 
antivirus may identify them as a risk and in case you choose
to automatically move risks they might move to 'VIRUS-FOUND' directory

#### Use this option only if you know what you are doing !


********************************************************************************************************************************************
********************************************************************************************************************************************
********************************************************************************************************************************************



********************************************************************************************************************************************

### maltrail-auto-active



#### maltrail

Maltrail is a malicious traffic detection system, utilizing publicly
available (black)lists containing malicious and/or generally suspicious
trails, along with static trails compiled from various AV.

Although maltrail is a great tool it does not take active
action against malicious traffic.

This program will use maltrail sensors to detect network
traffic containing malwares(only malwares/malicious traffic)
and block it within a few seconds by iptables/ipset.


#### maltrail-notify-log

as soon as the system detects malicious traffic,it will send a
message by 'notify-send' until contact with the infected ip stop.
in addition the system will send to desktop a log file named 
"maltrail-found" contain a list of malicious IP.


********************************************************

To follow the black list use

$ sudo ipset list | cat -n

to move ipset list to log files

$ sudo ipset list | cat -n >> test.log
 

to check if specific address is blocked

$ sudo ipset list | grep -F 'ip-address'

To look at the tracking history of maltrail

go to:

$ cd /var/log/maltrail/ 


Note !
*******************************************************
After the first installation and first reboot of system
it will take a few minutes for maltrail to load and 
start active,and after that maltrail will load
within a few seconds after each reboot.
*******************************************************
Although the blocking of malicious addresses will be
done within a few seconds,the alert system will
continue to work until contact with the malicious
address or attacker stops.this is to give the users 
an indication that an attempted attack or unwanted
contact is still taking place.
*******************************************************

Maltrail server will be disabled by default
But if you want to use it you can enable it easily,
Visit the developer page for more details.

https://github.com/stamparm/maltrail

********************************************************************************************************************************************

#### if you chose to use maltrail-server 
#### Here is an explanation of how to change the password



To change the admin password, you need to generate a sha256 password by running the command below;

$ echo -n 'password' | sha256sum | cut -d " " -f 1

5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8


In this installation the maltrail.conf file is located in

/opt/maltrail/maltrail.conf

$ sudo nano /opt/maltrail/maltrail.conf

Where password is your password string. Next, copy the code and paste
it on the maltrail.conf, server section, USERS sub-section. For example,
if you were changing for the admin user,

USERS

    admin:5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8:0:                        # password
    admin:9ab3cd9d67bf49d01f6a2e33d0bd9bc804ddbe6ce1ff5d219c42624851db5dbc:0:                        # changeme!
    local:9ab3cd9d67bf49d01f6a2e33d0bd9bc804ddbe6ce1ff5d219c42624851db5dbc:1000:192.168.0.0/16       # changeme!


now you can run the maltrail-server with a service

running the command;

$ sudo cp /opt/maltrail/maltrail-server.service /etc/systemd/system/maltrail-server.service

$ sudo systemctl daemon-reload

$ sudo systemctl start maltrail-server.service

$ sudo systemctl enable maltrail-server.service

check if it is active;

$ systemctl status maltrail-server.service


now go to the developer page of maltrail 
in github to see how to login to the server
by your browser.

********************************************************************************************************************************************

If you have come to the conclusion that the amount of memory maltrail
takes(10% by default)is too large,you can change it.

go to 

/opt/maltrail/maltrail.conf

$ sudo nano /opt/maltrail/maltrail.conf

and change the line

'CAPTURE_BUFFER'

for example:

from:
CAPTURE_BUFFER 10%

to:
CAPTURE_BUFFER 5%

save the file

and restart the service 

$ sudo systemctl restart maltrail-sensor.service

or 

reboot your system

********************************************************************************************************************************************

********************************************************************************************************************************************



*********************************************************************

### zram-config

Use in Maltrail cost you up to '10%' of the RAM in your system,
to deal with this problem the installation will give you the 
option to use 'zram-config' which will optimize and
actually increase the dynamic memory in your system by '50%'
on default with ubuntu-based or '2250MB' by default on debian-based

*********************************************************************



*********************************************************************

### apparmor optimization

For advanced users there is the option to enable apparmor
in enforce mode and add a huge amount of profiles.
in this way increases the system security.
this option is not required for regular users,except for those
who need a high level of security.


A simple explanation for apparmor...

Apparmor is a security framework that prevents applications
from turning evil.For example:If I run Firefox and visit a
bad site that tries to install malware that will delete my
home folder,Apparmor has limits on Firefox though preventing
it from doing anything I don't want
(like accessing my music, documents, etc).
This way even if your application is
compromised, no harm can be done.


Note !
************************************************************
This option is for default kernel (Debian/Ubuntu) only.

This is because it is not recommended to run this option on
new versions of the vanilla-kernel without is being modified
by Debian/Ubuntu developers.
************************************************************

*********************************************************************



## install auto-clamIPS


Open a terminal and run the following commands

#### $ sudo apt-get update

#### $ sudo apt-get install git

Download the tool to home folder

#### $ git clone https://github.com/ramner98/auto-clamIPS.git

#### $ cd auto-clamIPS && chmod +x setup.sh && sudo ./setup.sh -yy

or

#### $ cd auto-clamIPS

#### $ chmod +x setup.sh

#### $ sudo ./setup.sh


### and follow the instructions




Note !
*************************************************************************

#### FOR MX-LINUX

If you intend to install the program on MX-LINUX
You will need to enable systemd manually
before you perform the installation.

go to grub

$ sudo nano /etc/default/grub

And change the line 

GRUB_CMDLINE_LINUX_DEFAULT=

from: 

GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"

to:

GRUB_CMDLINE_LINUX_DEFAULT="quiet splash init=lib/systemd/systemd"

and save the file

update grub:

$ sudo update-grub

now reboot your system and start the installation

If you have difficulty doing this from the terminal use this tutorial
https://daylifetips.com/enable-systemd-on-mx-linux/

*************************************************************************

********************************************************************************************************************************************


#### uninstall


1.Run the program and select "uninstall"
this option will remove most of the installation (not all of it) and try to backup to the existing state by timeshift. 

2.While installing clamIPS,the program will try to perform a backup using a 'timeshift' named
"auto-clamav-uninstall". You can select this option to return to the state you were in before installing the program.

#### Warning !

#### option '2' will return your entire system (all settings) to the state it was in before installation. 


#### Note !
**************************************************************************************************
The reason for using - 'timeshift'

1.
to Allow quick removal of the program in case you
regret shortly after installation.

2.
In case you want to enable apparmor in enforce mode,
and experience difficulties while using the system.

3.
It is always good that 'timeshift' is installed :-)

**************************************************************************************************

********************************************************************************************************************************************



### options


#### manage services 

********************************************************************************************************************************************

#### full-scan
$ sudo systemctl start/stop/enable/disable clamscan-root-week.timer

#### home scan
$ sudo systemctl start/stop/enable/disable clamscan-home-day.timer

#### real-time-home-scaner
$ sudo systemctl start/stop/enable/disable if-change-scan.timer

#### zram-config
$ sudo systemctl start/stop/enable/disable zram-config.service

#### auto-update-clamav
$ sudo systemctl start/stop/enable/disable auto-update-clamav.timer

#### maltrail
$ sudo systemctl start/stop/enable/disable maltrail-sensor.service

#### maltrail-auto-active
$ sudo systemctl start/stop/enable/disable maltrail_scan.timer

#### notify-clamMA
$ sudo systemctl start/stop/enable/disable notify-send.timer

#### Return apparmor to omplain mode
$ sudo aa-complain /etc/apparmor.d/*


********************************************************************************************************************************************

#### Use a ignore files list for clamscan

This means that the antivirus ignores files
that appear in the list if you need to do so
for some reason.

The text file is located in 

$ /opt/auto-clamIPS/auto-clamav/ignore_list.txt

You need to add this command before target

--exclude=

example of adding a file to a list:
****************************************
--exclude=/home/user/test/file_test.sh

--exclude=/usr/local/bin/file_test2.py
****************************************

Note !
*******************************************************
#### This ignore-list will work on all types of scans,
#### so be careful with it !

and if you chose to use the list..
perform from time to time a manual check to see
what is on the list and if it should be there,
it is important !

You can check the list easily with

$ cat -n /opt/auto-clamIPS/auto-clamav/ignore_list.txt

*******************************************************

******************************************************************************************************
******************************************************************************************************
******************************************************************************************************


#### Remember there is no protection system which is a substitute
#### for responsible use of the system and over the internet !!!

In addition

**************************************************************************************************
Perform manual scans by clamscan on a regular basis

$ clamscan -r -i /

**************************************************************************************************

Check history of 'auto-clam-scan' logs

Located in: /opt/auto-clamIPS/auto-clamav/logs/logs_history/

Check manually from time to time if clamav-database is updated

$ sudo systemctl stop clamav-freshclam && sudo freshclam && sudo systemctl start clamav-freshclam

**************************************************************************************************

Check ipset black list from time to time

$ sudo ipset list


If you want to clear the blacklists of ipset


use the commands

for ipv4:

$ sudo ipset flush blacklists 

for ipv6:

$ sudo ipset flush blacklists2 

go to '/etc/ipset.conf'

$ sudo nano /etc/ipset.conf

and remove the relevant addresses.

Note
************************************
by using this file you can also
remove specific addresses without
completely removing the list.
***********************************

save the files and reboot.


**************************************************************************************************

Make system updates on a weekly basis

$ sudo apt-get update && sudo apt-get upgrade -y

**************************************************************************************************

Try to get to know every software that appears in your
system and check what it does and what it is for.

Large and inflated distributions that will contain an
unnecessary amount of package and software
may increase the risk of security vulnerabilities,
#### in other words always try to build the distribution
#### in yourself and install and use only what you really need !

**************************************************************************************************

******************************************************************************************************



### Thanks to the amazing developers !

https://www.clamav.net/

https://github.com/stamparm/maltrail

https://gitlab.com/apparmor

https://github.com/ecdye/zram-config


#
#### done !
#


