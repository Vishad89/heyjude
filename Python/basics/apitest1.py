import json
import requests

r = requests.get("https://formulae.brew.sh/api/formula.json")
rj=r.json()

print(rj)
