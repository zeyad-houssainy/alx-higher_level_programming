a = input("First number...\n")
b = input("Second number...\n")
try:
    print(a/b)
except (ZeroDivisionError):
    print("You can't devide by zero...")
except (TypeError):
    print("Type error is here ༼ つ ◕_◕ ༽つ")
