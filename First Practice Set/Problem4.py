import os

#selection of the directory whose content wanted to be listed

directory_path = '/'

#use the os module to list the directory content 

contents=os.listdir(directory_path)

#print the comments of the directory 
for item in contents:
    print(item)