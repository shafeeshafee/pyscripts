# import the os module

# get input for directory to look in
# create a counter set it at 0
# for item inside the directory
# when a directory or file is found, add to counter
# in the end display "There are x many items in this folder"


import os

path_to_traverse = input("Enter the folder you want to check: ")

item_count = 0

for item in os.listdir(path_to_traverse):
    item_count += 1

print(f"There are {item_count} items in {path_to_traverse}")
