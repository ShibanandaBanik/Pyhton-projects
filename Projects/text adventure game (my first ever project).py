import sys
import time
print("Welcome to the Journey of a teenager Text Adventure Game")
a = input("Enter Your Name : ")
print("Hello ",a)
print("It's 6.00 A.M. What should you do? Sleep or get up.")
time.sleep(1)
flag = True
while flag == True:
    b = input("If you want to sleep type Y or if you want to get up type N : ")
    if b == "Y":
        print("You did not want to get up.")
        print("As a result you woke up late and could not attend your classes.")
        sys.exit()
    elif b == "N":
        flag = False
        print("You woke up early. What should you do now?")
flag1 = True
while flag1 == True:
    c = str(input("If you want to brush your teeth type Y or if you want to have breakfast without brushing type N :"))
    if c == "Y":
        flag1 = False
        print("You brushed you teeth and started doing you due lessons")
        time.sleep(1)
        print("After that, I had breakfast and went out for school.")
    elif c == "N":
        flag1 = False
        print("At first you didn't want to brush your teeth.")
        print("But, then you thought that there will be bad smell coming from your mouth.")
        time.sleep(3)
        print("So, you brushed your teeth anyways and had breakfast. After that you went out for school.")        
flag2 = True
while flag2 == True:
    d = str(input("How do you want to go to school? By walking or by taking a rickshaw? if walk press Y if rickshaw press N : "))
    if d == "N":
        flag2 = False
        print("You wanted to go to your school by rickshaw. But, when you checked you pocket, you learnt that you have no money.")
        print("So, you started walking.")
        print("You reached your school in 6 minutes and attended all your classes. ")
        print("after that you returned home. What should you do?")
    elif d == "Y":
        flag2 = False
        print("Your school was not far from your home. So, you started walking")
        print("You reached your school in 6 minutes and attended all your classes.")
        time.sleep(3)
        print("After returning home, you took some rest now what should you do?")
flag3 = True
while flag3 == True:
    e = str(input("If you want to start studying type Y or want to play games type N : "))
    if e == "N":
        flag3 = False
        print("You played a lot of games. ")
        print("So, after having dinner your mother shouted at you for playing games and you went to bed like a bad boy.")
    elif e == "Y":
        flag3 = False
        print("You studied a lot and prepared your lessons. So, your mother was proud of you.")
        print("Afterwards, you had dinner and went to bed early like a good boy. :) ")
time.sleep(2)
print("ZzzzZzzz")
print("It's the next day. You woke up and remembered that last month you and your friends planned to go on a picnic this weekend.")
print("What should you do now?")
flag4 = True
while flag4 == True:
    f = input("If you want to go to picnic Type Y or if you want to stay at home type N : ")
    if f == "N":
        flag4 = False
        print("You spent your weekend in the home and could not enjoy the day. :(")
        sys.exit()
    elif f == "Y":
        flag4 = False
        print("You want to go to the picnic with your friends.")
        print("You got the permission of your parents and got ready.")
        time.sleep(1)
        print("You and your friends took a bus to the picnic place")
        print("What do you want to do? Sing or do nothing?")
flag5 = True
while flag5 == True:
    g = input("If you want to sing type Y or to stay calm and do nothing type N : ")
    if g == "N":
        flag5 = False
        print("You you spent the whole journey by bus doing nothing and got bored.")
    elif g == "Y":
        flag5 = False
        print("You and your friends sung a song and enjoyed the whole ride.")
print("You reached your destination on time.")
print("You guys enjoyed the picnic very much.")
print("Now it's time to return home")
time.sleep(4)
print("There is half an hour time left to return home. You wanted to buy a toy for your little sister.")
print("So, you went to a store and bought your little sister's favourite toys.")
print("But, you were too late. You and some other's lost the bus. The next bus will come an hour later.")
print("What should you do? Ask for a lift or wait?")
flag6 = True
while flag6 == True:
    h = input("If you want to wait type Y on if you you want to take a lift type N : ")
    if h == "N":
        flag6 = False
        print("You guys found a lift in 10 minutes and safely got back to home. :)")
    elif h == "Y":
        flag6 = False
        print("You guys waited for an hour and the bus arrived. You all got safely back to home.")
    time.sleep(2)
print("After returning home you feel very tired.")
print("Your parents wants to know about the journey and your late arrival")
print("What should you do? Tell them the story or sleep?")
flag7 = True
while flag7 == True:
    i = input("If you want to tell the story type Y or if you want to sleep type N : ")
    if i == "N":
        flag7 = False
        print('You said : "Mom, Dad Im very tired. I want to sleep"')
        print("You went to sleep.")
    elif i == "Y":
        flag7 = False
        print("You told the story to your parents and afterwards you went to sleep.")
time.sleep(2)
print("                        THANKS FOR PLAYING")
print("                         HOPE YOU ENJOYED")
print("                              Credits :")
print("                    A game by : Shibananda Banik")