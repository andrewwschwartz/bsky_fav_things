import requests

username = "your_username"
endpoint = f"https://ggapp.io/{username}/games"

response = requests.get(endpoint)

if response.status_code == 200:
    games_data = response.json()
    # Process the games_data as needed
else:
    print(f"Error: {response.status_code}")