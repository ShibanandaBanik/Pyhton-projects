import time
import random
num = range(1,100)
numb = random.choice(num)
print("Welcome to the number guessing game.")
time.sleep(1)
print("The game will chose a number between 1 to 100 .")
print("You have to guess the correct number")
flag = True
while flag:
    inp = int(input("Enter your guessed number."))
    if inp > numb:
        print("Number too high.")
    elif inp < numb:
        print("Number too low.")
    else:
        print("You guessed the number! The number was ",numb)
        exit()