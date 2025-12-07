import requests
from pprint import pprint

region= "americas"

#puuid= "Fer#001"

#endpoint_url = f"{base_url}/{endpoint}"

#Fer
#puuid= 'XDlnjfnpb1nEMEoZAr55Qi20inVfjMC_bZ9agsB7MviPYBoCBIWxfZSwKEkZ5T0-MTGSUV2RFTjjFg'
#webo
#puuid= 'MH3spPtKdtjdtua6cYFQolE3yD9ONd1NYk9zqKGHJmtMDj1opADNJVudMEew1ubQ3xLxYhBbMoRHxg #WEBO
#sebastian
#'puuid': 'TrGhO3YugrdBesYlgq67W-XSIvDBOTd09-cXhz0kaxwhuZO4a7haRq8uFy6OvSAIxwyyARLTV5UV7Q'

gameName="Fer"
tagLine="001"

url_base= f"https://{ region}.api.riotgames.com"
endpoint= f"riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}"
#endpoint= f"lol/match/v5/matches/by-puuid/{puuid}/ids"
url= f"{url_base}/{endpoint}"

api_key=""

headers = {
    "X-Riot-Token": api_key
}

responseUsuario= requests.get(url, headers=headers)

if responseUsuario.status_code == 200:
    usuario= responseUsuario.json()
    puuidUsuario= usuario['puuid']
    print(f"La peticion fue exitosa, Invocador: {usuario['gameName']}#{usuario['tagLine']}")
else:
    print("Error:", responseUsuario.status_code)


endpoint= f"lol/match/v5/matches/by-puuid/{puuidUsuario}/ids"
url= f"{url_base}/{endpoint}"


responseMatchs= requests.get(url, headers=headers)
if responseMatchs.status_code == 200:
    print(f"Partidas cargadas: {len(responseMatchs.json())}")
    listaMatchs=responseMatchs.json()
else:
    print("Error:", responseMatchs.status_code)


for matchs in listaMatchs:
    endpoint= f"lol/match/v5/matches/{matchs}"
    url= f"{url_base}/{endpoint}"
    responseMatch= requests.get(url, headers=headers)

    if responseMatch.status_code == 200:
        match1= responseMatch.json()
        listaParticipantes=match1['info']['participants']
        for jugador in listaParticipantes:
            if jugador['puuid'] == usuario['puuid']:
                print(f"gano: {jugador['win']}")
        

        
    else:
        print("Error:", responseMatch.status_code)
