#imports
import random as rand 

#varaibles & lists
alive = True
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
pro = False

def main():
    global alive
    while alive:
        print("pre amble")
        print("")
        print("A - high roller/celebrity")
        print("B - mantinence crew")
        print("C - just win it gambling")
        print("D - completion percent")
        print("E - escape program")
        start = input(">").strip().upper()
        if start == "A":
            pro_route()
        elif start == "B":
            crew()
        elif start == "C":
            casino("else")
        elif start == "D":
            endings()
        elif start == "E":
            alive = False
        else:
            print("not a valid input")

def pro_route():
    # renamed from pro() to avoid clash with boolean 'pro'
    global pro
    print("")
    print("ramble")
    print("A - keep gambling")
    print("B - cheat")
    print("C - make it to the pro lounge")
    choice = input(">").strip().upper()
    if choice == "A":
        casino("pro")
    elif choice == "B":
        print("they caught you and got arrested")
        print("you died")
        return
    elif choice == "C":
        lounge()
    else:
        print("not a valid input")

def crew():
    print("")
    print("ramble")
    print("A - cut off lights/power")
    print("B - sabatoage the cameras")
    print("C - hack their servers")
    choice = input(">").strip().upper()
    if choice == "A":
        print("the backups kicks in and you got found")
        print("you died")
        return
    elif choice == "B":
        cams()
    elif choice == "C":
        hacking()
    else:
        print("not a valid input")

def casino(check):
    global money, pro, ending10
    while money > 0:
        print("welcome to the casino")
        print("you have", money, "$")
        bet_str = input("how much do you bet? ").strip()
        try:
            bet = int(bet_str)
        except ValueError:
            print("wrong input, please type only a number")
            continue
        if bet <= 0:
            print("bet must be positive")
            continue
        if bet <= money:
            gamble(bet)
        else:
            print("you dont have enough money")
        if money > 99999:
            if check == "pro":
                print("you are now a high roller")
                pro = True
                lounge()
                return
            print("you win")
            ending10 = True
            return
    print("you lose")
    return

def gamble(yikes):
    global money
    money = money - yikes
    luck = rand.randint(0,200)
    # winnings can be fractional; keep integer for currency
    winnings = int(luck * yikes * 0.01)
    money = money + winnings
    print("you now have", money, "$")

def lounge():
    global pro, ending11, ending4, ending7, ending1
    print("ramble")
    print("A - humility")
    print("B - vault")
    print("C - 2x cross")
    choice = input(">").strip().upper()
    if choice == "A":
        if pro:
            print("you manged to be the best of the best renound for all time")
            ending11 = True
        else:
            print("you decided that you did need all the money so you took a reduced cut and walked away a ghost")
            ending4 = True
    elif choice == "B":
        print("you found the vault and took all the money")
        ending7 = True
    elif choice == "C":
        print("they saw it coming all along more details cause this a bad ending")
        ending1 = True
    else:
        print("not a valid input")

def hacking():
    print("entering hacking")
    q1 = input("what casino are you hacking? ")
    if q1 == "Bellagio":
        print("passing")
        pass
    else:
        print("wrong answer")
        print("you died")
        return
    q2 = input("q2 ")
    if q2 == "a2":
        print("passing")
        pass
    else:
        print("wrong answer")
        print("you died")
        return
    q3 = input("q3? ")
    if q3 == "a3":
        print("passing")
        pass
    else:
        print("wrong answer")
        print("you died")
        return
    print("success entering console")
    console()

def cams():
    global ending9, ending6, ending3
    print("")
    print("ramble")
    print("A - quick and silent")
    print("B - take it all")
    print("C - deep fakes")
    choice = input(">").strip().upper()
    if choice == "A":
        print("nobody noticed you, the fake bills you replaced were found weeks after the heist. you got away clean")
        ending9 = True
        return
    elif choice == "B":
        print("seriously? you thought you could just take it all?")
        print("you got caught and arrested")
        ending6 = True
        return
    elif choice == "C":
        print("you made deep fakes of the security guards and cameras, you got away clean")
        print("though cesars palace was framed lol")
        ending3 = True
        return
    else:
        print("not a valid input")

def console():
    global ending2, ending5, ending8
    print("")
    print("ramble")
    print("A - transfer the funds to the chinese")
    print("B - wipe their crypto wallets")
    print("C - leak their files as blackmail")
    choice = input(">").strip().upper()
    if choice == "A":
        print("you transferred the funds successfully")
        print("now what . . .")
        ending2 = True
        return
    elif choice == "B":
        print("you managed to sucesfully steal 90 million in bit coin")
        ending5 = True
        return
    elif choice == "C":
        print("they gave you millions to keep secret but you still leaked it lol")
        ending8 = True
        return
    else:
        print("not a valid input")

def endings():
    # simple completion/summary. Not present originally -> minimal implementation.
    print("completion percent / endings achieved:")
    endings_list = [
        ending1, ending2, ending3, ending4, ending5,
        ending6, ending7, ending8, ending9, ending10, ending11
    ]
    achieved = sum(1 for e in endings_list if e)
    total = len(endings_list)
    print(f"{achieved}/{total} endings achieved")
    if achieved == 0:
        print("passing")

if __name__ == "__main__":
    main()
#
