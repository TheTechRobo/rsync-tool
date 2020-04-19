# rsync-tool
 sync two folders together using a single command (on Mac and Linux)
 
 # Requirements
 * Mac OS X Lion and  OS X Yosemite are the only OSes this is tested on
 * For linux, the only thing this is tested on is Raspbian Stretch 2018-11
 * A terminal
# Instructions
 you will need to do the following:
 
- A better version of `rsync-tool` is now in [goodiecommand](https://github.com/thetechrobo/goodiecommand)!
- It is much easier and does not require editing a file.


# Making it Easier
 I have just added a file called 'Sync Two Folders.app'. 
 
 it's an Automator script. 
 
 to modify the paths just open Automator. File>Open
 Navigate to the script and change the paths. 
 after that save it,
 and you can run the app whenever to sync the two folders. 
 you can add your own Automator blocks to e.g. add a notification that says 'Successful!'
 
 
# Python script
 I made a python script
 
 It should work
 
 Its filename is:
 
	rsync.py

# Running it just once
The Python script asks you to run it once or indefinitely.  
To stop it (if you chose indefinitely), press ^C or close the terminal.


###### Looping Automator
Open the script as you would (above) and add the following block AFTER the shell script command:
Loop
Choose how much you want it to loop — you can't choose forever :( — so just type e.g. Loop 120 minutes and add another loop for 200 minutes 
so that it will loop the 120 minutes and then loop the 120 minutes again for 200 minutes and then repeat the 200 minutes for 220 minutes and so on. 

# Why shouldn't I use another, closed-source, more sophisticated third-party tool?
Because, unlike with another tool, you can easily check what's going on in the code, so you're sure that it's not a virus. Also, sophisticated isn't always better, and you're also supporting open-source ;) 
<p></p>
And plus, this uses an **official** Linux tool that's **included**. The developers wouldn't have added it if it was trouble ;)

# I hope you enjoy my script!
Courtesy to [ChrisWrites](https://www.chriswrites.com/how-to-sync-files-and-folders-on-the-mac/) for the instructions :)
