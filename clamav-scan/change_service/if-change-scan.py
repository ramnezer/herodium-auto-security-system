import subprocess
import time


def change_commands():

 ### searches for files that have been modified
 check_changes = subprocess.run(
     "grep -E 'CREATE |MOVED_TO ' /opt/auto-clamIPS/auto-clamav/logs/change.log", capture_output=True, shell=True)
 print(check_changes.stdout)

 if int(check_changes.returncode) == 0:
  ### stop the execution service to avoid duplicate scans(the change scanner will remain active).
  subprocess.run(['sudo', 'systemctl', 'stop', 'if-change-scan.timer'])
### prepares and fix the list to include only modified files
  subprocess.run(
      "sudo sort -u /opt/auto-clamIPS/auto-clamav/logs/change.log >> /opt/auto-clamIPS/auto-clamav/logs/change2.log", shell=True)
  subprocess.run(
      "sudo grep -E 'CREATE |MOVED_TO ' /opt/auto-clamIPS/auto-clamav/logs/change2.log >> /opt/auto-clamIPS/auto-clamav/logs/scan.log", shell=True)
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
      "sudo bash '/opt/auto-clamIPS/auto-clamav/clamav-scan-if.sh' >>'/opt/auto-clamIPS/auto-clamav/logs/data_2.log' 2>&1", shell=True)

  pro2 = subprocess.run(
      "grep -F 'access file' /opt/auto-clamIPS/auto-clamav/logs/data_2.log", capture_output=True, shell=True)
  print(pro2.stdout)
  if int(pro2.returncode) == 0:
    subprocess.run(
        "sudo -i truncate -s 0 /opt/auto-clamIPS/auto-clamav/logs/data_2.log", shell=True)
    subprocess.run(
        ['sudo', 'bash', '/opt/auto-clamIPS/auto-clamav/clamav-scan-home2.sh'])

    pro0 = subprocess.run(
        "grep -F 'FOUND' /var/log/clamav/clamav-found-malware-$(date +'%Y-%m-%d').log", capture_output=True, shell=True)
    print(pro0.stdout)
    if int(pro0.returncode) == 0:
     subprocess.run(
         ['sudo', 'bash', '/opt/auto-clamIPS/auto-clamav/clamav-scan-if2.sh'])
    subprocess.run(
        "sudo -i truncate -s 0 /opt/auto-clamIPS/auto-clamav/logs/scan.log", shell=True)
    subprocess.run(
        "sudo -i truncate -s 0 /opt/auto-clamIPS/auto-clamav/logs/auto.log", shell=True)
    subprocess.run(['sudo', 'systemctl', 'start', 'if-change-scan.timer'])

  else:

    check_infected = subprocess.run(
        "grep -F 'FOUND' /var/log/clamav/clamav-found-malware-$(date +'%Y-%m-%d').log", capture_output=True, shell=True)
### Check if infected files are found and if it is correct sends a
### warning and performs a full scan of the home directory.
###
### Cleans log files and returns the execution service to be active.
### The change scanner service will clean its log ('change.log') just before using the
### scan and will remain active all the time so that if there are new
### changes during the scan it will not miss them and will perform a
### specific scan only for the newly added files.

    print(check_infected.stdout)
    if int(check_infected.returncode) == 0:
     subprocess.run(
         ['sudo', 'bash', '/opt/auto-clamIPS/auto-clamav/clamav-scan-if2.sh'])
     subprocess.run(
         ['sudo', 'bash', '/opt/auto-clamIPS/auto-clamav/clamav-scan-home2.sh'])

    subprocess.run(
        "sudo -i truncate -s 0 /opt/auto-clamIPS/auto-clamav/logs/scan.log", shell=True)
    subprocess.run(
        "sudo -i truncate -s 0 /opt/auto-clamIPS/auto-clamav/logs/auto.log", shell=True)
    subprocess.run(
        "sudo -i truncate -s 0 /var/log/clamav/clamav-found-malware-$(date +'%Y-%m-%d').log", shell=True)

    subprocess.run(['sudo', 'systemctl', 'start', 'if-change-scan.timer'])
 
 else:
    subprocess.run(
    "sudo -i truncate -s 0 /opt/auto-clamIPS/auto-clamav/logs/change.log", shell=True)


change_commands()
