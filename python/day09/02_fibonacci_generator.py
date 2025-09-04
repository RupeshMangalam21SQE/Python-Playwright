# Generator for Fibonacci sequence
def fibonacci():
    a, b = 0, 1
    while True:  # Infinite generator
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):  # Print first 10 Fibonacci numbers
    print(next(fib))
