import requests

r = requests.get("https://www.bbc.co.uk/news")
print(r.status_code)
print(1+1)