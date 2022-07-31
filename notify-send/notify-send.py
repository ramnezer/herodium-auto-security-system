import subprocess
import time


def check_infected():
 check_infected = subprocess.run(
     "grep -F 'FOUND' /opt/auto-clamIPS/notify-clamMA/logs/notify.log", capture_output=True, shell=True)
 print(check_infected.stdout)

 if int(check_infected.returncode) == 0:
  subprocess.run(
      "sudo notify-send -u critical  '     ! WARNING !' 'MALWARE-FOUND' -i '/opt/auto-clamIPS/notify-clamMA/notify-media/malware1.png'", shell=True)
  time.sleep(10)

  subprocess.run(
      "sudo -i truncate -s 0 /opt/auto-clamIPS/notify-clamMA/logs/notify.log", shell=True)

 check_infected2 = subprocess.run(
     "grep -F 'FOUND' /opt/auto-clamIPS/notify-clamMA/logs/notify1.log", capture_output=True, shell=True)
 print(check_infected2.stdout)

 if int(check_infected2.returncode) == 0:
  subprocess.run(
      "sudo notify-send -u critical  '     ! WARNING !' 'MALWARE OR A SUSOICIOUS FILE IS FOUND' ", shell=True)
  time.sleep(10)
  subprocess.run(
      "sudo -i truncate -s 0 /opt/auto-clamIPS/notify-clamMA/logs/notify1.log", shell=True)

 check_malware = subprocess.run(
     "grep -F '(malware)' /opt/auto-clamIPS/notify-clamMA/logs/notify2.log", capture_output=True, shell=True)
 print(check_malware.stdout)

 if int(check_malware.returncode) == 0:
  subprocess.run("sudo notify-send -u critical  '     ! WARNING !' 'The system detected malicious network traffic'  -i '/opt/auto-clamIPS/notify-clamMA/notify-media/net-malwares1.png'", shell=True)
  time.sleep(10)
  subprocess.run(
      "sudo -i truncate -s 0 /opt/auto-clamIPS/notify-clamMA/logs/notify2.log", shell=True)


check_infected()
