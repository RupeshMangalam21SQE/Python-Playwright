import json

# Read existing JSON
with open("users.json", "r") as file:
    users = json.load(file)

# Add a new user
new_user = {"name": "Alice", "email": "alice@example.com"}
users.append(new_user)

# Write updated list back
with open("users.json", "w") as file:
    json.dump(users, file, indent=4)

print("New user added!")
