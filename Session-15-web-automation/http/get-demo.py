import requests

BASE_URL="https://books.toscrape.com/"

response= requests.get(BASE_URL)

print(response.status_code)
print(response.text[:500])