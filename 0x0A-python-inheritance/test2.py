def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


try:
    result = divide_numbers(10, 0)
    print(result)
except ValueError as e:
    print(f"Error: {e}")
