'''
Title: Restaurant
Author: Owen Chavanel
Description: navigate and checkout a menu
'''
menu = { 
    "butter": [{"s":"regular","p":4.0}, {"s":"3 gallon","p":7.0}, {"s":"5 gallon","p":12.0}, {"s":"25 gallon","p":55.0}], 
    "regular": [{"s":"cups","p":4.0}, {"s":"regular","p":6.0}, {"s":"large","p":10.0}, {"s":"5 gallon","p":40.0}], 
    "gormet": [{"s":"cups","p":4.0}, {"s":"regular","p":7.0}, {"s":"large","p":12.0}, {"s":"5 gallon","p":55.0}],
}
flavors = {
    "butter": ["butter"],
    "regular": ["chedder","chicago","blazing","kettle","dill"],
    "gormet": ["choclate","churro","pink","vegas","matcha"],
}

cost = 0.0
cups = 0
receipt = []


def main():
    global cost, cups, receipt
    done = False
    while not done:
        print("B - Butter")
        print("R - Regular")
        print("G - Gormet")
        print("C - Checkout and Quit")
        choice = input("Choice: ").upper().strip()
        if choice == "B":
            size("butter")
        elif choice == "R":
            for flavor in flavors["regular"]:
                print(flavor)
            thing = input("Which flavor? ").lower().strip()
            if thing in flavors["regular"]:
                size("regular")
            else:
                print("Invalid flavor")
        elif choice == "G":
            for flavor in flavors["gormet"]:
                print(flavor)
            thing = input("Which flavor? ").lower().strip()
            if thing in flavors["gormet"]:
                size("gormet")
            else:
                print("Invalid flavor")
        elif choice == "C":
            checkout()
            done = True
        elif choice == "Q":
            print("Exiting Program")
            done = True

def size(flavor):
    global cost, cups, receipt
    i=1
    if flavor == "butter":
     for item in menu["butter"]:
       print(i,": ",item["s"], "-", item["p"],"$")
       i+=1
    elif flavor == "regular":
      for item in menu["regular"]:
        print(i,": ",item["s"], "-", item["p"],"$")
        i+=1
    elif flavor == "gormet":
      for item in menu["gormet"]:
        print(i,": ",item["s"], "-", item["p"],"$")
        i+=1
    thing = input("Which size? ").lower().strip()
    if thing in ["1","2","3","4"]:
        cost += menu[flavor][int(thing)-1]["p"]
        receipt.append(f"{flavor} {menu[flavor][int(thing)-1]['s']} - ${menu[flavor][int(thing)-1]['p']:.2f}")
    else:
        print("Invalid size")
    if thing == "1" and (flavor == "gormet" or flavor == "regular"):
        cups += 1

def checkout():
    global cost, cups, receipt
    check = input("Are you sure you want to checkout? (Y/N) ").upper().strip()
    if check != "Y":
        print("Checkout canceled.")
        main()

    print("Receipt:")
    for item in receipt:
        print(item)

    while cups >= 3:
        print("Applying discount for 3 cups of popcorn")
        cost -= 2
        cups -= 3


    # complimentary item for orders over $40 (after discount)
    if cost > 40:
        print("Please enjoy this complementary cup of popcorn or a bag of fresh butter popcorn")

    tax = round(cost * 0.08, 2)
    total_after_tax = round(cost + tax, 2)

    print(f"Subtotal: $", cost)
    print(f"Tax: $", tax)
    print(f"Total after tax: $", total_after_tax)
    print("Thank you for shopping with us!")


main()
