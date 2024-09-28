import requests

response = requests.get('https://api.adviceslip.com/advice')

if response.status_code == 200:
    data = response.json()
    print("Here's your advice of the day: ")
    print(f"'{data["slip"]["advice"]}'") 
else:
    print(f"Error: {response.status_code}")