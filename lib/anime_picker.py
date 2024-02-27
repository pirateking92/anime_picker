from random import choice
import requests
import json


response = requests.get("https://api.jikan.moe/v4/anime/1")

cowboy_bebop = response.json()

anime_dict = [
    {"Cowboy Bebop": 1}, {"Naruto": 20}, 
]

def choose_anime():


for key, value in sorted(cowboy_bebop.items()):
    print("Anime Title:")
    print(value['titles'][0]['title'])

for key, value in sorted(cowboy_bebop.items()):
    print("MAL URL:")
    print(value['url'])
# print(cowboy_bebop["data"])



# def jprint(obj):
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)

# jprint(cowboy_bebop.json())

# print("Enter the name of an anime:")

# anime_list = ['test', 'test2', 'test3']

# print(choice(anime_list))