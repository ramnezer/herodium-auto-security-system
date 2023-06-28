import subprocess
import time



# Wait until the service finishes updating itself if it
# happens duringthe scan.the system will scan all the
# changes after the service is back up and running.
def check_daemon_service():
 
 check_daemon = subprocess.run(
     "sudo systemctl status clamav-daemon | grep -E 'Starting Clam AntiVirus|Started Clam AntiVirus'", capture_output=True, shell=True)
 print(check_daemon.stdout)

 if int(check_daemon.returncode) == 0:
  time.sleep(3)
  check_daemon_service()

check_daemon_service()
  
 
###

def change_commands():

 ### searches for files that have been modified
  check_changes = subprocess.run(
     "grep -E 'CREATE |MOVED_TO |CLOSE_WRITEXCLOSE ' /opt/auto-clamIPS/auto-clamav/logs/change.log", capture_output=True, shell=True)
  print(check_changes.stdout)

  if int(check_changes.returncode) == 0:
### stop the execution service to avoid duplicate scans(the change scanner will remain active).
   subprocess.run(['sudo', 'systemctl', 'stop', 'if-change-scan.timer'])
### prepares and fix the list to include only modified files
   subprocess.run(
      "sudo sort -u /opt/auto-clamIPS/auto-clamav/logs/change.log >> /opt/auto-clamIPS/auto-clamav/logs/change2.log", shell=True)
   subprocess.run(
      "sudo grep -E 'CREATE |MOVED_TO |CLOSE_WRITEXCLOSE ' /opt/auto-clamIPS/auto-clamav/logs/change2.log >> /opt/auto-clamIPS/auto-clamav/logs/scan.log", shell=True)
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
   
   time.sleep(3)
   subprocess.run(['sudo', 'systemctl', 'start', 'if-change-scan.timer'])
 
  else:
     subprocess.run(
     "sudo -i truncate -s 0 /opt/auto-clamIPS/auto-clamav/logs/change.log", shell=True)


change_commands()
