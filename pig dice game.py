print()
print()

print("WELCOME TO THE PIG DICE GAME !!")

print()
print("INSTRUCTIONS:")
print("         1. This game is played between two players,A and B. ")
print("         2. Game starts with A asked to roll a dice.")
print("         3. The game will add the score of both the player one after one of the dice.")
print("         4. If any player got '1' on the die, his game will end and all his score become 0        .")
print("         5. Any player can anytime ends its chance by saying 'n' to roll the dice for the next chance.")
print("         6. After the game ends, the respective scores of both the players were use to declare the winner of the game.")
print("         7. The player with more score will won the match.")

print()

sum1=0

import random

print("Player A's turn")
ask1=input("start the game?(y/n): ")
if(ask1=="y"):
    
    print()

    while True:
        
        print("It's A's turn")

        die1=random.randint(1,6)
        print("you rolled : " , f"({die1})")
        
        if(die1 != 1):
            sum1+=die1
            print("sum of your rolled dice is:", sum1)

            print()

            ask2=input("roll again ? (y/n):")
            if(ask2=="y"):
                continue
            if(ask2=="n"):
                print()
                print("total sum of A rolled dice is:", sum1)
                print()
                break

        if(die1==1):
            sum1-=sum1
            print("sorry, you lose your chance .")
            break

print()
print()

sum2=0

import random

print("Now it's Player B's turn")
ask3=input("start the game?(y/n): ")
if(ask3=="y"):
    
    print()

    while True:
        
        die2=random.randint(1,6)
        print("you rolled : " , f"({die2})")
        
        if(die2 != 1):
            sum2+=die2
            print("sum of your rolled dice is:", sum2)

            print()

            ask4=input("roll again ? (y/n):")
            if(ask4=="y"):
                continue
            if(ask4=="n"):
                print()
                print("total sum of B rolled dice is:", sum2)
                print()
                break

        if(die2==1):
            sum2-=sum2
            print("sorry, you lose your chace.")
            break
            
print()

print("Score of A:",sum1 , ", Score of B:",sum2)

print()

if(sum1>sum2):
    print("A won the match")
elif(sum1==sum2):
    print("The match is draw")
else:
    print("B won the match")

print()
print()




