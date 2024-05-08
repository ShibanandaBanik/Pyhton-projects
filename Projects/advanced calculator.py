# mathematical calcultor
import math

print("Welcome to a calculator created with python.")

while True:
    operation = input("Enter operations [+, -, *, / , %, **, log, round, sqrt, abs, pi (0. Exit)]: ")

    result = 0
    mul_result = 1

    #The main calculator
    if operation == "+":
        while True:
            num = int(input("Number for addition: "))
            result = result + num
            if num == 0:
                print(f"This is your result {result}")
                break

    elif operation == "-":
        num1 = int(input("Number to subtract from: "))
        while True:
            num2 = int(input("Number to subtract [00 to exit]: "))
            num1 = num1-num2
            if num2 == 00:
                print(f"The result is {num1}")
                break

    elif operation == "*":
        while True:
            num = int(input("Number to multiply [0 to exit]: "))
            mul_result = mul_result * num
            if num == 0:
                print(f"The result is {mul_result}")
                break
    
    elif operation == "/":
        num1 = int(input("Number to divide from: "))
        while True:
            num2 = int(input("Number to divide [1 to exit]:"))
            num1 = num1 / num2
            print(f"Result = {num1}")
            if num2 == 1:
                break
### Here res means result
    elif operation == "%":
        while True:
            num1 = int(input("Number to get modulus from (enter 1 two times to exit): "))
            num2 = int(input("Enter number:"))
            res = num1 % num2
            print(f"Result = {res}")
            if num1 and num2 == 1:
                break

    elif operation == "**":
        num1 = int(input("Number to get the power of: "))
        while True:
            num2 = int(input("Enter power [enter 1 to exit]: "))
            num1 = num1 ** num2
            print(f"Result = {num1}")
            if num2 == 1:
                break

    elif operation == "log":
        print()
        print("1. Natural Logarithm")
        print("2. Logarithm with a second argument to specify the base.")
        log_input = int(input("Enter chocice:"))
        while True:
            if log_input == 1:
                log = int(input("Number to get the log of [enter 1 to exit]: "))
                res1 = math.log(log)
                print(f"Result = {res1}")
                if log == 1:
                    break
            elif log_input == 2:
                log = int(input('Enter base [enter 1 two times to exit]: '))
                log1 = int(input("Enter second argument: "))
                if log and log1 == 1:
                    break
                res1 = math.log(log1,log)
                print(f"Result = {res1}")
                
        
    elif operation == "round":
        while True:
            round_num = float(input("Enter float number to round [enter 1 to exit]: "))
            res = round(round_num)
            if round_num == 1:
                break
            print(f"Result = {res}")

    elif operation == "sqrt":
        while True:
            num = int(input("Number to square root [enter 1 to exit]: "))
            res = math.sqrt(num)
            print(f"Result = {res}")
            if num == 1:
                break

    elif operation == "abs":
        while True:
            num = int(input("Enter negative number to absolute [enter 1 to exit]: "))
            res = abs(num)
            print(f"Result = {res}")
            if num == 1:
                break

    elif operation == "pi":
        while True:
            print()
            print("1. Get the value of pi.")
            print("2. Multiply number with pi.")
            print("0. Exit")
            pi_num = int(input("Enter choice: "))
            if pi_num == 1:
                res = math.pi
                print(f"Result = {res}")
            elif pi_num == 2:
                num = int(input("Enter number: "))
                pi = math.pi
                num = num * pi
                print(f"Result = {num}")
                break
            elif pi_num == 0:
                break
    elif operation == 0:
        break