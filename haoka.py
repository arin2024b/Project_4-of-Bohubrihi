import random

randomNum = random.randint(1,50)
# print(randomNum)
countAttempt = 0

while(countAttempt<6):
    
    if(countAttempt==5):
        print("Your Chances are Over,Please Try Again Later")
        break
        
    user_input = int(input("Enter Your Guessing Number :"))
    
    if(user_input>=1 and user_input<=50):
        if(user_input==randomNum):
            print("You got a correct guess and It's: ",user_input)
            print("You've already taken ",countAttempt+1," chance or chances to guess the correct number")
            break
        else:
            if(user_input<randomNum):
                print("You Guessed Lower,Try To Guess Higer Number")
            elif(user_input>randomNum):
                print("You Guessed Higher,Try To Guess Lower Number")
    else:
        print("Your Guessed Number Is Out Of Range,Please Give A Number Between 1-50")

    if (countAttempt == 0):
        print('You Got Your 1st Chance')
    elif (countAttempt == 1):
        print('You Got Your 2nd Chance')
    elif (countAttempt == 2):
        print('You Got Your 3rd Chance')
    elif (countAttempt == 3):
        print('You Got Your 4th Chance')
    elif (countAttempt == 4):
        print('You Got Your 5th And Last Chance')

    countAttempt+=1
