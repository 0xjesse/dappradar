##script that returns top dapps by UAW
import requests

url = "https://api.dappradar.com/4tsxo4vuhotaojtl/dapps"

headers = {
    "X-BLOBR-KEY": "YMYWi7wXBuOwU2SFgoUeqHU3LftwZmPd"
}

params = {
    "page": 1,
    "resultsPerPage": 50
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()["results"]

    for dapp in data:
        print(f"Name: {dapp['name']}")
        print(f"Category: {dapp['categories']}")
        print("")

else:
    print(f"Error {response.status_code}: {response.text}")