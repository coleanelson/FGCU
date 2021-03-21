""""This is a Basic Calculator for Basic Mathematical Functions."""

__author__ = "Colby Nelson"

#If you want to show as a percent or dollar
# sign, change the last sep to the desired sign.

def addition(limit):
    # Addition
    print("Addition")
    total = 0
    for x in range(limit):
        number = float(input("Input number for addition then press enter: "))
        total += number
    print("Answer:", format(total, "0.2f"), sep='')
    print("\n")

def subtraction():
    # Subtraction
    print("Subtraction \n Program will take biggest number input. \n Will not generate negative numbers.")
    number = float(input("Input first number for subtraction then press enter: "))
    number2 = float(input("Input second number for subtraction then press enter: "))
    if number > number2:
        print("Answer:", format(number - number2, "0.2f"), sep='')
    else:
        print("Answer:", format(number2 - number, "0.2f"), sep='')
    print("\n")

def multiplication(limit):
    # Multiplication
    print("multiplication")
    total = 1
    for x in range(limit):
        number = float(input("Input number for multiplication then press enter: "))
        total *= number
    print("Answer:", format(total, "0.2f"), sep='')
    print("\n")

def division():
    # Division
    print("Division")
    number1 = float(input("Input the first number you want to have divided then press enter: "))
    number2 = float(input("Input the second number for the divisor then press enter: "))
    print("Answer:", format(number1 / number2, "0.2f"), sep='')
    print("\n")

def modulus():
    print("Remainder")
    num9 = float(input("Input the first number you want to have divided then press enter: "))
    num10 = float(input("Input the divisor then press enter: "))
    print("Remainder:", format(num9 % num10, ".2f"), sep='')
    print("\n")

def exponent():
    # Exponent
    print("Exponiential Power multiplier")
    num11 = int(input("Input the first number then press enter: "))
    num12 = int(input("Input the exponential power then press enter: "))
    print(num11, num12, sep='^')
    print("answer:", format(num11 ** num12), sep='')
    print("\n")

def floor_division():
    # Floor Division
    print("Rounding down whole number division")
    num13 = int(input("Input the number needing divided: "))
    num14 = int(input("Input the number to divided by: "))
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