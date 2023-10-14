import subprocess
import time



###  Verify that the clamav Signature database has been updated every 24 hours

def check_internet(): 

 pro = subprocess.run(
     "ping -q -w 1 -c 1 `ip r | grep default | cut -d ' ' -f 3` > /dev/null && echo ok", capture_output=True, shell=True)

 print(pro.stdout)


 if int(pro.returncode)==0:
  
  def auto_update_clamav():

    pro = subprocess.run(['sudo', 'apt-get', 'update'])
    time.sleep(3)
    pro1 = subprocess.run(['sudo', 'systemctl', 'stop', 'clamav-freshclam'])
    time.sleep(3)
    pro2 = subprocess.run(['sudo', 'freshclam'])
    time.sleep(3)
    pro3 = subprocess.run(['sudo', 'systemctl', 'start', 'clamav-freshclam'])
    time.sleep(3)
    

### Make sure the service ('clamav-daemon') is not updated while 'clamdscan' is running
### In order not to break the scan.wait until the end and perform an update    
    
    def check_clamdscan_if():
     
     check_clamdscan = subprocess.run(['pgrep', '-f',  "clamdscan --fdpass"])
     print(check_clamdscan.returncode)
    
     if int(check_clamdscan.returncode) == 0:
      print("wait...")
      time.sleep(60)
      check_clamdscan_if()
     
     else:
      
      update_clamav_daemon = subprocess.run(['sudo', 'systemctl', 'restart', 'clamav-daemon'])   
   
    check_clamdscan_if()
    
  ### check if rkhunter is installed and update if it is true
  
    check_rkhunter = subprocess.run(['sudo', 'rkhunter', '--version'])
    print(check_rkhunter.returncode)

    if int(check_rkhunter.returncode) == 0:
     pro4 = subprocess.run(['sudo', 'rkhunter', '--update'])

  auto_update_clamav()

check_internet()
