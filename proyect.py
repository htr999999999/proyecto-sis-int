

import googlemaps
import pprint
import time
from apikey import APIkeyas
#Definir API KEY
API_KEY = APIkeyas
import json

#Definir cliente

gmaps = googlemaps.Client(key= API_KEY)

#inputs de usuario
# palabrakey = input("¿Que quieres comer hoy?\n>")
# tipo_comida = input("¿Que tipo de comida quieres comer hoy?\n>")

# match tipo_comida: 
#     case 'fastfood':
#         tipo_comida = 'fastfood'
#         print(tipo_comida)
#     case _:
#         tipo_comida = 'No ha selecionado nada'
#         print(tipo_comida)
#         exit()
ubicaciones={
    "JESUS_MARIA" :"-12.0780894556, -77.0482420569",
    "SAN_JUAN_DE_LURIGANCHO": "-11.9459474278, -76.9714642367",
    "ANCON": "-11.702568503, -77.0958901385", 
    "SAN MIGUEL": "-12.0765987497, -77.0900896423"
}
i=-1
for key, values in ubicaciones.items():
    
    i+=1
    print(i,". ",key)


ubicacion = int(input("ingrese ubicacion:\n>"))
ubicacionUsar = list(ubicaciones.values())
# match ubicacion:
#     case 1:
#         ubicacion = 
# Definir busqueda

places_result = gmaps.places_nearby(location =ubicacionUsar[ubicacion] ,radius='5000', open_now = False, type='bank')  # type: ignore

# # pprint.pprint(places_result)0

# with open('data.json', 'w', encoding='utf8') as f:
#     for place in places_result['results']:
#         my_place_id = place['place_id']
#         my_fields = ['name','rating','vicinity', 'type']
#         place_details = gmaps.place(place_id = my_place_id, fields = my_fields)  # type: ignore
#         json.dump(place_details, f, indent=4, ensure_ascii=False)

with open('data.json', 'w', encoding='utf8') as f:
    # for place in places_result['results']:
    #     my_place_id = place['place_id']
    #     my_fields = ['name','rating','vicinity', 'type']
    #     place_details = gmaps.place(place_id = my_place_id, fields = my_fields)
    
    json.dump(places_result, f, indent=4, ensure_ascii=False)