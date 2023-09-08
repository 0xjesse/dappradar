import requests

url = "https://api.dappradar.com/4tsxo4vuhotaojtl/dapps/top/uaw?top=50"
headers = {
  "X-BLOBR-KEY": "YMYWi7wXBuOwU2SFgoUeqHU3LftwZmPd"
}

response = requests.get(url, headers=headers)

data = response.json()
dapps = data['results']

# Sort dapps by UAW in descending order
dapps = sorted(dapps, key=lambda x: x['metrics']['uaw'], reverse=True)

for dapp in dapps:
    print("Name:", dapp['name'])
    print("Website:", dapp['website'])
    print("Chains:", ", ".join(dapp['chains']))
    print("UAW:", dapp['metrics']['uaw'])
    print()