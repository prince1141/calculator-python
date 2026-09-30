def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("=== Simple Calculator ===")
    while True:
        print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "5":
            print("Goodbye!")
            break
        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice, try again.")
            continue

        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        if choice == "1":
            print("Result:", add(a, b))
        elif choice == "2":
            print("Result:", subtract(a, b))
        elif choice == "3":
            print("Result:", multiply(a, b))
        else:
            print("Result:", divide(a, b))


if __name__ == "__main__":
    main()
