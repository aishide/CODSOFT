while True:
    print("\n")
    print("Enter the numbers ")
    num1 = float(input("Enter the first number : "))
    num2 = float(input("Enter the second number : "))


    print(f"\nThe numbers are {num1} and {num2}. Choose the operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (x)")
    print("4. Division (/)")
    print("5. Remainder (%)")
    print("6. Exponent (^)")
    print("7. Exit (f)")

    result = input("Enter your choice ( + | - | x | / | % | ^ | f ) : ")

    if result == "+":
        print(f"The sum of {num1} and {num2} is {num1 + num2}")

    elif result == "-":
        print(f"The difference between {num1} and {num2} is {num1 - num2}")

    elif result == "x":
        print(f"The multiplication of {num1} and {num2} is {num1 * num2}")

    elif result == "/":
        if num2 != 0:
            print(f"The division of {num1} and {num2} is {num1 / num2}")
        else:
            print("We can't divide a number by zero.")

    elif result == "%":
        print(f"The remainder of {num1} and {num2} is {num1 % num2}")

    elif result == "^":
        print(f"{num1} to the power {num2} is {num1 ** num2}")

    elif result == "f":
        print("Thank you for using the calculator!")
        break

    else:
        print("Please choose a valid operation.")
