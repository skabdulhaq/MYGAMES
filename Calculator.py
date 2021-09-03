import os
def clear():
    os.system('cls')

def add(n1, n2):
    return n1+n2


def sub(n1, n2):
    return n1-n2


def multiply(n1, n2):
    return n1*n2


def divide(n1, n2):
    return n1/n2


def power(n1, n2):
    return n1 ^ n2


def calculator():
    clear()
    operation = {
        "+": add,
        "-": sub,
        "*": multiply,
        "/": divide,
        "^": power, }
    num1 = float(input("What is your first number=> "))

    for operations in operation:
        print(operations)
    flag = True

    while flag:
        operation_function = (input("What operation do you want to do=> "))
        # x = operation_function
        # if not x=="+" or not x=="-" or not x=="/" or not x=="^" or not x=="*":
        #     print("invalid operation")
        #     return ""
        num2 = float(input("What is your next number=> "))

        calculation = operation[operation_function]
        answer = calculation(num1, num2)

        print(f"{num1} {operation_function} {num2} is equal to {answer}")

        con = input(f"Type 'y' to continue calculating with {answer} to restart calculation type 'n' \n to exit type anything \n")
        if con == 'y':
            num1 = answer
        elif con == 'n':
            calculator()
            clear()
        else:
            print("Thankyou for using my calculator")
            flag = False
calculator()
