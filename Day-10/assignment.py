#Write a python program to get list of files inside a directories that a user provides
import os

folders = input("Please provide the list of directories with space in betweeen them: ").split()

for folder in folders:

    try:
        files = os.listdir(folder)
    
    except FileNotFoundError:
        print("Please enter a valid folder name, looks like this folder does not exist: " + folder)
        continue   # you can use 'break' here if you want the program to stop executing further 

    except PermissionError: 
         print("Sorry no access to this folder: ", folder)
         continue

    print("======> Listing files for the folder - " + folder + " <======")
    
    for file in files:
            print(file)


