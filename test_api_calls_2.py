import sys
import requests

myip="109.88.99.125"
request_url = f"https://ipinfo.io/{myip}/json"
response = requests.get(request_url)

if response.status_code >= 300:
    print(f"Error {response}")
    sys.exit(1)
    
# get result into a dictionary
result = response.json()

print(result)
print(f"{result['country']}/{result['region']}")