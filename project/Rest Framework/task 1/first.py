import requests


response = requests.get("https://official-joke-api.appspot.com/random_joke")


if response.status_code == 200:
   
    joke = response.json()
    print(f"Here's a joke for you:\n{joke['setup']}\n{joke['punchline']}")
else:
    print("Sorry, couldn't fetch a joke at the moment.")
