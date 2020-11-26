import time
from sys import exit
from subprocess import Popen as r
print("Loading...")
time.sleep(1.5)
source = input("What is the SOURCE DIRECTORY? ")
destination = input("What is the DESTINATION DIRECTORY?")
onceOrTwice = input("Would you like rsync-tool to run rsync ONCE or INDEFINITELY? ")
if onceOrTwice.lower() == "once":
	try:
	    r(["rsync -aE --delete ", source, " ", destination], shell=True)
    except Exception:
        exit("An error occured: %s." % Exception)
    print("All done.")
elif onceOrTwice.lower() == "indefinitely":
    while True:
        try:
	        r(["rsync -aE --delete ", source, " ", destination], shell=True)
        except KeyboardInterrupt:
             exit("You exited.")
        except:
            exit("An error occured.")
        print("Press ^C to cancel.")
