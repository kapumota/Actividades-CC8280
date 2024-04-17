#!/usr/bin/env python3

import requests, json


domain = input("Ingresa el hostname http://")

response = requests.get("http://"+domain)

print(response.json)

print("Status codigo: "+str(response.status_code))

print("Headers respuesta: ")
for header, value in response.headers.items():
  print(header, '-->', value)
  
print("Solicitud headers  : ")
for header, value in response.request.headers.items():
  print(header, '-->', value)
