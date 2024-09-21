def reverse_str(str):
    length_of_str = len(str)
    result = []
        
    for i in range(length_of_str):
       result.insert(0, str[i])

    return "".join(result) 

print(reverse_str("watermelon"))


