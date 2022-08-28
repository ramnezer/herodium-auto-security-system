import subprocess
import time


###########################################
# Install timeshift and backup the system #
###########################################


def timeshift_commands():
    pro = subprocess.run(['sudo', 'apt-get', 'install', 'timeshift', '-y'])
    pro2 = subprocess.run(['sudo', 'timeshift', '--create',
                           '--comments', 'uninstall-auto-clam-antivirus'])
    print(pro.returncode)
    print(pro2.returncode)

    if int(pro.returncode + pro2.returncode)==0:
        print("############################################################")
        print("* Timeshift installation and system backup were successful *")
        print("############################################################")
        print("")
        print("the program will continue the installation process in a few seconds, please wait ...")
        time.sleep(3)
    else:
        print("#####################################################") 
        print("*          warning:system backup is failed          *")
        print("#####################################################")
        print("")
        time.sleep(3)
        print("#################################################################")
        print("Please check if the internet connection is available")
        print("Without installing this software and performing the backup you" )
        print("will not be able to uninstall the program and return to the state")
        print("you were in before the installation.")
        print("#################################################################")
        print("")
        loop = input("Do you want to try to Install timeshift and backup the system again? [y/n]") 
        if loop  == "y":
          subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
          timeshift_commands()


        else:
            
              print("##############################################################################") 
              print("*                       warning: backup system failed                        *")
              print("##############################################################################")
              time.sleep(3)
              print("")
        
              while input("Do you want to continue without backup system? [y/n]") == "n":
                exit ()
          

timeshift_commands()

##############################################################################################################################


###########################
#   auto-clam-antivirus   #
###########################

      
def clamav_install_commands():

    pro1 = subprocess.run(
        "sudo apt-get update && sudo apt-get upgrade -y", shell=True)
    
    pro2 = subprocess.run(
        ['sudo', 'mkdir', '-p', '/opt/auto-clamIPS/auto-clamav/'])
    
    pro3 = subprocess.run(
        ['sudo', 'mkdir', '-p', '/opt/auto-clamIPS/auto-clamav/logs/'])
    
    pro4 = subprocess.run(
        ['sudo', 'mkdir', '-p', '/opt/auto-clamIPS/auto-clamav/logs/logs_history/'])
    
    pro5 = subprocess.run(['sudo', 'apt-get', 'install', 'clamav', '-y'])
    
    pro7 = subprocess.run(
        ['sudo', 'cp', 'clamav-scan/clamav-root-scan.sh', '/opt/auto-clamIPS/auto-clamav/'])
    
    pro8 = subprocess.run(
        ['sudo', 'cp', 'clamav-scan/clamscan-root-month-week-Day-Hour-timer/clamscan-root.service', '/etc/systemd/system/'])
    
    pro9 = subprocess.run(
        ['sudo', 'cp', 'clamav-scan/clamscan-root-month-week-Day-Hour-timer/clamscan-root-week.timer', '/etc/systemd/system/'])
    
    pro10 = subprocess.run(['sudo', 'systemctl', 'daemon-reload'])
    
    pro11 = subprocess.run(
        ['sudo', 'systemctl', 'start', 'clamscan-root-week.timer'])
    
    pro12 = subprocess.run(
        ['sudo', 'systemctl', 'enable', 'clamscan-root-week.timer'])
    
    pro13 = subprocess.run(
        ['sudo', 'cp', 'clamav-scan/ignore_list.txt', '/opt/auto-clamIPS/auto-clamav/'])

    
    print(pro1.returncode)
    print(pro2.returncode)
    print(pro3.returncode)
    print(pro4.returncode)
    print(pro5.returncode)
    print(pro7.returncode)
    print(pro8.returncode)
    print(pro9.returncode)
    print(pro10.returncode)
    print(pro11.returncode)
    print(pro12.returncode)
    print(pro13.returncode)


    if int(pro1.returncode + pro2.returncode + pro3.returncode + pro4.returncode + pro5.returncode
    + pro7.returncode + pro8.returncode + pro9.returncode + pro10.returncode + pro11.returncode +
    pro12.returncode + pro13.returncode)==0:
        print("") 
        print("* Installing and update clamav was successful *")
        print("")
        print("")
        print("the program will continue the installation process in a few seconds, please wait ...")  
        time.sleep(3)

    else:

        print("") 
        print("* warning: Installing and update clamav finished with errors *")
        print("")
        time.sleep(3)
        print("")
        loop = input("Do you want to try to Installing and update clamav again ? [y/n]")  
        if loop  == "y":
         subprocess.run(['sudo', 'bash', 'scripts/fix.sh']) 
         clamav_install_commands() 


        else:
        
            print("") 
            print("* warning: Installing and update clamav was failed *")
            print("")
            time.sleep(3)
            print("")
    
clamav_install_commands()  


####################################################################################################################################


def root_scan_commands():    
 
 print("")
 print("")
 print("You can set 4 types of auto-full-scan for the entire system and each") 
 print("device connected to it.")
 print("the default is to perform a full scan once a week ")
 print("")
 print("Enter [1] clamscan all 12-hours")  
 print("Enter [2] clamscan once a day on 00:00:00")
 print("Enter [3] clamscan once a week on Sat 3:00:00 (default)")  
 print("Enter [4] clamscan once a month on /**/15/ 03:00:00") 


 retls = input("select an option: ")
 
 if retls  == "1":

        with open('/etc/systemd/system/clamscan-root-week.timer', 'r', encoding='utf-8') as file:
            data = file.readlines()
  
        print(data)
        data[4] = "OnCalendar=*-*-* 00,12:00:00 \n"
  
        with open('/etc/systemd/system/clamscan-root-week.timer', 'w', encoding='utf-8') as file:
         file.writelines(data)

 if retls  == "2":
        
        with open('/etc/systemd/system/clamscan-root-week.timer', 'r', encoding='utf-8') as file:
            data = file.readlines()
  
        print(data)
        data[4] = "OnCalendar=*-*-* 3:00:00 \n"
  
        with open('/etc/systemd/system/clamscan-root-week.timer', 'w', encoding='utf-8') as file:
         file.writelines(data)

 if retls  == "3":
        
        with open('/etc/systemd/system/clamscan-root-week.timer', 'r', encoding='utf-8') as file:
            data = file.readlines()
  
        print(data)
        data[4] = "OnCalendar=Sat 3:00:00 \n"
  
        with open('/etc/systemd/system/clamscan-root-week.timer', 'w', encoding='utf-8') as file:
         file.writelines(data)

 if retls  == "4":
        
        with open('/etc/systemd/system/clamscan-root-week.timer', 'r', encoding='utf-8') as file:
            data = file.readlines()
  
        print(data)
        data[4] = "OnCalendar=*-*-15 03:00:00 \n"
  
        with open('/etc/systemd/system/clamscan-root-week.timer', 'w', encoding='utf-8') as file:
         file.writelines(data)

 def update_timer():
  pro = subprocess.run(['sudo', 'systemctl', 'daemon-reload'])
  
  print(pro.returncode)

  if int(pro.returncode)==0:
        print("") 
        print("* enable root_scanner_timer was successful *")
        print("")
        print("")
        print("the program will continue the installation process in a few seconds, please wait ...")  
        time.sleep(3)
  else:

    print("")  
    print("enable root_scanner_timer was failed ")
    print("")

 update_timer()

