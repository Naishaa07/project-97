import random

no = random.randint(1,9)

chances=0
while(chances<5):
    chances=chances+1
    userNo= int(input("Pls enter a no. between 1 and 9"))
    if(no==userNo):
         print("You guessed the correct no.")
         no = random.randint(1,9)
         chances=0
    elif (chances==5):
        print("The correct answer is-")
        print(no)
        no = random.randint(1,9)
        chances=0
    else :
         print("Oops! Wrong answer")
         if(no-userNo>0):
             print("the correct answer is greater")
         else:
             print("the correct answer is smaller")
