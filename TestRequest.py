import requests

r = requests.get("https://www.instagram.com/")

print(r.status_code)