root_scan_commands()

##############################################################################################################################


def home_scan():
 
 print("")
 print("")   
 print("A full scan of the system can take a very long time, so most users ") 
 print("will prefer to perform it once a week.")
 print("To give you more security the program will allow you to perform a ")
 print("scan to a home directory only which is considered more problematic.")
 print("")
 home_directory = input("Are you interested to running an automatic scan on your home directory ? [y/n] ")  
 if home_directory  == "y":   
  
  def timer2_commands():
    pro = subprocess.run(
        ['sudo', 'cp', 'clamav-scan/clamav-scan-home.sh', '/opt/auto-clamIPS/auto-clamav/'])
    
    pro2 = subprocess.run(
        ['sudo', 'cp', 'clamav-scan/clamscan-home-week-Day-Hour-timer/clamscan-home.service', '/etc/systemd/system/'])
    
    pro3 = subprocess.run(
        ['sudo', 'cp', 'clamav-scan/clamscan-home-week-Day-Hour-timer/clamscan-home-day.timer', '/etc/systemd/system/'])
    
    pro4 = subprocess.run(['sudo', 'systemctl', 'daemon-reload'])
    
    pro5 = subprocess.run(
        ['sudo', 'systemctl', 'start', 'clamscan-home-day.timer'])
    
    pro6 = subprocess.run(
        ['sudo', 'systemctl', 'enable', 'clamscan-home-day.timer'])

    print(pro.returncode)
    print(pro2.returncode)
    print(pro3.returncode)
    print(pro4.returncode)
    print(pro5.returncode)
    print(pro6.returncode)

    if int(pro.returncode + pro2.returncode + pro3.returncode + pro4.returncode + pro5.returncode + pro6.returncode)==0:  
     time.sleep(1)

    else:
    
     print("enable home directory scanner was filled' ")

     loop = input("Do you want to try to fix possible problems and try to install again? [y/n]")  
     if loop  == "y":
      subprocess.run(['sudo', 'bash', 'scripts/fix.sh']) 
      timer2_commands()
    
    print("")
    print("")
    print("By logic you will need to perform the scan at a lower ")
    print("timing than the full scan.")
    print("For example, if you run a full scan once a week, you will want to run")
    print("a home scan once a day or 12 hours.")
    print("")
    print("Enter [1] clamscan all 6-hours")  
    print("Enter [2] clamscan all 12-hours")
    print("Enter [3] clamscan once a day")  
    print("Enter [4] clamscan once a week") 

    retls = input("select an option: ")

    if retls  == "1":

        with open('/etc/systemd/system/clamscan-home-day.timer', 'r', encoding='utf-8') as file:
            data = file.readlines()

        print(data)
        data[4] = "OnCalendar=*-*-* 00,06,12,18:00:00 \n"

        with open('/etc/systemd/system/clamscan-home-day.timer', 'w', encoding='utf-8') as file:
            file.writelines(data)

    if retls  == "2":
        
        with open('/etc/systemd/system/clamscan-home-day.timer', 'r', encoding='utf-8') as file:
            data = file.readlines()

        print(data)
        data[4] = "OnCalendar=*-*-* 00,12:00:00 \n"

        with open('/etc/systemd/system/clamscan-home-day.timer', 'w', encoding='utf-8') as file:
            file.writelines(data)

    if retls  == "3":
        
        with open('/etc/systemd/system/clamscan-home-day.timer', 'r', encoding='utf-8') as file:
            data = file.readlines()

        print(data)
        data[4] = "OnCalendar=*-*-* 00:00:00 \n"

        with open('/etc/systemd/system/clamscan-home-day.timer', 'w', encoding='utf-8') as file:
            file.writelines(data)

    if retls  == "4":
        
        with open('/etc/systemd/system/clamscan-home-day.timer', 'r', encoding='utf-8') as file:
            data = file.readlines()

        print(data)
        data[4] = "OnCalendar=Sat 3:00:00 \n"

        with open('/etc/systemd/system/clamscan-home-day.timer', 'w', encoding='utf-8') as file:
            file.writelines(data)

  timer2_commands()


  def update2_timer():
    pro = subprocess.run(['sudo', 'systemctl', 'daemon-reload'])

    print(pro.returncode)

    if int(pro.returncode)==0:
     print("") 
     print("* enable home directory scanner was successful *")
     print("")
     print("")
     print("the program will continue the installation process in a few seconds, please wait ...")  
     time.sleep(3)
   
    else:

     print("enable home directory scanner was failed ")

  update2_timer()

home_scan()  


##################################################################################################################################


#################
#   Real-time   #
#################


def real_time():

 def if_change():

  print("")  
  print("")   
  print("To make the program more effective and identify risks immediately.") 
  print("You have the option to enable automatic scan of changes.")
  print("The system will scan your home directory and all the directories inside her")
  print("on a regular basis and if it detects a change such as")
  print("creating,downloading,copying,moving a file or directories with files it will start")
  print("scanning the only the specific files added or moved inside the home directory")
  print("in case malware is found the program will perform a full scan of home directory.")
  print("")

  change = input("Are you interested to enable a real-time-home-scanner ? [y/n] ")  
  if change  == "y":

    pro = subprocess.run(['sudo', 'apt-get', 'install', 'inotify-tools', '-y'])
    
    pro2 = subprocess.run(
        ['sudo', 'cp', 'clamav-scan/change_service/if-change.sh', '/opt/auto-clamIPS/auto-clamav/'])
    
    pro3 = subprocess.run(
        ['sudo', 'cp', 'clamav-scan/change_service/if-change-scan.py', '/opt/auto-clamIPS/auto-clamav/'])
    
    pro4 = subprocess.run(
        ['sudo', 'cp', 'clamav-scan/change_service/clamav-scan-if.sh', '/opt/auto-clamIPS/auto-clamav/'])
    
    pro5 = subprocess.run(
        ['sudo', 'cp', 'clamav-scan/change_service/clamav-scan-if2.sh', '/opt/auto-clamIPS/auto-clamav/'])
    
    pro6 = subprocess.run(
        ['sudo', 'cp', 'clamav-scan/change_service/clamav-scan-home2.sh', '/opt/auto-clamIPS/auto-clamav/'])
    
    pro7 = subprocess.run(
        ['sudo', 'cp', 'clamav-scan/change_service/if-change.service', '/etc/systemd/system/'])
    
    pro8 = subprocess.run(
        ['sudo', 'cp', 'clamav-scan/change_service/if-change.timer', '/etc/systemd/system/'])
    
    pro9 = subprocess.run(
        ['sudo', 'cp', 'clamav-scan/change_service/if-change-scan.service', '/etc/systemd/system/'])
    
    pro10 = subprocess.run(
        ['sudo', 'cp', 'clamav-scan/change_service/if-change-scan.timer', '/etc/systemd/system/'])
    
    pro11 = subprocess.run(['sudo', 'systemctl', 'daemon-reload'])
    pro12 = subprocess.run(['sudo', 'systemctl', 'start', 'if-change.timer'])
    pro13 = subprocess.run(['sudo', 'systemctl', 'enable', 'if-change.timer'])
    
    pro14 = subprocess.run(
        ['sudo', 'systemctl', 'enable', 'if-change-scan.timer'])

