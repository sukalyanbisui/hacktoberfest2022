from urllib import response
import requests

URL="https://sj-kumar.github.io/"

response = requests.get (URL)

print(response.json())
