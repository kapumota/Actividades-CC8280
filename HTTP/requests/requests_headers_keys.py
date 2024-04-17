import requests

if __name__ == "__main__":
    domain = input("Ingresa el hostname http://")
    response = requests.get("http://"+domain)
    for header in response.headers.keys():
        print(header  + ":" + response.headers[header])
