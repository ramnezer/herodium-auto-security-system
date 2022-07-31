import subprocess
import time

def freshclam_fix():

 pro = subprocess.run(['sudo', 'bash', 'freshclam_fix.sh'])
 check_error = subprocess.run(
     "grep -E '429|403' freshclam_error.log", capture_output=True, shell=True)
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
     print("updating your database") 
     print("")
     print("")
     loop = input("Do you want to try to fix the problem ? [y/n] ")
     if loop  == "y":
      subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
      print("")
      print("Please wait it may take some time ...")
      print("")
      subprocess.run('sudo rm -f  "/var/lib/clamav/bytecode.cvd" "/var/lib/clamav/daily.cld" "/var/lib/clamav/freshclam.dat" "/var/lib/clamav/main.cvd"' ,shell=True)       
      subprocess.run('sudo systemctl stop clamav-freshclam && sudo freshclam && sudo systemctl start clamav-freshclam' ,shell=True)       
      freshclam_fix()

freshclam_fix()