#### make sure 'engrampa' is installed,it is not critical but it is better to have it installed
    pro16 = subprocess.run(['sudo', 'apt-get', 'install', 'engrampa', '-y'])
    
    print(pro.returncode)
    print(pro2.returncode)
    print(pro3.returncode)
    print(pro4.returncode)
    print(pro5.returncode)
    print(pro6.returncode)
    print(pro7.returncode)
    print(pro8.returncode)
    print(pro9.returncode)
    print(pro10.returncode)
    print(pro11.returncode)
    print(pro12.returncode)
    print(pro13.returncode)
    print(pro14.returncode)


    if int(pro.returncode + pro2.returncode + pro3.returncode + pro4.returncode + pro5.returncode + pro6.returncode + 
    pro7.returncode + pro8.returncode + pro9.returncode + pro10.returncode + pro11.returncode + pro12.returncode
    + pro13.returncode + pro14.returncode)==0:
     print("") 
     print("enable 'if_change' and timers && scripts was successful")
     print("")
     print("the program will continue the installation process in a few seconds, please wait ...")  
     time.sleep(3)

    else:

     print("") 
     print("*warning: enable if_change and timers && scripts was failed*")
     print("")
     time.sleep(3)
     print("")
     loop = input("Do you want to try to fix the problem and try again ? [y/n]")  
     if loop  == "y":
      subprocess.run(['sudo', 'bash', 'scripts/fix.sh']) 
      if_change() 

 if_change()


##################
#  move_malware  #
##################


 def auto_move_malwares():
  

  ####### if-change.timer

  pro3 = subprocess.run(['sudo', 'systemctl', 'status', 'if-change.timer'], capture_output=True)
      
  print(pro3.stdout)

  if int(pro3.returncode)==0:


   print("") 
   print("") 
   print("!!! This option is intended for professional or experienced users only !!!")
   print("")
   print("")
   print("To make the detection system mor autonomous") 
   print("You have the option to automatically move threats")
   print("with real-time-home-scanner to a special directory")
   print("named 'virus-found'")
   print("Located in:  /home/$(users)/auto-clamIPS/VIRUS-FOUND/")
   print("within this directory a zip file will be created that will")
   print("include all the infected files,it will allow the user to")
   print("make a selection between the files.")
   print("")
   print("")
   print("!!! Note !!!")
   print("")
   print("This option will not include the regular schedulers(full scan and home)")
   print("for the reason that sometimes 'auto-move' may be too aggressive")
   print("The real-time scan includes a backup scan in case it fails or in case")
   print("malware is found,the backup scan will include the entire home directory")
   print("and the 'auto-move' settings will also be included in this scan ! ")
   print("")
   print("")
   print("!!! Warning !!!")
   print("")
   print("If there are files in your home directory that are compatible with windows")
   print("that have undergone reverse engineering with tools like")
   print("wine to run on linux distro,the antivirus may identify them as a risk")
   print("and in case you choose to automatically move risks")
   print("They might move to the target directory")
   print("")
   print("Use this option only if you know what you are doing !")
   print("")




   auto_move = input("Are you interested to enable automatically-move-threats together with real-time-home-scaner ? [y/n] ")  
   if auto_move  == "y":


  #######

          with open('/opt/auto-clamIPS/auto-clamav/clamav-scan-if.sh', 'r', encoding='utf-8') as file:
           data = file.readlines()

          print(data)
          data[11] = 'clamscan --infected --recursive --exclude=/home/$user/auto-clamIPS/VIRUS-FOUND/ --exclude=/home/$user/Desktop/clamav-found-malware-$(date +"%Y-%m-%d").log $exclude --move=/home/$user/auto-clamIPS/VIRUS-FOUND/ --file-list="/opt/auto-clamIPS/auto-clamav/logs/auto.log" >> "$LOGFILE" \n'

          with open('/opt/auto-clamIPS/auto-clamav/clamav-scan-if.sh', 'w', encoding='utf-8') as file:
           file.writelines(data) 

          time.sleep(1)

  #######

          with open('/opt/auto-clamIPS/auto-clamav/clamav-scan-home2.sh', 'r', encoding='utf-8') as file:
           data = file.readlines()

          print(data)
          data[15] = 'clamscan --infected --recursive --exclude=/home/$user/auto-clamIPS/VIRUS-FOUND/ --exclude=/home/$user/.local/share/Trash/files/ --exclude=/home/$user/Desktop/clamav-found-malware-$(date +"%Y-%m-%d").log $exclude --move=/home/$user/auto-clamIPS/VIRUS-FOUND/ "$S" >> "$LOGFILE" \n'

          with open('/opt/auto-clamIPS/auto-clamav/clamav-scan-home2.sh', 'w', encoding='utf-8') as file:
           file.writelines(data) 

          time.sleep(1)


 auto_move_malwares()

real_time()

################################################################################################################################

### to prevent bugs during installation the service will be temporarily stopped until the system reboot
subprocess.run(['sudo', 'systemctl', 'stop', 'if-change.timer'], capture_output=True)


###########################
#  installing zram-config  #
###########################


def zram_commands():
 
 print("")
 print("")
 print("Use in maltrail cost you '10%' of the RAM in your system,") 
 print("to deal with this problem the program will give you the")
 print("option to 'install zram-config' which will optimize and")  
 print("actually increase the dynamic memory in your system by '50%'")
 print("on default with ubuntu-based or '2250MB' by default on debian-based")
 print("")

 zram = input("Are you interested to install zram-config ? [y/n] ")  
 if zram  == "y": 

  def zram_ubuntu_debian():

### for ubuntu based distros
   pro = subprocess.run('cat /proc/version | grep Ubuntu' ,capture_output=True ,shell=True)
   print(pro.stdout)
   if int(pro.returncode)==0:

    pro1 = subprocess.run(['sudo', 'apt-get', 'install', 'zram-config'])
    print(pro1.returncode)
    if int(pro1.returncode)==0:    
     print("") 
     print("* Installation zram-config was successful *")
     print("")
     print("")
     print("the program will continue the installation process in a few seconds, please wait ...")
     time.sleep(3)

    else:
 
      print("") 
      print("*warning: Installation zram-config was failed*")
      print("")
      time.sleep(3)
      print("")
      print("")
      loop = input("Do you want to try to install zram-config again? [y/n]")  
      if loop  == "y":
       subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
       zram_ubuntu_debian()   

    
