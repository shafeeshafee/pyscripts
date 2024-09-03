import os

path_to_traverse = input("Enter the folder you want to check: ")

# create count checks for dir_count and file_count
dir_count = 0
file_count = 0

for item in os.listdir(path_to_traverse):
    # get full path of each item
        # /home/john/file.txt instead of just file.txt
    item_path = os.path.join(path_to_traverse, item)
    if os.path.isdir(item_path):
        dir_count += 1
    elif os.path.isfile(item_path):
        file_count += 1

print(f"There are {dir_count} directories and {file_count} files in {path_to_traverse}")
