import os
print("Loading...")
while True: #comment for run-once
	os.system('rsync -aE --delete Src Des') #delete indent for run-once
	print("To stop, close the terminal")
