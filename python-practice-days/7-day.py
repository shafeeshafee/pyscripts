import sys

if len(sys.argv) != 2:
    print("Error: Please provide exactly one filename!")
    sys.exit(1)

filename = sys.argv[1]

# validation for filename: check if the filename is not empty or only whitespace
if not filename.strip():
    print("Error: Filename cannot be empty.")
    sys.exit(1)


try:
    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, start = 1):
            print(f"{line_number} - {line.strip()}")
# if input file is not found
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    sys.exit(1)
# if they don't have permissions
except PermissionError:
    print(f"Error: Permission denied for file '{filename}'")
    sys.exit(1)
# if it's a directory instead of a file
except IsADirectoryError:
    print(f"Error: '{filename} is a directory. Enter only a filename.")
    sys.exit(1)
# any other error
except Exception as e:
    print(f"An unexpected error happened, sorry. More info: {e}")
    sys.exit(1)