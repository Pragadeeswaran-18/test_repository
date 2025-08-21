def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python arithmetic.py <add|sub|mul|div> <a> <b>")
        sys.exit(1)

    op, a, b = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
    if op == "add":
        print(add(a, b))
    elif op == "sub":
        print(subtract(a, b))
    elif op == "mul":
        print(multiply(a, b))
    elif op == "div":
        print(divide(a, b))
    else:
        print("Unknown operation. Use add, sub, mul, or div.")
        sys.exit(1)