### for debian based distros
   pro2 = subprocess.run('cat /proc/version | grep Debian',
                         capture_output=True, shell=True)
   print(pro2.stdout)
   if int(pro2.returncode) == 0:

    pro3 = subprocess.run("sudo rm -fr zram-config", shell=True)
    
    pro4 = subprocess.run(
        ['sudo', 'git', 'clone', 'https://github.com/ecdye/zram-config'])
    
    pro5 = subprocess.run("sudo cp -r zram-config /etc/", shell=True)
    pro6 = subprocess.run(['sudo', 'bash', '/etc/zram-config/install.bash'])
    pro7 = subprocess.run(['sudo', 'cp', 'debian/ztab', '/etc/ztab'])


    print(pro3.returncode)
    print(pro4.returncode)
    print(pro5.returncode)
    print(pro7.returncode)


    if int(pro3.returncode + pro4.returncode + pro5.returncode + pro7.returncode)==0:    
     print("") 
     print("*** Installation zram-config was successful ***")
     print("")
     print("")
     print("the program will continue the installation process in a few seconds, please wait ...")
     time.sleep(3)

    else:

      print("") 
      print("*warning: Installation zram-config was failed*")
      print("")
      time.sleep(3)
      print("")
      print("")
      loop = input("Do you want to try to install zram-config again? [y/n]")  
      if loop  == "y":
       subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
       zram_ubuntu_debian()   

  zram_ubuntu_debian()

zram_commands()    


#####################################################################################################################################


###  An initial database update is performed immediately,and after that the
###  System verify that the clamav database has been updated every 6 hours

def auto_update_clamav():
     
 pro = subprocess.run(['sudo', 'systemctl', 'stop', 'clamav-freshclam'])
 time.sleep(3)
 
 pro2 = subprocess.run(['sudo', 'freshclam'])
 time.sleep(3)
 
 pro3 = subprocess.run(['sudo', 'systemctl', 'start', 'clamav-freshclam'])
 
 pro4 = subprocess.run(
     ['sudo', 'cp', 'clamav-scan/auto_update_clamav/auto-update-clamav.py', '/opt/auto-clamIPS/auto-clamav/'])
 pro5 = subprocess.run(
     ['sudo', 'cp', 'clamav-scan/auto_update_clamav/auto-update-clamav.service', '/etc/systemd/system/'])
 pro6 = subprocess.run(
     ['sudo', 'cp', 'clamav-scan/auto_update_clamav/auto-update-clamav.timer', '/etc/systemd/system/'])

 pro7 = subprocess.run(['sudo', 'systemctl', 'daemon-reload'])
 
 pro8 = subprocess.run(
     ['sudo', 'systemctl', 'start', 'auto-update-clamav.timer'])
 pro9 = subprocess.run(
     ['sudo', 'systemctl', 'enable', 'auto-update-clamav.timer'])
 pro10 = subprocess.run(
     ['sudo', 'cp', '-r', 'scripts/freshclam_fix', '/opt/auto-clamIPS/auto-clamav/'])

 print(pro.returncode)
 print(pro2.returncode)
 print(pro3.returncode)
 print(pro4.returncode)
 print(pro5.returncode)
 print(pro6.returncode)
 print(pro7.returncode)
 print(pro8.returncode)
 print(pro9.returncode)
 print(pro10.returncode)

 if int(pro.returncode + pro2.returncode + pro3.returncode + pro4.returncode +
 pro5.returncode + pro6.returncode + pro7.returncode + pro8.returncode + pro9.returncode + pro10.returncode)==0:
  
  print("")
  print("*** enable auto_update_clamav was successful ***")
  print("")
  time.sleep(3)
 else:
  print("")   
  print("")   
  print("*** enable auto_update_clamav was filled ***")
  print("")
  print("")
  time.sleep(3)

  loop = input("Do you want to try to fix possible problems and try enable auto_update_clamav again? [y/n]")  
  if loop  == "y":
   subprocess.run(['sudo', 'bash', 'scripts/fix.sh']) 
   auto_update_clamav()

  else:

      print("")      
      print("") 
      print("*warning: enable auto_update_clamav was filled*")
      print("")
      print("")
      time.sleep(3)
      print("")
        
      while input("Do you want to continue without enable auto_update_clamav? [y/n]") == "n":
       exit ()

auto_update_clamav()


def freshclam_fix():

### check for update error and fix if is necessary

 pro = subprocess.run(
     ['sudo', 'bash', 'clamav-scan/auto_update_clamav/freshclam_fix.sh'])
 check_error = subprocess.run(
     "grep -E '429|403' clamav-scan/auto_update_clamav/freshclam_error.log", capture_output=True, shell=True)
 print(check_error.stdout)

 if int(check_error.returncode)==0:       
     print("")
     print("Failed to update clamav database")
     print("'ERROR type FreshClam previously received error code 429 or 403'")
     print("")
     print("This bug usually occurs when you use a vpn-proxy , slow network")
     print("or perform too many updates in a short period of time.")
     print("")
     print("The program will try to fix it but before that try to use a regular")
     print("internet service or use a different IP address.")
     print("")
     print("In any case, do not start using the auto-clamav without")
     print("updating your database !")
     print("")
     print("You can try to do this manually at another time")
     print("by using fix script")
     print(" [cd /opt/auto-clamIPS/auto-clamav/freshclam_fix && sudo python3 freshclam_fix.py] ")   
     print("")
     print("")
     loop = input("Do you want to try to fix the problem right now ? [y/n] ")
     if loop  == "y":
      subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
      print("")
      print("Please wait it may take some time ...")
      print("")
      subprocess.run(
          'sudo rm -f  "/var/lib/clamav/bytecode.cvd" "/var/lib/clamav/daily.cld" "/var/lib/clamav/freshclam.dat" "/var/lib/clamav/main.cvd"', shell=True)
      subprocess.run(
          'sudo systemctl stop clamav-freshclam && sudo freshclam && sudo systemctl start clamav-freshclam', shell=True)
      freshclam_fix()

freshclam_fix()


#####################################################################################################################################



########################
#   install maltrail   #
########################


