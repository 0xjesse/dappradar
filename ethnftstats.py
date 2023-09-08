import requests

project = "4tsxo4vuhotaojtl"
url = "https://api.dappradar.com/" + project + "/nfts/marketplaces"

query = {
  "chain": "ethereum", ## can change this to other chains
  "range": "30d",
  "sort": "volume",
  "order": "desc",
  "page": "1",
  "resultsPerPage": "50"
}

headers = {"X-BLOBR-KEY": "Na2zmyqtD4fTibw4LzbWcFRVxsVirbrb"}

response = requests.get(url, headers=headers, params=query)

data = response.json() ## can use other library to present data in a more digestible way. see dapp.py, can specify chain there
print(data)