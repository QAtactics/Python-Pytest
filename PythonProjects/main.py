import requests

token = 'токен'

response_trainer_reg = requests.post('https://pokemonbattle.me:9104//trainers/reg', 
                         headers = {'Content-Type' : 'application/json'}, 
json = {'trainer_token': token,
    "email": "почта",
    "password": "пароль"})

print(response_trainer_reg.json())

response_trainer = requests.post('https://pokemonbattle.me:9104/trainers/confirm_email', 
                         headers = {'Content-Type' : 'application/json'}, 
json = {'trainer_token': token,})

print(response_trainer.json())

response = requests.post('https://pokemonbattle.me:9104/pokemons', 
                         headers = {'Content-Type' : 'application/json', 'trainer_token': token,}, 
json = {'name': 'Бульбазавр', 'photo': 'https://dolnikov.ru/pokemons/albums/010.png'})

print(response.json())

response_re_name = requests.put('https://pokemonbattle.me:9104/pokemons', 
                         headers = {'Content-Type' : 'application/json', 'trainer_token': token,}, 
json = {'pokemon_id': 5973,'name': 'QAMACHINE'}) 

print(response_re_name.json())

response_add_pokemon = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', 
                         headers = {'Content-Type' : 'application/json', 'trainer_token': token,}, 
json = {'pokemon_id': 5973}) 

print(response_add_pokemon.json())
