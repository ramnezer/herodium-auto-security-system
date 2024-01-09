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
        
        print("")
        print("")
        print("#######################################################") 
        print("*             Preparation was successful              *")
        print("#######################################################")
        print("")
        print("")
        print("the program will continue the process in a few seconds, please wait ...")
        time.sleep(3)

    else:
        print("")
        print("")
        print("############################################################################") 
        print("*                   warning: Preparation was was failed                    *")
        print("############################################################################")
        time.sleep(3)
        print("")
        print("")
        loop = input("Do you want to try to Prepare the system to uninstallation again? [y/n]")  
        if loop  == "y":
          prepare_un_commands()
          

 prepare_un_commands()


##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################

  
################################
#   uninstalling auto_clamav   #
################################


 def uninstalling_commands():
###   
    pro = subprocess.run(['sudo', 'systemctl', 'disable', 'clamav-daemon'])
    pro3 = subprocess.run(['sudo', 'systemctl', 'stop', 'clamav-daemon'])
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
    pro26 = subprocess.run(['sudo', 'apt-get', 'purge', 'crowdsec', '-y'])
    
    pro27 = subprocess.run(['sudo', 'apt-get', 'remove', 'crowdsec-firewall-bouncer-iptables', '-y'])
    pro27 = subprocess.run(['sudo', 'apt-get', 'purge', 'crowdsec-firewall-bouncer-iptables', '-y'])
###  
    pro28 = subprocess.run(['sudo', 'systemctl', 'stop', 'rkhunter_scanner.timer'])
    pro29 = subprocess.run(['sudo', 'systemctl', 'disable', 'rkhunter_scanner.timer'])
    pro30 = subprocess.run(['sudo', 'apt-get', 'remove', 'rkhunter', '-y'])
    pro31 = subprocess.run(['sudo', 'apt-get', 'remove', 'cpulimit', '-y'])
    pro32 = subprocess.run(['sudo', 'systemctl', 'stop', 'media_scan.timer'])
    pro33 = subprocess.run(['sudo', 'systemctl', 'disable', 'media_scan.timer'])
    pro34 = subprocess.run(['sudo', 'truncate', '-s', '0', '/opt/auto-clamIPS/auto-clamav/logs/install.log'])
###

    print(pro.returncode)
    print(pro3.returncode)
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
    print(pro24.returncode)
    print(pro25.returncode)
    print(pro26.returncode)
    print(pro27.returncode)
    print(pro28.returncode)
    print(pro29.returncode)
    print(pro30.returncode)
    print(pro31.returncode)
    print(pro32.returncode)
    print(pro33.returncode)
    print(pro34.returncode)


    if int(pro.returncode|pro3.returncode)==0:
       
       print("")
       print("") 
       print("* uninstalling auto_clamav was successful *")
       print("")
       print("")
       print("the program will continue the process in a few seconds, please wait ...")
       print("")
       print("")
       time.sleep(3)

    else:
       
       print("")
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

uninstalling_auto_clamav_commands()


##############################################################################################################################
##############################################################################################################################

