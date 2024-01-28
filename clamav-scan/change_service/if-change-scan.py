import subprocess
import time
import schedule



###################################################################
### On rare occasions 'inotify' may miss an output,in order     ###
### to reduce this possibility to the minimum possible,the      ###
### program will use two monitors and scanners that will        ###
### work in a complementary way with each other,the scanners    ###
### will monitor files with a different output(type of change)  ###
### but with a logical value corresponding to the other scanner ###
### thus reducing the scanning time of each of them.The result  ###
### will be a more reliable scan without the need to use more   ###
### processing power on the part of the CPU.                    ###
###################################################################


def clean_old():
### Clear old data before entering the loop
 subprocess.run(
    "sudo -i truncate -s 0 /opt/auto-clamIPS/auto-clamav/logs/change.log", shell=True)
 subprocess.run(
    "sudo -i truncate -s 0 /opt/auto-clamIPS/auto-clamav/logs/change2.log", shell=True)
 subprocess.run(
    "sudo -i truncate -s 0 /opt/auto-clamIPS/auto-clamav/logs/scan.log", shell=True)
 subprocess.run(
    "sudo -i truncate -s 0 /opt/auto-clamIPS/auto-clamav/logs/auto.log", shell=True)
###
 subprocess.run(
    "sudo -i truncate -s 0 /opt/auto-clamIPS/auto-clamav/logs/change_entangl.log", shell=True)
 subprocess.run(
    "sudo -i truncate -s 0 /opt/auto-clamIPS/auto-clamav/logs/change2_entangl.log", shell=True)
 subprocess.run(
    "sudo -i truncate -s 0 /opt/auto-clamIPS/auto-clamav/logs/scan_entangl.log", shell=True)
 subprocess.run(
    "sudo -i truncate -s 0 /opt/auto-clamIPS/auto-clamav/logs/auto_entangl.log", shell=True)
###
clean_old()


def loop_scan():
   
# Wait until the service finishes updating itself if it
# happens duringthe scan.the system will scan all the
# changes after the service is back up and running.
 def check_daemon_service():
 
  check_daemon = subprocess.run(
     "sudo systemctl status clamav-daemon | grep -E 'Starting Clam AntiVirus|Started Clam AntiVirus|inactive' && clamdscan --fdpass --infected /opt/auto-clamIPS/  | grep -E 'LibClamAV Error:|ERROR:'", capture_output=True, shell=True)
  print(check_daemon.stdout)

  if int(check_daemon.returncode) == 0:
   time.sleep(3)
   check_daemon_service()

 check_daemon_service()
  
 
###

 def change_commands():

 ### searches for files that have been modified
   check_changes = subprocess.run(
      "grep -E 'CREATE |ATTRIB ' /opt/auto-clamIPS/auto-clamav/logs/change.log", capture_output=True, shell=True)
   print(check_changes.stdout)

   if int(check_changes.returncode) == 0:

### prepares and fix the list to include only modified files
    subprocess.run(
      "sudo sort -u /opt/auto-clamIPS/auto-clamav/logs/change.log >> /opt/auto-clamIPS/auto-clamav/logs/change2.log", shell=True)
    subprocess.run(
      "sudo grep -E 'CREATE |ATTRIB ' /opt/auto-clamIPS/auto-clamav/logs/change2.log >> /opt/auto-clamIPS/auto-clamav/logs/scan.log", shell=True)
    subprocess.run(
      "sudo cut -d ' ' -f 2,3-1024 /opt/auto-clamIPS/auto-clamav/logs/scan.log >> /opt/auto-clamIPS/auto-clamav/logs/auto.log", shell=True)
    subprocess.run(
      "sudo -i truncate -s 0 /opt/auto-clamIPS/auto-clamav/logs/change.log", shell=True)
    subprocess.run(
      "sudo -i truncate -s 0 /opt/auto-clamIPS/auto-clamav/logs/change2.log", shell=True)
###

    subprocess.run(
      "sudo -i truncate -s 0 /opt/auto-clamIPS/auto-clamav/logs/data_2.log", shell=True)
