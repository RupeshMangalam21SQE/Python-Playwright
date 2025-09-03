def robust_division(a, b):
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except ValueError:
        return "Error: Invalid input, please enter numbers only"

# Test Runs
print(robust_division(10, 2))    # 5.0
print(robust_division(10, 0))    # Error: Cannot divide by zero
print(robust_division("a", 2))   # Error: Invalid input
