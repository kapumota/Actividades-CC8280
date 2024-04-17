#!/usr/bin/python

import urllib.request

print("Empezando la descarga....")

url="https://www.python.org/static/img/python-logo.png"

#download file with urlretrieve
urllib.request.urlretrieve(url, "python.png")

#download file with urlopen
with urllib.request.urlopen(url) as response:
    print("Estado:", response.status)
    print( "Descargando python.png")
    with open("python.png", "wb" ) as image:
        image.write(response.read())
