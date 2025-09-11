# Reads a file, converts text to uppercase, writes to a new file
with open("input.txt", "r") as infile:
    content = infile.read()

with open("output.txt", "w") as outfile:
    outfile.write(content.upper())

print("Conversion complete! Check output.txt")