def maltrail_commands():
  
  print("")
  print("")
  print("Maltrail is a malicious traffic detection system") 
  print("This program will use maltrail sensors to detect")
  print("network traffic containing malwares(only malwares/malicious)")  
  print("and block it using iptables/ipset.")
  print("")
  print("")

  maltrail = input("Are you interested to install and enable maltrail-real-time-protection ? [y/n] ")  
  if maltrail  == "y":
    
    def maltrail_install():

     pro1 = subprocess.run(['sudo', 'apt-get', 'install', 'git', 'python3', 'python3-dev', 'python3-pip',
                            'python-is-python3', 'libpcap-dev', 'build-essential', 'procps', 'schedtool', '-y'])
     
     pro2 = subprocess.run(
         ['sudo', 'apt-get', 'install', 'python3-pcapy', '-y'])
     
     pro3 = subprocess.run("sudo rm -fr '/opt/maltrail'", shell=True)
     
     pro4 = subprocess.run(
         'cd /opt/ && sudo git clone --depth 1 https://github.com/stamparm/maltrail.git', shell=True)
     
     pro5 = subprocess.run(
         "sudo chown -R $USER:$USER /opt/maltrail", shell=True)

     pro6 = subprocess.run(['sudo', 'mkdir', '-p', '/var/log/maltrail'])
     
     pro7 = subprocess.run(['sudo', 'mkdir', '-p', '/etc/maltrail'])
     
     pro8 = subprocess.run(
         ['sudo', 'cp', '/opt/maltrail/maltrail.conf', '/etc/maltrail'])
     
     pro9 = subprocess.run(['sudo', 'cp', '/opt/maltrail/maltrail-sensor.service',
                            '/etc/systemd/system/maltrail-sensor.service'])
     
     pro10 = subprocess.run(['sudo', 'systemctl', 'daemon-reload'])
     
     pro11 = subprocess.run(
         ['sudo', 'systemctl', 'start', 'maltrail-sensor.service'])
     
     pro12 = subprocess.run(
         ['sudo', 'systemctl', 'enable', 'maltrail-sensor.service'])
     
  
     print(pro1.returncode)
     print(pro2.returncode)
     print(pro3.returncode)
     print(pro4.returncode)
     print(pro5.returncode)
     print(pro6.returncode)
     print(pro7.returncode)
     print(pro8.returncode)
     print(pro9.returncode)
     print(pro10.returncode)
     print(pro11.returncode)
     print(pro12.returncode)


     if int(pro1.returncode + pro2.returncode + pro3.returncode + pro4.returncode + pro5.returncode + pro6.returncode
     + pro7.returncode + pro8.returncode + pro9.returncode + pro10.returncode + pro11.returncode +
     pro12.returncode)==0:
      print("") 
      print("* Installing maltrail was successful *")
      print("")
      print("")
      print("the program will continue the installation process in a few seconds, please wait ...")  
      time.sleep(3)

     else:

      print("") 
      print("* warning: Installation ended with errors *")
      print("")
      time.sleep(3)
      print("")
      loop = input("Do you want to try to Installing maltrail again and fix the errors ? [y/n]")  
      if loop  == "y":
        subprocess.run(['sudo', 'bash', 'scripts/fix.sh']) 
        maltrail_install() 

      else:

        print("") 
        print("* warning: Installing maltrail was failed *")
        print("")
        time.sleep(3)
        print("")
    
    maltrail_install()

### maltrail-auto-active-sensors 

    def ClamMaltrail_enable():
     
     pro = subprocess.run(
         ['sudo', 'apt-get', 'install', 'ipset', 'iptables', '-y'])
     
     pro1 = subprocess.run(
         ['sudo', 'mkdir', '-p', '/opt/auto-clamIPS/maltrail/logs/'])
     
     pro2 = subprocess.run(
         ['sudo', 'cp', 'maltrail/blacklist.sh', '/opt/auto-clamIPS/maltrail/'])
     
     pro3 = subprocess.run(
         ['sudo', 'cp', 'maltrail/listener_maltrail.sh', '/opt/auto-clamIPS/maltrail/'])
     
     pro4 = subprocess.run(
         ['sudo', 'cp', 'maltrail/maltrail_scan.py', '/opt/auto-clamIPS/maltrail/'])
     
     pro5 = subprocess.run(
         ['sudo', 'cp', 'maltrail/maltrail-services/listener_maltrail.service', '/etc/systemd/system/'])
     
     pro6 = subprocess.run(
         ['sudo', 'cp', 'maltrail/maltrail-services/listener_maltrail.timer', '/etc/systemd/system/'])
     
     pro7 = subprocess.run(
         ['sudo', 'cp', 'maltrail/maltrail-services/maltrail_scan.service', '/etc/systemd/system/'])
     
     pro8 = subprocess.run(
         ['sudo', 'cp', 'maltrail/maltrail-services/maltrail_scan.timer', '/etc/systemd/system/'])
     
     pro9 = subprocess.run(['sudo', 'systemctl', 'daemon-reload'])
     
     pro10 = subprocess.run(
         ['sudo', 'systemctl', 'start', 'listener_maltrail.service'])
     
     pro11 = subprocess.run(
         ['sudo', 'systemctl', 'enable', 'listener_maltrail.timer'])
     
     pro12 = subprocess.run(
         ['sudo', 'systemctl', 'start', 'maltrail_scan.service'])
     
     pro13 = subprocess.run(
         ['sudo', 'systemctl', 'enable', 'maltrail_scan.timer'])
     
     pro14 = subprocess.run(
         'sudo ipset create blacklists hash:ip timeout 0 maxelem 150000', shell=True)
     
     pro15 = subprocess.run(
         'sudo ipset create blacklists2 hash:ip timeout 0 family inet6 maxelem 150000', shell=True)
     
     pro16 = subprocess.run(
         'sudo iptables -C INPUT  -m set  --match-set blacklists  src -j DROP 2> /dev/null || sudo iptables -I INPUT 1  -m set  --match-set blacklists src -j  DROP 2> /dev/null', shell=True)
     
     pro17 = subprocess.run(
         'sudo ip6tables -C INPUT  -m set  --match-set blacklists2  src -j DROP 2> /dev/null || sudo ip6tables -I INPUT 1  -m set  --match-set blacklists2 src -j DROP 2> /dev/null', shell=True)
     
     pro18 = subprocess.run('sudo -i ipset save blacklists > /etc/ipset_maltrail.conf', shell=True)
     pro19 = subprocess.run('sudo -i ipset save blacklists2 > /etc/ipset_maltrail2.conf', shell=True)

### ipset optimization
     pro20 = subprocess.run(['sudo', 'apt-get', 'install', 'iprange', 'libcorkipset-utils',
                             'libcorkipset1', 'libipset-dev', 'libipset13', '-y'])

     print(pro1.returncode)
     print(pro2.returncode)
     print(pro3.returncode)
     print(pro4.returncode)
     print(pro5.returncode)
     print(pro6.returncode)
     print(pro7.returncode)
     print(pro8.returncode)
     print(pro9.returncode)
     print(pro10.returncode)
     print(pro11.returncode)
     print(pro12.returncode)
     print(pro13.returncode)


     if int(pro1.returncode + pro2.returncode + pro3.returncode + pro4.returncode + pro5.returncode + pro6.returncode + 
     pro7.returncode + pro8.returncode + pro9.returncode + pro10.returncode + pro11.returncode + pro12.returncode
     + pro13.returncode)==0:
      print("") 
      print("enable maltrail-active-sensors services was successful")
      print("")
      print("the program will continue the installation process in a few seconds, please wait ...")  
      time.sleep(3)

     else:

      print("") 
      print("*enable maltrail-active-sensors services was failed*")
      print("")
      time.sleep(3)
      print("")
      loop = input("Do you want to try to fix the problem and try again ? [y/n]")  
      if loop  == "y":
        subprocess.run(['sudo', 'bash', 'scripts/fix.sh']) 
        ClamMaltrail_enable()
    
    ClamMaltrail_enable()


