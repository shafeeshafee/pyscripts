# Create a Python function that accepts a list of numbers and returns the sum. Write a test function using pytest to verify it works correctly. 

# Output Example:

# Sum of [1, 2, 3, 4, 5] is 15

# Pytest Output Example:

# Test results:
# Test passed: Sum of [1, 2, 3] is 6
# Test passed: Sum of [] is 0
# Test passed: Sum of [-1, -2, -3] is -6

def sum_of(numlist):
    total = 0
    for num in numlist:
        total += num
    return total

print(sum_of([1,2,3]))