import requests
response = requests.get("https://api.github.com")
if response.status_code == 200:
    # json means kisi bhi website ma sa specific data nikalana
    data = response.json()
    print("GitHub User API Link:", data["current_user_url"])