### Automatic blacklist cleaning

    def flush_blacklists():
     
     print("")
     print("")
     print("IP addresses that are considered malicious today can")
     print("become legitimate again after a certain period of time.")
     print("")
     print("The program will allow you two options ")
     print("for automatically cleaning the block list.")
     print("once a week or once a month")
     print("")
     print("If the addresses remain malicious, they will be returned")
     print("to the list automatically if the maltrail sensors detect")
     print("them again.")
     print("")
     print("")



     blacklists = input("Are you interested to enable automatic blacklist cleaning for maltrail-blocker ? [y/n] ")  
     if blacklists  == "y":
      
      pro = subprocess.run(['sudo', 'cp', 'maltrail/flush_blacklists.sh', '/opt/auto-clamIPS/maltrail/'])

      pro1 = subprocess.run(
        ['sudo', 'cp', 'maltrail/maltrail-services/flush_blacklists.timer', '/etc/systemd/system/'])

      pro2 = subprocess.run(
        ['sudo', 'cp', 'maltrail/maltrail-services/flush_blacklists.service', '/etc/systemd/system/'])  
    

      print("")
      print("")  
      print("Enter [1] clean once a week(default)")  
      print("Enter [2] clean once a month on /**/15/ 02:00:00")
      print("")
      print("")

      retls = input("select an option: ")

      if retls  == "1":

        with open('/etc/systemd/system/flush_blacklists.timer', 'r', encoding='utf-8') as file:
            data = file.readlines()

        print(data)
        data[4] = "OnCalendar=Sat 2:00:00 \n"

        with open('/etc/systemd/system/flush_blacklists.timer', 'w', encoding='utf-8') as file:
            file.writelines(data)

      if retls  == "2":
        
        with open('/etc/systemd/system/flush_blacklists.timer', 'r', encoding='utf-8') as file:
            data = file.readlines()

        print(data)
        data[4] = "OnCalendar=*-*-15 02:00:00 \n"

        with open('/etc/systemd/system/flush_blacklists.timer', 'w', encoding='utf-8') as file:
            file.writelines(data)

      pro3 = subprocess.run(['sudo', 'systemctl', 'daemon-reload'])
     
      pro4 = subprocess.run(
         ['sudo', 'systemctl', 'start', 'flush_blacklists.timer'])
     
      pro5 = subprocess.run(
         ['sudo', 'systemctl', 'enable', 'flush_blacklists.timer'])

      print(pro.returncode)
      print(pro1.returncode)
      print(pro2.returncode)
      print(pro3.returncode)
      print(pro4.returncode)
      print(pro5.returncode)

      if int(pro1.returncode + pro2.returncode + pro3.returncode + pro4.returncode + pro5.returncode)==0:
       print("") 
       print("enable automatic-blacklist-cleaning services was successful")
       print("")
       print("the program will continue the installation process in a few seconds, please wait ...")  
       time.sleep(3)

      else:

       print("") 
       print("*enable automatic-blacklist-cleaning services was was failed*")
       print("")
       time.sleep(3)
       print("")
       loop = input("Do you want to try to fix the problem and try again ? [y/n]")  
       if loop  == "y":
        subprocess.run(['sudo', 'bash', 'scripts/fix.sh']) 
        flush_blacklists() 

       else:

        print("") 
        print("* warning: enable automatic-blacklist-cleaning services was was failed *")
        print("")
        time.sleep(3)
        print("")


    flush_blacklists()


maltrail_commands()


#####################################################################################################################################


#################
# enable_notify #
#################


def enable_notify():

 pro1 = subprocess.run(
     ['sudo', 'mkdir', '-p', '/opt/auto-clamIPS/notify-clamMA/logs/'])
 
 pro2 = subprocess.run(
     ['sudo', 'cp', 'notify-send/notify-send.py', '/opt/auto-clamIPS/notify-clamMA/'])
 
 pro3 = subprocess.run(
     ['sudo', 'cp', 'notify-send/notify-reset-boot.py', '/opt/auto-clamIPS/notify-clamMA/'])
 
 pro4 = subprocess.run(
     ['sudo', 'cp', 'scripts/notify_send.sh', '/opt/auto-clamIPS/notify-clamMA/'])
 
 pro5 = subprocess.run(['sudo', 'cp', '-r', 'notify-send/notify-media/',
                        '/opt/auto-clamIPS/notify-clamMA/notify-media/'])
 
 pro6 = subprocess.run(
     ['sudo', 'cp', 'notify-send/notify-services/notify-send.service', '/etc/systemd/system/'])
 
 pro7 = subprocess.run(
     ['sudo', 'cp', 'notify-send/notify-services/notify-send.timer', '/etc/systemd/system/'])

###

#### Add notify-send.service to user environment ####

 check_user = subprocess.run("echo $(users) | cut -d ' ' -f 1" ,capture_output=True ,shell=True)
 print(check_user.stdout.decode())

  
 with open('/etc/systemd/system/notify-send.service', 'r', encoding='utf-8') as file:
    data = file.readlines()

 print(data)
 data[5] = str('Environment="DISPLAY=:0" "XAUTHORITY=/home/') + (check_user.stdout.decode())
 
 with open('/etc/systemd/system/notify-send.service', 'w', encoding='utf-8') as file:
    file.writelines(data)

 subprocess.run(['sudo', 'bash', '/opt/auto-clamIPS/notify-clamMA/notify_send.sh'])

###

 pro10 = subprocess.run(['sudo', 'systemctl', 'daemon-reload'])
 pro11 = subprocess.run(['sudo', 'systemctl', 'start', 'notify-send.service'])
 pro12 = subprocess.run(['sudo', 'systemctl', 'enable', 'notify-send.timer'])  


 print(pro1.returncode)
 print(pro2.returncode)
 print(pro3.returncode)
 print(pro4.returncode)
 print(pro5.returncode)
 print(pro6.returncode)
 print(pro7.returncode)
 print(pro10.returncode)
 print(pro11.returncode)
 print(pro12.returncode)


 if int(pro1.returncode + pro2.returncode + pro3.returncode + pro4.returncode + pro5.returncode + pro6.returncode + 
 pro7.returncode + pro10.returncode + pro11.returncode + pro12.returncode)==0:
  
  print("") 
  print("*enable notify services was successful*")
  print("")
  print("the program will continue the installation process in a few seconds, please wait ...")  
  time.sleep(3)

 else:

  print("") 
  print("*enable notify services was failed*")
  print("")
  time.sleep(3)
  print("")
  loop = input("Do you want to try to fix the problem and try again ? [y/n]")  
  if loop  == "y":
   subprocess.run(['sudo', 'bash', 'scripts/fix.sh']) 
   enable_notify

enable_notify() 


#####################################################################################################################################


def fix_firefox_u22():

### fix tmp error for ubuntu 22.04 LTS only
 
 pro = subprocess.run("cat /etc/os-release | grep -F 'Ubuntu 22.04' " ,capture_output=True ,shell=True)
 print(pro.stdout)
 if int(pro.returncode)==0:
  
