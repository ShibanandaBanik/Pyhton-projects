while True:
    character = input("Enter any character from keyboard [type esc to exit]: ")
    if character.isalnum():
        if character.isalpha():
            if character.isupper():
                print(character,"is Upper Case Letter.")
            elif character.islower():
                print(character,"is Lower Case Letter")
        elif character.isdigit():
            print(character,"is a digit")
    else:
        print(character,"is a Special character.")
    if character == 'esc':
        break