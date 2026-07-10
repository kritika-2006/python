import requests # Toolbox mangaya
# Python ko bola ki is website par jao aur data lekar aao (GET request)
response = requests.get("https://api.github.com")
# Check karte hain ki website ne data diya ya gussa ho gayi (Status Code 200 matlab OK)
print("Status Code:",response.status_code)
# Us website ke andar kya text/data hai, use thoda sa print karke dekhte hain
print("\nWebsite Data:\n",response.text[:300]) # Sirf shuruat ka 300 characters dikhane ke liye