### check if snapd is install and update if this is true 

  pro1 = subprocess.run("snap list | grep -F 'snapd' " ,capture_output=True ,shell=True)
  print(pro1.stdout)
  if int(pro1.returncode)==0:

    pro2 = subprocess.run(['sudo', 'snap', 'refresh', 'firefox'])
    print(pro2.returncode)
    if int(pro2.returncode)==0:    
     print("") 
     print("* Updated/fix firefox-snap successfully *")
     print("")
     print("")
     print("the program will continue the installation process in a few seconds, please wait ...")
     time.sleep(3)

fix_firefox_u22() 


#########################################################################################################################################


def crowdsec_install():

 print("")
 print("")   
 print("Option for servers/companies/businesses")
 print("")
 print('"CrowdSec is a free,modern & collaborative behavior detection"')
 print('"engine,coupled with a global IP reputation network."')
 print("")
 print("")
 print("unlike maltrail which will work under this concept ")
 print("to detect and block traffic which has been proven to be malicious,")
 print("crowdsec will focus on identifying and blocking traffic that has ")
 print("been proven to have problematic behavior(ddos attack,web crawlers,")
 print("credit card fraud...)")
 print
 print("crowdsec also uses very small system resources.")
 print("")
 print("this way crowdsec will become a complementary program to maltrail")
 print("")
 print("")
 print("Note !")
 print("The installation will not active cscli-dashboard")
 print("")
 print("")


 crowdsec = input("Are you interested to install and enable crowdsec + firewall-bouncer ? [y/n] ")  
 if crowdsec  == "y":

     pro = subprocess.run(['sudo', 'apt-get', 'install', 'curl', '-y'])
     
     pro1 = subprocess.run(
         "curl -s https://packagecloud.io/install/repositories/crowdsec/crowdsec/script.deb.sh | sudo bash", shell=True)
     
     pro2 = subprocess.run(['sudo', 'apt-get', 'install', 'crowdsec'])
     
     pro3 = subprocess.run(
         ['sudo', 'apt-get', 'install', 'crowdsec-firewall-bouncer-iptables', '-y'])

  
     print(pro.returncode)
     print(pro1.returncode)
     print(pro2.returncode)
     print(pro3.returncode)

     if int(pro.returncode + pro1.returncode + pro2.returncode + pro3.returncode)==0:
      print("") 
      print("* Installing crowdsec was successful *")
      print("")
      print("")
      print("the program will continue the installation process in a few seconds, please wait ...")  
      time.sleep(8)

     else:

      print("") 
      print("* warning: Installing crowdsec ended with errors *")
      print("")
      time.sleep(3)
      print("")
      loop = input("Do you want to try to Installing crowdsec again and fix the errors ? [y/n]")  
      if loop  == "y":
        subprocess.run(['sudo', 'bash', 'scripts/fix.sh']) 
        crowdsec_install() 

      else:

        print("") 
        print("* warning: Installing crowdsec was failed *")
        print("")
        time.sleep(3)
        print("")
    
 else:

# Installing fail2ban #

       def fail2ban_commands():
       
        pro = subprocess.run(['sudo', 'apt-get', 'install', 'fail2ban', '-y'])
        pro1 = subprocess.run(['sudo', 'systemctl', 'enable', 'fail2ban'])
        pro2 = subprocess.run(['sudo', 'systemctl', 'start', 'fail2ban'])


        print(pro.returncode)
        print(pro1.returncode)
        print(pro2.returncode)

        if int(pro.returncode + pro1.returncode + pro2.returncode)==0:
         print("########################################################")
         print("*       Installing/enable fail2ban was successful      *")
         print("########################################################")
         print("")
         print("the program will continue the installation process in a few seconds, please wait ...")
         time.sleep(3)

        else:

         print("#########################################################################") 
         print("*                 warning: failed installing fail2ban                   *")
         print("#########################################################################")
         time.sleep(3)
         print("")
         print("##################################################################")
         print("Please check if the internet connection is available and try again")
         print("##################################################################")
         print("")
         loop = input("Do you want to try to installing fail2ban again? [y/n]")  
         if loop  == "y":
          subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
          fail2ban_commands()


         else:

              print("#######################################################################") 
              print("*                 warning: failed installing fail2ban                 *")
              print("#######################################################################")
              time.sleep(3)
              print("")
        
              while input("Do you want to continue without installing fail2ban ? [y/n]") == "n":
                exit ()

       fail2ban_commands()
 
crowdsec_install()


#########################################################################################################################################


#############################
#   Apparmor optimization   #
#############################


def apparmor_commands():

  print("")
  print("")
  print("For advanced users there is the option to enable apparmor in enforce mode and add")
  print("a huge amount of profiles and utilities")
  print("")
  print("This option is not required for regular users,except for those who need a high level of security.")
  print("You can get an explanation of how to use and manage the tool in the following link.")
  print("")
  print("https://linuxhint.com/apparmor-profiles-ubuntu")
  print("")
  print("If you select this option the system will try to create a backup using timeshift called 'return-apparmor' ")
  print("That way you can go back to the state you were before enabled apparmor")
  print("")
  print("You also have the option to change the apparmor profile to 'complain mode' by < sudo aa-complain /etc/apparmor.d/* > ")
  print("")
  print("to disable apparmor manually from the terminal go to grub <sudo nano /etc/default/grub>")
  print("to line 'GRUB_CMDLINE_LINUX_DEFAULT=' ")
  print("change <apparmor=1> to <apparmor=0> save the file")
  print("go to terminal again and update-grub <sudo update-grub> after this reboot your system")
  print("")
  time.sleep(3)

  apparmor = input("Do you want to enable apparmor in enforce mode and install useful apparmor utilities ? [y/n] ")  
  if apparmor  == "y":
      
      def timeshift_create():
          pro = subprocess.run(['sudo', 'timeshift', '--create', '--comments', 'return-apparmor'])
          
          print(pro.returncode)

          if int(pro.returncode)==0:
            print("#################################################")
            print(" timeshift_return-apparmor_backup was successful ")
            print("#################################################") 
            time.sleep(3)
          
          else:

              print("##################################################################") 
              print("*      warning: timeshift_return-apparmor_backup was failed      *")
              print("##################################################################")
              print("")
              time.sleep(3)
              
              loop = input("Do you want to try to backup again? [y/n]")  
              if loop  == "y":
                subprocess.run(['sudo', 'bash', 'scripts/fix.sh']) 
                timeshift_create()
              
              else:

                without = input("Do you want to continue without create timeshift_return-apparmor_backup ? [y/n] ")
                if without == "n":
                 exit()

      timeshift_create()     



      def enable_apparmot():

#### make sure wget is install
          pro1 = subprocess.run(['sudo', 'apt-get', 'install', 'wget', '-y'])
