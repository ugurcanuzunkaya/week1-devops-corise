# Demo Calculator App For Week 1 Project
# Addition Method
def add(a, b):
    return a + b


# Subtract Method
def sub(a, b):
    return a - b


# Multiplication
def mul(a, b):
    return a * b


# Division
def div(a, b):
    return a / b


if __name__ == "__main__":
    # Declare variable and set default values
    a = 4
    b = 2
    print(f"Sum of {a} and {b} is ", add(a, b))
    print(f"Difference of {a} and {b} is ", sub(a, b))
    print(f"Product of {a} and {b} is ", mul(a, b))
    print(f"Division of {a} and {b} is ", div(a, b))
