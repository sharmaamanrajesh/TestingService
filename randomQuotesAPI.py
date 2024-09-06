import requests
import os

def get_quote():
  
    category = 'happiness'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    api_key = os.environ.get("API_KEY")
    response = requests.get(api_url, headers={'X-Api-Key': api_key})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)
    data = response.json()
    quote = data[0]["quote"]
    author = data[0]["author"]
    return f"{quote} - {author}"

print(get_quote())