#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

username=input("Ingresa el nombre de usuario:")
password = getpass()

response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth(username,password))
print('Response.status_code:'+ str(response.status_code))

if response.status_code == 200:
    print('Login exitoso :'+response.text)
