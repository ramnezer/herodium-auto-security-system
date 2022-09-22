import subprocess
import time

def change_commands():

### 
 check_malware = subprocess.run(
     "grep -E '(malware)|(malicious)' /opt/auto-clamIPS/maltrail/logs/scan.log", capture_output=True, shell=True)
 print(check_malware.stdout)

 if int(check_malware.returncode) == 0:
  subprocess.run(['sudo', 'systemctl', 'stop', 'maltrail_scan.timer'])
 
  subprocess.run(
      "sudo grep -E '(malware)|(malicious)' /opt/auto-clamIPS/maltrail/logs/scan.log >> /opt/auto-clamIPS/maltrail/logs/clean.log", shell=True)
 
  subprocess.run(
      "sudo -i truncate -s 0 /opt/auto-clamIPS/maltrail/logs/scan.log", shell=True)
 
  subprocess.run(
      "sudo cut -d ' ' -f 10 /opt/auto-clamIPS/maltrail/logs/clean.log >> /opt/auto-clamIPS/maltrail/logs/clean1.log", shell=True)
  
  subprocess.run(
      "sudo cut -d ' ' -f 1 /opt/auto-clamIPS/maltrail/logs/clean1.log >> /opt/auto-clamIPS/maltrail/logs/clean2.log", shell=True)
  
  subprocess.run(['sudo', 'bash', '/opt/auto-clamIPS/maltrail/maltrail-clear-symbols.sh'])

  subprocess.run(
      "sudo sort -u /opt/auto-clamIPS/maltrail/logs/clean3.log >> /opt/auto-clamIPS/maltrail/logs/ipset.log", shell=True)
  
  subprocess.run(
      "sudo -i truncate -s 0 /opt/auto-clamIPS/maltrail/logs/clean.log", shell=True)
  
  subprocess.run(
      "sudo -i truncate -s 0 /opt/auto-clamIPS/maltrail/logs/clean1.log", shell=True)
  
  subprocess.run(
      "sudo -i truncate -s 0 /opt/auto-clamIPS/maltrail/logs/clean2.log", shell=True)

  subprocess.run(
      "sudo -i truncate -s 0 /opt/auto-clamIPS/maltrail/logs/clean3.log", shell=True)

  subprocess.run(
      "sudo bash '/opt/auto-clamIPS/maltrail/blacklist.sh'", shell=True)
  
  subprocess.run(
      "sudo -i truncate -s 0 /opt/auto-clamIPS/maltrail/logs/ipset.log", shell=True)

### To avoid duplicates while scanning url we will perform double clean to scan log
  subprocess.run(
      "sudo -i truncate -s 0 /opt/auto-clamIPS/maltrail/logs/scan.log", shell=True)
 
  subprocess.run(['sudo', 'systemctl', 'start', 'maltrail_scan.timer'])


change_commands()

