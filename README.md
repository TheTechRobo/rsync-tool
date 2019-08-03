# rsync-tool
 sync two folders together using a single command
 
# Instructions
 you will need to do the following:
 
- open your terminal
- pico rsync.sh
- modify rsync.sh for the source & destination paths
- Ctrl-X
- type y and then enter
- chmod +x rsync.sh
- ./rsync.sh
- you will need to run it whenever you want to sync it, it is not continuous


# Making it Easier
 I have just added a file called 'Sync Two Folders.app'
 it's an Automator script
 to modify the paths just open Automator. 
 File>Open
 Navigate to the script
 And change the stuff
 after that save it
 and you can run the app whenever to sync the two folders. 
 you can add your own Automator blocks to e.g. add a notification that says 'Successful!'
 
 
# Python script
 you can also make a Python script
 the process is faster
 type:
	import os
	os.system('rsync -aE SourceFolderPath DestinationFolderPath')
 then you just need in the terminal:
	python ScriptFilename
then it should work :)