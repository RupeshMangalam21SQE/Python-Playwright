start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(f"Prime numbers between {start} and {end} are:")
for num in range(start, end + 1):
    if num < 2:
        continue
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num)
