import requests

url = "https://api.jsoning.com/mock/public/users"
response = requests.get(url)

if response.status_code == 200:
    users = response.json()
    print("Fetched Users:")
    for user in users:
        print(f"{user['firstname']} {user['lastname']} - {user['email']} - {user['city']}")
else:
    print("Failed to fetch data:", response.status_code)
