import os

path = "."  # current directory
items = os.listdir(path)

print(f"Contents of '{path}':")
for item in items:
    print(item)
