import requests

BOT_TOKEN = "YOUR_BOT_TOKEN"

headers = {
    "Authorization": f"Bot {BOT_TOKEN}",
    "Content-Type": "application/json"
}

response = requests.get("https://discord.com/api/v10/users/@me/guilds", headers=headers)

if response.status_code == 200:
    guilds = response.json()
    for guild in guilds:
        print(f"Server Name: {guild['name']} | Server ID: {guild['id']}")
else:
    print(f"Error: {response.status_code} - {response.text}")
