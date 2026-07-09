import requests
# website ka name likhege jise hume test karna h 
target_url = "https://api.github.com"
# kuch alag alag path jo hume check karna h 
paths_to_test = ["/users","/orgs","/this-is-hidden","/secret-page"]
print(f"Scanning target: {target_url}\n")

# loop chalakar har path ko automatic test karenge
for path in paths_to_test:
    full_url = target_url + path
    response = requests.get(full_url)

    if response.status_code == 200:
        print(f" FOUND (2000 0k): {full_url}")
    elif response.status_code == 404:
        print(f" Not found (404): {full_url}")