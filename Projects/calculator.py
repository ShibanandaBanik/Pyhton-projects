flag = True


while flag:

    result1 = 1
    method = input("enter method [+,-,*,/,**,%] : ")
    flag = True
    result = 0

    if method == "+":
        while flag:
            sum_number = int(input("Enter number to add : "))
            result = result + sum_number
            if sum_number == 0:
                print("Your result is : ",result)
                break

    elif method == "*":
        while flag:
            multiplication = int(input("Enter number to multiply [type 1 to stop multiplication] : "))
            result1 = result1*multiplication
            if multiplication == 1:
                print("Your result is : ",result1)
                break

    #I did not do it like +,* beacuse if i did it doesn't work
    elif method == "-":
        while flag:
            subtract1 = int(input("Enter 1st number to subtract from : "))
            subtract2 = int(input("Enter 2nd number to subtract : "))
            result = subtract1 - subtract2
            print("Your result is : ",result)
            if subtract1 or subtract2 == 0:
                break

    elif method == "/":
        while flag:
            division1 = int(input("Enter first number to divide :"))
            division2 = int(input("Enter second number to divide :"))
            result = division1 / division2
            print("Your result is : ",result)

    elif method == "%":
        while flag:
            modulus1 = int(input("Enter first number to get modulus :"))
            modulus2 = int(input("Enter second number [type 0 to stop modulus] :"))
            result = modulus1 % modulus2
            print(result)
            if modulus1 or modulus2 == 0:
                break

    elif method == "**":
        while flag:
            power1 = int(input("Enter number :"))
            power2 = int(input("Enter number to power [type 0 to stop power] :"))
            result = power1 ** power2
            print("Your result is : ",result)
            if power1 or power2 == 0:
                break
    #when i put an invalid method it will say that \|/
    else:
        print("Syntax error try again")