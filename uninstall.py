import subprocess
import time


def uninstalling_auto_clamav_commands():


############################################################################################################################
############################################################################################################################


#########################################
# Prepare the system for uninstallation #
#########################################

  def prepare_un_commands():
    pro = subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])

    print(pro.returncode)

    if int(pro.returncode)==0:
        print("#######################################################") 
        print("*             Preparation was successful              *")
        print("#######################################################")
        print("")
        print("the program will continue the process in a few seconds, please wait ...")
        time.sleep(3)

    else:

        print("############################################################################") 
        print("*                   warning: Preparation was was failed                    *")
        print("############################################################################")
        time.sleep(3)
        print("")
        loop = input("Do you want to try to Prepare the system to uninstallation again? [y/n]")  
        if loop  == "y":
          prepare_un_commands()
          

  prepare_un_commands()


##############################################################################################################################
##############################################################################################################################


######################
# auto-clamav-backup #
######################

  def timeshift_commands():
  
      pro = subprocess.run(['sudo', 'timeshift', '--create', '--comments', 'auto-clamav-backup'])
      print(pro.returncode)

      if int(pro.returncode)==0:
          print("") 
          print("*auto_clamav-backup was successful*")
          print("")
          print("")
          print("")
          print("the program will continue the process in a few seconds, please wait ...")
          time.sleep(3)

      else:

          print("") 
          print("*auto_clamav-backup was failed*")
          print("")
          time.sleep(3)
          print("")
          loop = input("Do you want to try to enable auto_clamav-backup again? [y/n]")  
          if loop  == "y":
            subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
            timeshift_commands()
            

                  
  timeshift_commands()


##############################################################################################################################
##############################################################################################################################

  
###############################
#   uninstalling auto_clamav   #
###############################


  def uninstalling_commands():
###   
    pro = subprocess.run(['sudo', 'apt-get', 'remove', 'clamav', '-y'])
    pro2 = subprocess.run(['sudo', 'apt-get', 'purge', 'clamav', '-y'])
    pro3 = subprocess.run(['sudo', 'apt-get', 'remove', 'clamav-daemon', '-y'])
    pro4 = subprocess.run(['sudo', 'apt-get', 'purge', 'clamav-daemon', '-y'])
    pro5 = subprocess.run(['sudo', 'systemctl', 'stop', 'clamscan-root-week.timer'])
    pro6 = subprocess.run(['sudo', 'systemctl', 'disable', 'clamscan-root-week.timer'])
    pro7 = subprocess.run(['sudo', 'systemctl', 'stop', 'clamscan-home-day.timer'])
    pro8 = subprocess.run(['sudo', 'systemctl', 'disable', 'clamscan-home-day.timer'])
    pro9 = subprocess.run(['sudo', 'systemctl', 'stop', 'if-change.timer'])
    pro10 = subprocess.run(['sudo', 'systemctl', 'disable', 'if-change.timer'])
    pro11 = subprocess.run(['sudo', 'systemctl', 'stop', 'if-change-scan.timer'])
    pro12 = subprocess.run(['sudo', 'systemctl', 'disable', 'if-change-scan.timer'])
    pro13 = subprocess.run(['sudo', 'systemctl', 'stop', 'auto-update-clamav.timer'])
    pro14 = subprocess.run(['sudo', 'systemctl', 'disable', 'auto-update-clamav.timer'])
###  
    pro15 = subprocess.run(['sudo', 'systemctl', 'stop', 'notify-send.timer'])
    pro16 = subprocess.run(['sudo', 'systemctl', 'disable', 'notify-send.timer'])
###  
    pro17 = subprocess.run(['sudo', 'systemctl', 'stop', 'maltrail-sensor.service'])
    pro18 = subprocess.run(['sudo', 'systemctl', 'disable', 'maltrail-sensor.service'])
    pro19 = subprocess.run(['sudo', 'systemctl', 'stop', 'maltrail-server.service'])
    pro20 = subprocess.run(['sudo', 'systemctl', 'disable', 'maltrail-server.service'])   
    pro21 = subprocess.run(['sudo', 'systemctl', 'stop', 'listener_maltrail.timer'])
    pro22 = subprocess.run(['sudo', 'systemctl', 'disable', 'listener_maltrail.timer'])
    pro21 = subprocess.run(['sudo', 'systemctl', 'stop', 'maltrail_scan.timer'])
    pro22 = subprocess.run(['sudo', 'systemctl', 'disable', 'maltrail_scan.timer'])
    pro23 = subprocess.run(['sudo', 'bash', '/opt/auto-clamIPS/maltrail/flush_blacklists.sh'])
    pro24 = subprocess.run(['sudo', 'systemctl', 'stop', 'flush_blacklists.timer'])
    pro25 = subprocess.run(['sudo', 'systemctl', 'disable', 'flush_blacklists.timer'])
###  
    pro26 = subprocess.run(['sudo', 'apt-get', 'remove', 'crowdsec', '-y'])
    pro27 = subprocess.run(['sudo', 'apt-get', 'remove', 'crowdsec-firewall-bouncer-iptables', '-y'])
###  
    pro28 = subprocess.run(['sudo', 'systemctl', 'stop', 'rkhunter_scanner.timer'])
    pro29 = subprocess.run(['sudo', 'systemctl', 'disable', 'rkhunter_scanner.timer'])
    pro30 = subprocess.run(['sudo', 'apt-get', 'remove', 'rkhunter', '-y'])
