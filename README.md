# rsync-tool
 sync two folders together using a single command (on Mac)
 
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
 I have just added a file called 'Sync Two Folders.app'. 
 
 it's an Automator script. 
 
 to modify the paths just open Automator. File>Open
 Navigate to the script and change the paths. 
 after that save it,
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

# Running it continuously
I am not great at bash programming so I cannot do this there...yet. 

Modify your Python code to be:

	import os
	while True:
		os.system('rsync -aE SrcPath DesPath')
Then it should loop, so long as you don't close the terminal

###### Looping Automator
Open the script as you would (above) and add the following block AFTER the shell script command:
Loop
Choose how much you want it to loop — you can't choose forever :( — so just type e.g. Loop 120 minutes and add another loop for 200 minutes 
so that it will loop the 120 minutes and then loop the 120 minutes again for 200 minutes and then repeat the 200 minutes for 220 minutes and so on. 

# Why shouldn't I use another, closed-source, third-party tool?
Because, unlike with a third-party tool, with this you can actually — and easily — check what's going on in the code.
So you're sure that it's not a virus. Plus, you're supporting open-source :)

# I hope you enjoyed! 
