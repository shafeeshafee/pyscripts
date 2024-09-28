import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print("Please enter one filename.")
    sys.exit(1)

try:
    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, start = 1):
            print(f"{line_number} - {line.strip()}")
except FileNotFoundError:
    print(f"File '{filename}' not found.")