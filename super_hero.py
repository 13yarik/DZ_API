import requests

def get_upload_link():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    data = requests.get(url).json()
    return data

characters = get_upload_link()

def find_character_by_name(characters, name):
    for character in characters:
        if character['name'] == name:
            return character

Hulk = find_character_by_name(characters, "Hulk")
Captain_America = find_character_by_name(characters, "Captain America")
Thanos = find_character_by_name(characters, "Thanos")

intelligence_Hulk = int(Hulk['powerstats']['intelligence'])
intelligence_Captain_America = int(Captain_America['powerstats']['intelligence'])
intelligence_Thanos = int(Thanos['powerstats']['intelligence'])

max_value_intelligence = max(intelligence_Hulk, intelligence_Captain_America, intelligence_Thanos)

if intelligence_Hulk > intelligence_Captain_America and intelligence_Hulk > intelligence_Thanos:
    print(f"Самый умный персонаж - Халк, его интеллект = {max_value_intelligence}")
elif intelligence_Captain_America > intelligence_Hulk and intelligence_Captain_America > intelligence_Thanos:
    print(f"Самый умный персонаж - Капитан Америка, его интеллект = {max_value_intelligence}")
elif intelligence_Thanos > intelligence_Hulk and intelligence_Thanos > intelligence_Captain_America:
    print(f"Самый умный персонаж - Танос, его интеллект = {max_value_intelligence}")
else:
    print(f"Есть персонажи с одинаковыми значениями интеллекта")



