import requests

token = '421f9f851a5845cc1b3a4299dcda12dd'
host = 'https://pokemonbattle.me:9104'

answer_confirm = requests.post(f'{host}/pokemons', json = 
{
    "name": "generate",
    "photo": "generate"
}, headers = 
{
    "Content-Type" : "application/json", 
    "trainer_token" : token
    })

print(answer_confirm.text)

answer_confirm = requests.put(f'{host}/pokemons', json = 
{
    "pokemon_id": "12550",
    "name": "MaxDc",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers = 
{
    "Content-Type" : "application/json", 
    "trainer_token" : token
    })
    
print(answer_confirm.text)

answer_confirm = requests.post(f'{host}/trainers/add_pokeball', json = 
{
    "pokemon_id": "12550"
}, headers = 
{
    "Content-Type" : "application/json", 
    "trainer_token" : token
    })

print(answer_confirm.text)