# Output Example: 

# Enter temperature in Fahrenheit: 98.6
# 98.6 Fahrenheit is 37.0 Celsius

def fahrenheit_to_celsius():
    fahrenheit = float(input("Enter the temperature in fahrenheit: "))
    celsius = ((fahrenheit - 32) * 5) / 9

    return f"{fahrenheit} in celsius is: {celsius}"

print(fahrenheit_to_celsius())