### Clear old scan tracking in a log file and scan with 'clamav' and send new results to data_2.log.
### "data_2.log" intended only for tracking faults during the scan.
    subprocess.run(
      "sudo bash '/opt/auto-clamIPS/auto-clamav/clamav-scan-if.sh'", shell=True)

  

    check_infected = subprocess.run(
        "grep -F 'FOUND' /var/log/clamav/clamav-found-malware-$(date +'%Y-%m-%d').log", capture_output=True, shell=True)

    print(check_infected.stdout)
    if int(check_infected.returncode) == 0:
       subprocess.run(
          ['sudo', 'bash', '/opt/auto-clamIPS/auto-clamav/clamav-scan-if2.sh'])

    subprocess.run(
        "sudo -i truncate -s 0 /opt/auto-clamIPS/auto-clamav/logs/scan.log", shell=True)
    subprocess.run(
        "sudo -i truncate -s 0 /opt/auto-clamIPS/auto-clamav/logs/auto.log", shell=True)
    subprocess.run(
        "sudo -i truncate -s 0 /var/log/clamav/clamav-found-malware-$(date +'%Y-%m-%d').log", shell=True)
   
    subprocess.run(
        "sudo -i echo '/opt/auto-clamIPS/auto-clamav/logs/auto_entangl.log' > /opt/auto-clamIPS/auto-clamav/auto_check.log", shell=True)
 
   else:
      subprocess.run(
      "sudo -i truncate -s 0 /opt/auto-clamIPS/auto-clamav/logs/change.log", shell=True)


 change_commands()

 
###
###
###

 time.sleep(5)
 def check_daemon_service():
  
  check_daemon = subprocess.run(
     "sudo systemctl status clamav-daemon | grep -E 'Starting Clam AntiVirus|Started Clam AntiVirus|inactive' && clamdscan --fdpass --infected /opt/auto-clamIPS/  | grep -E 'LibClamAV Error:|ERROR:'", capture_output=True, shell=True)
  print(check_daemon.stdout)

  if int(check_daemon.returncode) == 0:
   time.sleep(3)
   check_daemon_service()

 check_daemon_service()
  
 
###

 def change_commands_entangl():

 ### searches for files that have been modified
   check_changes = subprocess.run(
      "grep -E 'MOVED_TO |CLOSE_WRITEXCLOSE ' /opt/auto-clamIPS/auto-clamav/logs/change_entangl.log", capture_output=True, shell=True)
   print(check_changes.stdout)

   if int(check_changes.returncode) == 0:

### prepares and fix the list to include only modified files
    subprocess.run(
      "sudo sort -u /opt/auto-clamIPS/auto-clamav/logs/change_entangl.log >> /opt/auto-clamIPS/auto-clamav/logs/change2_entangl.log", shell=True)
    subprocess.run(
      "sudo grep -E 'MOVED_TO |CLOSE_WRITEXCLOSE ' /opt/auto-clamIPS/auto-clamav/logs/change2_entangl.log >> /opt/auto-clamIPS/auto-clamav/logs/scan_entangl.log", shell=True)
    subprocess.run(
      "sudo cut -d ' ' -f 2,3-1024 /opt/auto-clamIPS/auto-clamav/logs/scan_entangl.log >> /opt/auto-clamIPS/auto-clamav/logs/auto_entangl.log", shell=True)
    subprocess.run(
      "sudo -i truncate -s 0 /opt/auto-clamIPS/auto-clamav/logs/change_entangl.log", shell=True)
    subprocess.run(
      "sudo -i truncate -s 0 /opt/auto-clamIPS/auto-clamav/logs/change2_entangl.log", shell=True)
###

    subprocess.run(
      "sudo -i truncate -s 0 /opt/auto-clamIPS/auto-clamav/logs/data_2.log", shell=True)


    subprocess.run(
      "sudo bash '/opt/auto-clamIPS/auto-clamav/clamav-scan-if.sh'", shell=True)

  

    check_infected = subprocess.run(
        "grep -F 'FOUND' /var/log/clamav/clamav-found-malware-$(date +'%Y-%m-%d').log", capture_output=True, shell=True)

    print(check_infected.stdout)
    if int(check_infected.returncode) == 0:
       subprocess.run(
          ['sudo', 'bash', '/opt/auto-clamIPS/auto-clamav/clamav-scan-if2.sh'])

    subprocess.run(
        "sudo -i truncate -s 0 /opt/auto-clamIPS/auto-clamav/logs/scan_entangl.log", shell=True)
    subprocess.run(
        "sudo -i truncate -s 0 /opt/auto-clamIPS/auto-clamav/logs/auto_entangl.log", shell=True)
    subprocess.run(
        "sudo -i truncate -s 0 /var/log/clamav/clamav-found-malware-$(date +'%Y-%m-%d').log", shell=True)
   
    subprocess.run(
        "sudo -i echo '/opt/auto-clamIPS/auto-clamav/logs/auto.log' > /opt/auto-clamIPS/auto-clamav/auto_check.log", shell=True)
 
   else:
      subprocess.run(
      "sudo -i truncate -s 0 /opt/auto-clamIPS/auto-clamav/logs/change_entangl.log", shell=True)


 change_commands_entangl()

loop_scan()


schedule.every(5).seconds.do(loop_scan)

while 1:
   schedule.run_pending()
   time.sleep(1)
