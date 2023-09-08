import json
import csv

# Load JSON data from file or source
json_data = """
[
    {
        "Dapp ID": 3,
        "Name": "CryptoKitties",
        "Description": "In CryptoKitties, users collect and breed oh-so-ad",
        "Full Description": "<p>In CryptoKitties, users collect and breed oh-so-adorable creatures that we call CryptoKitties! Each kitty has a unique genome that defines its appearance and traits. Players can breed their kitties to create new furry friends and unlock rare cattributes.</p>",
        "Logo": "https://dashboard-assets.dappradar.com/document/3/cryptokitties-dapp-games-eth-logo_43af8137d6219e1fd08b52d9cdfc9447.png",
        "Link": "https://dappradar.com/ethereum/games/cryptokitties",
        "Website": "https://www.cryptokitties.co",
        "Chains": ["ethereum"],
        "Categories": ["games"],
        "Social Links": [
            {"Title": "discord", "URL": "https://discord.gg/3GvT66U", "Type": "discord"},
            {"Title": "facebook", "URL": "https://www.facebook.com/CryptoKitties/", "Type": "facebook"},
            {"Title": "instagram", "URL": "https://www.instagram.com/cryptokitties/", "Type": "instagram"},
            {"Title": "medium", "URL": "https://medium.com/cryptokitties", "Type": "medium"},
            {"Title": "other", "URL": "https://www.cryptokitties.co/blog/", "Type": "other"},
            {"Title": "reddit", "URL": "https://www.reddit.com/r/CryptoKitties/", "Type": "reddit"},
            {"Title": "twitter", "URL": "https://twitter.com/cryptokitties", "Type": "twitter"},
            {"Title": "youtube", "URL": "https://www.youtube.com/channel/UClUgQBJcxAmHjOQgV4QgVXg", "Type": "youtube"}
        ]
    }
]
"""
data = json.loads(json_data)

# Define the output CSV file
csv_file = "output.csv"

# Define the header for the CSV file
header = ["Dapp ID", "Name", "Description", "Full Description", "Logo", "Link", "Website", "Chains", "Categories", "Social Links"]

# Open the CSV file for writing
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row to the CSV file
    writer.writerow(header)

    # Loop through each JSON object in the data list
    for obj in data:

        # Extract the values for each field
        dapp_id = obj.get("Dapp ID")
        name = obj.get("Name")
        description = obj.get("Description")
        full_description = obj.get("Full Description")
        logo = obj.get("Logo")
        link = obj.get("Link")
        website = obj.get("Website")
        chains = ",".join(obj.get("Chains", []))
        categories = ",".join(obj.get("Categories", []))
        social_links = ",".join([f"{link['Title']}: {link['URL']}" for link in obj.get("Social Links", [])])

        # Write data as a row in the CSV file
        writer.writerow([dapp_id, name, description, full_description, logo, link, website, chains, categories, social_links])