import os

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

try:
    dir_size = get_dir_size('./test_dir')
    print(f"Directory size: {dir_size: .2f} MB")
except (FileNotFoundError, NotADirectoryError) as e:
    print(f"Error: {e}")