import requests

url = "https://api.dappradar.com/4tsxo4vuhotaojtl/dapps"

headers = {
    "X-BLOBR-KEY": "MLwhRAntZUFfVFh75cxtQ1iL5Loqmsqw"
}

params = {
    "page": 11,
    "resultsPerPage": 50
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()["results"]

    for dapp in data:
        print(f"Dapp ID: {dapp['dappId']}")
        print(f"Name: {dapp['name']}")
        print(f"Description: {dapp['description']}")
        print(f"Full Description: {dapp['fullDescription']}")
        print(f"Logo: {dapp['logo']}")
        print(f"Link: {dapp['link']}")
        print(f"Website: {dapp['website']}")
        print(f"Chains: {dapp['chains']}")
        print(f"Categories: {dapp['categories']}")
        print("Social Links:")
        for link in dapp['socialLinks']:
            print(f"    Title: {link['title']}")
            print(f"    URL: {link['url']}")
            print(f"    Type: {link['type']}")
        print("")

else:
    print(f"Error {response.status_code}: {response.text}")