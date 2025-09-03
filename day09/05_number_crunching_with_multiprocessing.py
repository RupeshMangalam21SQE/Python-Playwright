from multiprocessing import Pool

# Function to find prime factors of a number
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

numbers = [123456, 987654, 67891, 1000003]

if __name__ == "__main__":
    with Pool() as pool:
        results = pool.map(prime_factors, numbers)
    for num, res in zip(numbers, results):
        print(f"Factors of {num}: {res}")
