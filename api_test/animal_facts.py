import os
import requests
from dotenv import load_dotenv

load_dotenv()

url = "https://animals-by-api-ninjas.p.rapidapi.com/v1/animals"

user_animal_input = input("Enter the name of an animal: ")

print("Checking our zoo for", user_animal_input)

query_string = {"name" : user_animal_input}

api_key = os.getenv("RAPIDAPI_KEY")

headers = {
	"x-rapidapi-key": api_key,
	"x-rapidapi-host": "animals-by-api-ninjas.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=query_string)

# checks if response is successful, as in there's a hit on the animal they're looking for 
if response.status_code == 200:
    animals_data = response.json()
    # displays information about an animal, whether one or many, found in data
    def display_animal_info(animal):
        name = animal.get('name', 'Unknown animal')
        lifestyle = animal.get('characteristics', {}).get('lifestyle', 'unknown lifestyle').lower()
        locations = ', '.join(animal.get('locations', ['Unknown location']))
        diet = animal.get('characteristics', {}).get('diet', 'Unknown diet').lower()
        favorite_food = animal.get('characteristics', {}).get('favorite_food', 'Unknown food')

        print(f"\n- {name} is an animal that is primarily found in {locations}. They live a very {lifestyle} life. Their diet is {diet}, and they love {favorite_food}.\n")

    # handles if there's only one animal, else goes through the list
    def handle_animals_data(animals_data):
        if len(animals_data) == 1:
            print(f"Meet your new zoo friend: {animals_data[0]['name']}")
            display_animal_info(animals_data[0])
        else:
            print("Here are the details of the animals in your zoo:")
            for animal in animals_data:
                display_animal_info(animal)

    handle_animals_data(animals_data)

else:
    print(f"Failed to find the animal you're looking for. {response.status_code}. Try again, or try a different animal!")
