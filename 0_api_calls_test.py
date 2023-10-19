import requests
import pprint

# key
ACCESS_KEY = "9036b7da90ca089457b0a4183d7579a1"
URL = f"http://apilayer.net/api/live?access_key={ACCESS_KEY}&currencies=EUR,GBP&source=USD"

response = requests.get(URL)

pprint.pprint(response.json())