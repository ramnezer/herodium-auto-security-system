import subprocess
import time

def notify_send():

### in case of switching between users,fix the service to the currently user that is currently in use

 check_user = subprocess.run(
     " users | cut -d ' ' -f 1", capture_output=True, shell=True)
 print(check_user.stdout.decode())

  
 with open('/etc/systemd/system/notify-send.service', 'r', encoding='utf-8') as file:
    data = file.readlines()

 print(data)
 data[5] = str('Environment="DISPLAY=:0" "XAUTHORITY=/home/') + (check_user.stdout.decode())
 
 with open('/etc/systemd/system/notify-send.service', 'w', encoding='utf-8') as file:
    file.writelines(data)

 subprocess.run(
     ['sudo', 'bash', '/opt/auto-clamIPS/notify-clamMA/notify_send.sh'])

 subprocess.run(['sudo', 'systemctl', 'daemon-reload'])
 subprocess.run(['sudo', 'systemctl', 'restart', 'notify-send.service'])
	
notify_send()  
