import os
import time

def get_dir_size(dir):
    # check if dir exists and is actually a dir
    if not os.path.exists(dir):
        raise FileNotFoundError(f"{dir} does not exist.")
    if not os.path.isdir(dir):
        raise NotADirectoryError(f"The path {dir} is not a directory.")

    # total_size will keep track of the total size, initialize it at 0 bytes
    total_size = 0
    # walk through each dir and subdirectory within a given directory
    for dirpath, dirnames, filenames in os.walk(dir):
        # loop through each file in the current dir
        for filename in filenames:
            # get the full path of the file by combining directory path and filename
            filepath = os.path.join(dirpath, filename)
            # add the size of the current file to the total
            total_size += os.path.getsize(filepath)

    # convert from bytes to megabytes    
    size_in_mb = total_size / (1024 * 1024)
    return size_in_mb 

def monitor_dir_size(dir, size_limit_mb, check_interval=5):
    # runs in an infinite loop, continuously monitoring the directory size
    while True:
        try:
            dir_size = get_dir_size(dir):
            print(f"Monitoring dir size... Directory size is: {dir_size: .2f} MB")

            if dir_size > size_limit_mb:
                # prints the current directory size in each iteration
                print(f"Alert: Directory size exceeded the limit of {size_limit_mb} MB!")
            
            # uses time.sleep() to pause between checks, avoiding excessive resource usage 
            time.sleep(check_interval)
        except (FileNotFoundError, NotADirectoryError) as e:
            print(f"There was an unexpected error: {e}")
            break