####
          pro2 = subprocess.run(
              ['wget', 'https://www.kicksecure.com/derivative.asc'])
          
          pro4 = subprocess.run(
              "sudo cp derivative.asc /usr/share/keyrings/derivative.asc", shell=True)
          
          pro3 = subprocess.run(
              'echo "deb [signed-by=/usr/share/keyrings/derivative.asc] https://deb.kicksecure.com bullseye main contrib non-free" | sudo tee /etc/apt/sources.list.d/derivative.list', shell=True)
          
          pro4 = subprocess.run(['sudo', 'apt-get', 'update'])
          
          pro5 = subprocess.run(['sudo', 'apt-get', 'install', 'apparmor-profiles', 'apparmor-profiles-extra',
                                 'apparmor-easyprof', 'apparmor-utils', 'certspotter', 'auditd', 'apparmor-profiles-kicksecure', '-y'])
          
          pro6 = subprocess.run(['sudo', 'rm', '-f', 'derivative.asc'])
          
          pro7 = subprocess.run(
              "sudo aa-enforce /etc/apparmor.d/*", shell=True)
          
          print(pro1.returncode)
          print(pro2.returncode)
          print(pro3.returncode)
          print(pro4.returncode)
          print(pro5.returncode)
          print(pro6.returncode)
          print(pro7.returncode)


          if int(pro1.returncode + pro2.returncode + pro3.returncode + pro4.returncode + pro5.returncode 
          + pro6.returncode + pro7.returncode)==0:
              print("#############################################################################") 
              print("* apparmor optimization and installation of useful utilities was successful *")
              print("#############################################################################")
              print("")
              print("the program will continue the installation process in a few seconds, please wait ...")  
              time.sleep(3)
          else:

              print("##################################################") 
              print("* warning: optimize apparmor finished with errors*")
              print("##################################################")
              time.sleep(3)
              print("")
              loop = input("Do you want to try to fix it? [y/n]")  
              if loop  == "y":
                subprocess.run(['sudo', 'bash', 'scripts/fix.sh']) 
                enable_apparmot() 


              else:
              
                  print("############################################") 
                  print("*   warning: failed to optimize apparmor   *")
                  print("############################################")
                  time.sleep(3)
                  print("")
          

      enable_apparmot()  


apparmor_commands()


#########################################################################################################################################


### Linux Kernel security hardening
### Backup sysctl file 


def hardening_commands():

 print("")
 print("")
 print("Use linux Kernel hardening to improve system security")
 print("")
 print("Recommended for use from kernel 5.8 and up.")
 print("")
 print("sysctl is an interface that allows you to make changes")
 print("to a linux kernel,with /etc/sysctl.conf file you can")
 print("configure various linux networking and system settings.")
 print("")
 print("This list(config) includes new fixing")
 print("for security vulnerabilities(2022)")
 print("")
 print("Note !")
 print("I recommend trying the config on a virtual or test")
 print("environment before implementing it in a real system.")
 print("")
 print("you can do it manually in over time by copy the list from")
 print("clamIPS/scripts/sysctl.conf to /etc/sysctl.conf")
 print("")
 print("")


 hardening = input("Do you want to optimize sysctl.conf for security ? [y/n] ")  
 if hardening  == "y":

    pro = subprocess.run(['sudo', 'mkdir', '-p', '/opt/auto-clamIPS/backup/'])
    
    pro1 = subprocess.run(
        ['sudo', 'cp', '-n', '/etc/sysctl.conf', '/opt/auto-clamIPS/backup/'])

    check_sysctl = subprocess.run(
        "grep -F '### AUTO-CLAM-IPS SYSTEM SECURITY OPTIONS ###' /etc/sysctl.conf", capture_output=True, shell=True)
    print(check_sysctl.stdout)

    if int(check_sysctl.returncode) == 1:

      subprocess.run(
          "sudo cat scripts/sysctl.conf >> /etc/sysctl.conf", shell=True)
      
      subprocess.run(['sudo', 'sysctl', '-p'])    
      
    print(pro.returncode)
    print(pro1.returncode)
    


    if int(pro.returncode + pro1.returncode)==0:
       print("#########################################################") 
       print("*       optimize sysctl.conf file was successful         *")
       print("#########################################################")
       print("")
       print("")
       print("the program will continue the installation process in a few seconds, please wait ...")
       time.sleep(3)

    else:

       print("#############################################################################") 
       print("*                warning: optimize sysctl.conf file was failed              *")
       print("#############################################################################")
       time.sleep(3)
       print("")
       print("")
       loop = input("Do you want to try to optimize the file again? [y/n]")  
       if loop  == "y":
        hardening_commands()
            

hardening_commands() 


#########################################################################################################################################



##############################
# enable ufw && install gufw #
##############################



def ufw_commands():
 
 print("")
 print("")
 print("enable ufw and set default(deny incoming/allow outgoing)")
 print("firewall rules for iptables and install gufw (gui for ufw)")
 print("")
 print("")
 print("")
 print("Note!")
 print("")
 print("This default option is intended for regular users who do not")
 print("need to use incoming remote connection such as 'ssh' for example")
 print("")
 print("If you intend to use incoming connections skip this option")
 print("and configure the firewall manually before you enable the rules.")
 print("")
 print("You can get explanation on how to do this at the following link")
 print("")
 print("https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-18-04")
 print("")
 print("")
 print("")

 ufw = input("Are you interested to enable ufw firewall rules for iptables right now ? [y/n]")  
 if ufw  == "y":


    pro = subprocess.run(['sudo', 'apt-get', 'install', 'gufw', '-y'])
    pro2 = subprocess.run(['sudo', 'ufw', 'default', 'deny', 'incoming'])
    pro3 = subprocess.run(['sudo', 'ufw', 'default', 'allow', 'outgoing'])
    pro4 = subprocess.run(['sudo', 'ufw', 'enable'])


    print(pro.returncode)
    print(pro2.returncode)
    print(pro3.returncode)
    print(pro4.returncode)

    if int(pro.returncode + pro2.returncode + pro2.returncode + pro3.returncode
    + pro4.returncode)==0:
        print("########################################################") 
        print("*               enable ufw was successful              *")
        print("########################################################")
        print("")
        print("the program will continue the installation process in a few seconds, please wait ...")
        time.sleep(3)

    else:

        print("#########################################################################") 
        print("*                   warning: enable ufw was failed                      *")
        print("#########################################################################")
        time.sleep(3)
        print("")
        print("")
        loop = input("Do you want to try to install ufw again? [y/n]")  
        if loop  == "y":
          subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
          ufw_commands()


        else:

                print("#############################################################################") 
                print("*                       warning: enable ufw was failed                      *")
                print("#############################################################################")
                time.sleep(3)
                print("")
          
                while input("Do you want to continue without enable ufw ? [y/n]") == "n":
                  exit ()


ufw_commands()


#########################################################################################################################################




### To prevent bugs after the installation finished the program will make sure the file is clean
subprocess.run("sudo -i truncate -s 0 /opt/auto-clamIPS/auto-clamav/logs/change.log", shell=True)




print("")
print("")
print("")
print("############################################")
print("https://github.com/ramner98/auto-clamIPS.git")
print("############################################")
time.sleep(3)
print("")
print("")
print("###############################################")
print("Installation complete please reboot your system")
print("###############################################")
print("")

