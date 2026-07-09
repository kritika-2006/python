import requests
# Hum check kar rahe hain ki kya admin page khula hai?
response = requests.get("https://github.com/admin")
if response.status_code == 200:
    print("Warning: Admin page found ")
elif response.status_code == 404:
    print("Safe: Admin page not found (404 not found)")
