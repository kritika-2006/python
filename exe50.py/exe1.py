import requests
response = requests.get("https://api.github.com/yeh-page-exist-nhi-karta")
print("Status code:",response.status_code)
print("\nWebsite Data:\n",response.text[:300])