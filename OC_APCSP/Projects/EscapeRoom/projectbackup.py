#my project is being weird so im making this as a back up. no fancy lore or anything 
import random
life=10
hint=3
code=random.randint(1,20)
passwords=['apple','banana','cherry','date','fig','grape','kiwi','lemon','mango','nectarine']
pasword=random.choice(passwords)
print('''beofre you enter the room they tell you she is a crazy killer 
      then you enter and its just a litle girl in a toy room. she stares at you
      lets play three games and if you win you can leave. OR ELSE ''')
print("now. . . i like fruit")
#password game
while life > 0:
    ui = input("what is my favorite fruit?")
    if ui == pasword:
        print("you guessed the fruit")
        break
    elif ui in passwords:
        passwords.remove(ui)
        print("wrong fruit, try:")
        print(passwords)
        life-=1
        print("you have "+str(life)+" lives left")
    else:
        print("error: not a valid fruit")
else:
    print("you ran out of lives, the fruit was "+pasword)
    exit()
print("you win game 1 now:")
#riddle game
while life > 0:
    ui=input("What is the answer to this question?")
    if ui=="What":
        print("you guessed right")
        break
    else:
        print("no thats wrong ")
        life-=1
        print("you have "+str(life)+" lives left")
else:
    print("you ran out of lives, the answe was 'What'")
    exit()
print("you win game 2 now:")
#number game
while life > 0:
    ui=int(input("guess a number between 1 and 20: "))
    if ui==code:
        print("you guessed the number")
        break
    elif ui<code:
        print("too low")
        life-=1
        print("you have "+str(life)+" lives left")
    elif ui>code:
        print("too high")
        life-=1
        print("you have "+str(life)+" lives left")
    else:
        print("error")
else:
    print("you ran out of lives, the number was "+str(code))
    exit()
print("you win bye bye freind ")
print('''you walk out of the room and as you do you feel very tired
      sudennly you fall to the floor as the room around you begins to grow
      the little girl comes to pick you. youve become her new stuffed animal
      yay now i can add you with the rest of my collection''')