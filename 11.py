#imports
import random as rand 

#varaibles & lists
alive=True 
money = 10000
ending1 = False
ending2 = False
ending3 = False
ending4 = False
ending5 = False
ending6 = False
ending7 = False
ending8 = False
ending9 = False
ending10 = False
ending11 = False

def main():
    while alive:
        print("pre amble")
        print("")
        print("A - high roller/celebrity")
        print("B - mantinence crew")
        print("C - just win it gambling")
        print("D - completion percent")
        print("E - escape program")
        start=input(">").strip().upper()
        if start == "A":
            pro()
        elif start == "B":
            crew()
        elif start == "C":
            casino("else")
        elif start == "D":
            endings()
        elif start == "E":
            alive=False
        else:
            print("not a valid input")
        
def pro():
    print("")
    print("ramble")
    print("A - keep gambling")
    print("B - cheat")
    print("C - make it to the pro lounge")
    choice=input(">").strip().upper()
    if choice == "A":
        casino("pro")
    elif choice == "B":
        print("they caught you and got arrested")
        print("you died")
        main()
    elif choice == "C":
        lounge()
def crew():
    print("")
    print("ramble")
    print("A - cut off lights/power")
    print("B - sabatoage the cameras")
    print("C - hack their servers")
    choice=input(">").strip().upper()
    if choice == "A":
        print("the backups kicks in and you got found")
        print("you died")
        main()
    elif choice == "B":
        cams()
    elif choice == "C":
        hacking()
def casino(check):
    while money > 0
        print("welcome to the casino")
        print("you have", money,"$")
        bet=input("how much do you bet?")
        if bet is int:
            if bet < money or bet == money :
                gamble(bet)
            else:
                print("you dont have enough money")
        else:
            print("wront input, please type only a number")
        if  money > 99999:
            print("you win")
            ending10=True
            main()
    print("you loose")

def gamble(yikes):
    money=money-yikes
    luck=rand.randint(0,200)
    money=money+luck*yikes*.01
    print("you now have", money, "$")
def lounge():

def hacking():

def cams():

#execution

main()
    