###

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
    print(pro15.returncode)
    print(pro16.returncode)
    print(pro17.returncode)
    print(pro18.returncode)
    print(pro21.returncode)
    print(pro22.returncode)
    print(pro23.returncode)



    if int(pro.returncode|pro2.returncode|pro3.returncode|pro4.returncode)==0:
       print("") 
       print("* uninstalling auto_clamav was successful *")
       print("")
       print("")
       print("the program will continue the process in a few seconds, please wait ...")
       time.sleep(3)

    else:

       print("") 
       print("* warning: uninstalling auto_clamav finished with bugs *")
       print("")
       time.sleep(3)
       print("")
       print("")
       loop = input("Do you want to try to uninstalling auto_clamav again? [y/n]")  
       if loop  == "y":
        subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
        uninstalling_commands()                

  uninstalling_commands()  


##############################################################################################################################
##############################################################################################################################


##############################
#  uninstalling zram-config  #
##############################

### for ubuntu and debian distros

  def zram_commands():

   zram = input("Are you interested to disable zram-config ? [y/n] ")  
   if zram  == "y": 

    pro = subprocess.run(['sudo', 'systemctl', 'stop', 'zram-config.service'])
    pro2 = subprocess.run(['sudo', 'systemctl', 'disable', 'zram-config.service'])


    print(pro.returncode)
    print(pro2.returncode)


    if int(pro.returncode|pro2.returncode)==0:
   
     print("") 
     print("* disable zram-config was successful *")
     print("")
     print("")
     print("the program will continue the process in a few seconds, please wait ...")
     time.sleep(3)

    else:

     print("") 
     print("*warning: disable zram-config was failed*")
     print("")
     time.sleep(1)
     print("")
     loop = input("Do you want to try to disable zram-config again? [y/n]")  
     if loop  == "y":
      subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
      zram_commands()

  zram_commands()


###################################################################################################################################
###################################################################################################################################


#################################
#  restart apparmor to default  #
#################################


####### check apparmor status
  pro0 = subprocess.run("sudo aa-unconfined | grep -F 'avahi-daemon (enforce)'" ,capture_output=True ,shell=True)
  print(pro0.stdout)
  if int(pro0.returncode)==0:
 
    reapparmor = input("Are you interested to restart apparmor to default mode ? [y/n] ")  
    if reapparmor == "y": 

     def reapparmor_commands():
      pro = subprocess.run("sudo aa-complain  /etc/apparmor.d/*" ,shell=True)
      pro2 = subprocess.run(['sudo', 'apt-get', 'purge',  'apparmor-profiles', 'apparmor-profiles-extra',
      'apparmor-easyprof', 'apparmor-notify', 'apparmor-utils', 'certspotter', 'auditd', '-y'])

      print(pro.returncode)
      print(pro2.returncode)
 
      if int(pro.returncode|pro2.returncode)==0:
       print("") 
       print(" *** restart apparmor to default was successful  ***")
       print("")
       print("")
       print("the program will continue the process in a few seconds, please wait ...")
       time.sleep(3)

      else:

       print("") 
       print("***  warning: restart apparmor to default was failed  ***")
       print("")
       time.sleep(3)
       print("")
       print("")
       loop = input("Do you want to try to fix the problem and try again? [y/n]")  
       if loop  == "y":
        subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
        reapparmor_commands()
          

     reapparmor_commands()

###################################################################################################################################


######################
# return sysctl.conf #
######################


  def returnup_commands():
   
   print("")
   print("using sysctl.conf backup to return the")
   print("file to the state it was in before")
   print("installing the program")
   print("")
   print("Note !")
   print("This action will overwrite the current file")
   print("")
   print("")

   returnup = input("Are you interested to return sysctl.conf to its original state ? [y/n] ")
   if returnup == "y": 

    pro = subprocess.run(['sudo', 'cp', '/opt/auto-clamIPS/backup/sysctl.conf', '/etc/sysctl.conf'])

    print(pro.returncode)

    if int(pro.returncode)==0:
       print("") 
       print("*** return sysctl.conf file was successful ***")
       print("")
       print("")
       time.sleep(3)

    else:

       print("") 
       print("*** warning: return sysctl.conf file was failed ***")
       print("")
       time.sleep(3)
       print("")
       print("")
       loop = input("Do you want to try to return the file again? [y/n]")  
       if loop  == "y":
        subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
        returnup_commands()
            

  returnup_commands()  


############################################################################################################################
############################################################################################################################



#############################
#  autoclean && autoremove  #
#############################


  def autoclean_commands():
   pro = subprocess.run(['sudo', 'apt-get', 'autoclean', '-y'])
   pro2 = subprocess.run(['sudo', 'apt-get', 'auto-remove', '-y'])

   print(pro.returncode)
   print(pro2.returncode)

   if int(pro.returncode|pro2.returncode)==0:
      print("###########################################################") 
      print("*         autoclean && autoremove was successful          *")
      print("###########################################################")
      print("")
      print("the program will continue the process in a few seconds, please wait ...")
      time.sleep(3)

   else:

      print("##############################################################################") 
      print("*                warning: autoclean && autoremove was failed                 *")
      print("##############################################################################")
      time.sleep(3)
      print("")
      print("")
      loop = input("Do you want to try to autoclean && autoremove again? [y/n]")  
      if loop  == "y":
       subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
       autoclean_commands()
          

  autoclean_commands()


uninstalling_auto_clamav_commands()



print("")
print("")
print("")
print("############################################")
print("https://github.com/ramner98/auto-clamIPS.git")
print("############################################")
time.sleep(3)
print("")
print("")
print("#################################################")
print("Uninstallation complete please reboot your system")
print("#################################################")
