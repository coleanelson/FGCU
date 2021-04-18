""""This is a Basic Calculator for Basic Mathematical Functions."""

__author__ = "Colby Nelson"

#If you want to show as a percent or dollar
# sign, change the last sep to the desired sign.

def addition(limit):
    """This is a basic calculator for addition. The user should have a basic understanding of math to use this."""
    # Addition
    print("Addition")
    total = 0
    for x in range(limit):
        while True:
            try:
                number = float(input("Input number for addition then press enter: "))
                break
            except ValueError:
                print("ERROR!!!! Must enter a number")
        total += number
    print("Answer:", format(total, "0.2f"), sep='')
    print("\n")

def subtraction():
    # Subtraction
    print("Subtraction \n Program will take biggest number input. \n Will not generate negative numbers.")
    while True:
        try:
            number = float(input("Input number for subtraction then press enter: "))
            break
        except ValueError:
            print("ERROR!!!! Must enter a number")
    while True:
        try:
            number2 = float(input("Input number for subtraction then press enter: "))
            break
        except ValueError:
            print("ERROR!!!! Must enter a number")
    if number > number2:
        print("Answer:", format(number - number2, "0.2f"), sep='')
    else:
        print("Answer:", format(number2 - number, "0.2f"), sep='')
    print("\n")

def multiplication(limit):
    """This is a basic calculator for multiplication. The user should have a basic understanding of math to use this."""
    # Multiplication
    print("multiplication")
    total = 1
    for x in range(limit):
        while True:
            try:
                number = float(input("Input number for multiplication then press enter: "))
                break
            except ValueError:
                print("ERROR!!!! Must enter a number")
        total *= number
    print("Answer:", format(total, "0.2f"), sep='')
    print("\n")

def division():
    """This is a basic calculator for division. The user should have a basic understanding of math to use this."""
    # Division
    print("Division")
    while True:
        try:
            number1 = float(input("Input the divisible number then press enter: "))
            break
        except ValueError:
            print("ERROR!!!! Must enter a number")
    while True:
        try:
            number2 = float(input("Input number for divisor then press enter: "))
            break
        except ValueError:
            print("ERROR!!!! Must enter a number")
    print("Answer:", format(number1 / number2, "0.2f"), sep='')
    print("\n")

def modulus():
    """This is a basic calculator for finding the remainder. The user should have a basic understanding of math to use this."""
    print("Remainder")
    while True:
        try:
            num9 = float(input("Input the first number you want to have divided then press enter: "))
            break
        except ValueError:
            print("ERROR!!!! Must enter a number")
    while True:
        try:
            num10 = float(input("Input the divisor then press enter: "))
            break
        except ValueError:
            print("ERROR!!!! Must enter a number")
    print("Remainder:", format(num9 % num10, ".2f"), sep='')
    print("\n")

def exponent():
    """This is a basic calculator for finding the exponiential Power. The user should have a basic understanding of math to use this."""
    # Exponent
    print("Exponiential Power multiplier")
    while True:
        try:
            num11 = int(input("Input the first number then press enter: "))
            break
        except ValueError:
            print("ERROR!!!! Must enter a number")
    while True:
        try:
            num12 = int(input("Input the exponential power then press enter: "))
            break
        except ValueError:
            print("ERROR!!!! Must enter a number")
    print(num11, num12, sep='^')
    print("answer:", format(num11 ** num12), sep='')
    print("\n")

def floor_division():
    """Rounding down division"""
    # Floor Division
    print("Rounding down whole number division")
    while True:
        try:
            num13 = int(input("Input the number needing divided: "))
            break
        except ValueError:
            print("ERROR!!!! Must enter a number")
    while True:
        try:
            num14 = int(input("Input the number to divided by: "))
            break
        except ValueError:
            print("ERROR!!!! Must enter a number")
    print(num13, num14, sep='/')
    print("answer:", num13 // num14, sep='')
    print("\n")

def main():
    print("The program goes through addition," + " subtraction," + " multiplication," + " division," + " modulus," + " exponent," + " and floor division", sep=' ')
    user_continue = "x"

    while user_continue != "~" or user_choice != "`":
        print(" 1 = addition \n 2 = subtraction \n 3 = multiplication \n 4 = division \n 5 = remainder \n 6 = exponential powers \n 7 = floor division or rounding the number down, to the nearest whole number \n ~ = end program ")
        user_choice = int(input("Enter correlating number to the problem you want to solve and press enter: "))
        if not (user_choice <=7 and user_choice >= 1):
            print("INVALID INPUT!")

        elif user_choice == 1:
            # Addition
            addition_limit = int(input("How many number sets do you want to add? Then press enter: "))
            addition(addition_limit)
            user_continue = str(input("Press any key to keep using, or press ~ or ` to stop then press enter: "))

        elif user_choice == 2:
            # Subtraction
            subtraction()
            user_continue = str(input("Press any key to keep using, or press ~ or ` to stop then press enter: "))

        elif user_choice == 3:
            # Multiplication
            multiplication_limit = int(input("How many numbers sets do you want to multiply together? then press enter: "))
            multiplication(multiplication_limit)
            user_continue = str(input("Press any key to keep using, or press ~ or ` to stop then press enter:"))

        elif user_choice == 4:
            # Division
            division()
            user_continue = str(input("Press any key to keep using, or press ~ or ` to stop then press enter: "))

        elif user_choice == 5:
            # Modulus
            modulus()
            user_continue = str(input("Press any key to keep using, or press ~ or ` to stop then press enter: "))

        elif user_choice == 6:
            # Exponent
            exponent()
            user_continue = str(input("Press any key to keep using, or press ~ or ` to stop then press enter: "))

        else:
            # Floor Division
            floor_division()
            user_continue = str(input("Press any key to keep using, or press ~ or ` to stop then press enter: "))

    print("Thank you for using my calculator", end='!')

main()