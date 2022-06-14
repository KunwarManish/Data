# first we will display the options to user

while True:
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")
    print("Enter q or Q to Exit")

    choice = input("Enter your choice: ")

    if choice == 'q' or choice == "Q":
        break

    # user can enter number with decimal places
    num1 = float(input("Enter Number 1 : "))
    num2 = float(input("Enter Number 2 : "))

    if choice == "1":
        print(num1, "+", num2, "=", (num1 + num2))
    elif choice == "2":
        print(num1, "-", num2, "=", (num1 - num2))
    elif choice == "3":
        print(num1, "*", num2, "=", (num1 * num2))
    elif choice == "4":
        if num2 == 0.0:
            print("Divide by 0 Error")
        else:
            print(num1, "/", num2, "=", (num1 / num2))

    else:
        print("invalid choice")

    print()
