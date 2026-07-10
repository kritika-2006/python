import requests
url = input("Enter the url of the website:")
try:
    response = requests.get(url)

    if response.status_code == 200:
        print("Website is run smoothly")
    else:
        print("kuch gadbad h. server na status code {response.status_code} diya")
    
except:
    print("URL galat h ya internet band h!")