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
    "regular": ["cheddar","chicago","blazing","kettle","dill"],
    "gormet": ["chocolate","churro","pink","vegas","matcha"],
}
treats_menu = { 
    "m&m": [{"s":"regular","p":6.0}, {"s":"large","p":12.0}],
    "nerds": [{"s":"regular","p":4.0}, {"s":"large","p":10.0}],
    "mints": [{"s":"regular","p":4.0}, {"s":"large","p":7.0}],
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
        print("T - treats/candy")
        print("C - Checkout and Quit")
        choice = input("Choice: ").upper().strip()
        if choice == "B":
            size("butter")
        elif choice == "T":
            treats()
        elif choice == "R":
            regular()
        elif choice == "G":
            gormet()
        elif choice == "C":
            checkout()
            done = True
        elif choice == "Q":
            print("Exiting Program")
            done = True


def size(flavor):
    global cost, cups, receipt
    i = 1
    if flavor == "butter":
        for item in menu["butter"]:
            print(i, ": ", item["s"], "-", item["p"], "$")
            i += 1
    elif flavor == "regular":
        for item in menu["regular"]:
            print(i, ": ", item["s"], "-", item["p"], "$")
            i += 1
    elif flavor == "gormet":
        for item in menu["gormet"]:
            print(i, ": ", item["s"], "-", item["p"], "$")
            i += 1
    thing = input("Which size? ").lower().strip()
    if thing in ["1", "2", "3", "4"]:
        price = menu[flavor][int(thing) - 1]["p"]
        cost += price
        receipt.append(f"{flavor} {menu[flavor][int(thing)-1]['s']} - ${price:.2f}")
        print("added to cart!")
        print("")
        if thing == "1" and (flavor == "gormet" or flavor == "regular"):
            cups += 1
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



def government(total):
    tax = round(total * 0.08, 2)
    total_after_tax = round(total + tax, 2)
    return tax, total_after_tax


def treats():
    global cost, receipt
    print("Treats available:")
    for candy in treats_menu:
        print("-", candy)
    thing = input("Which treat? ").lower().strip()
    if thing in treats_menu:
        i = 1
        for item in treats_menu[thing]:
            print(f"{i}: {item['s']} - ${item['p']}")
            i += 1
        sel = input("Which size? ").strip()
        if sel in ["1", "2"]:
            price = treats_menu[thing][int(sel)-1]["p"]
            cost += price
            receipt.append(f"{thing} {treats_menu[thing][int(sel)-1]['s']} - ${price:.2f}")
            print("added to cart!")
        else:
            print("Invalid size")
    else:
        print("Invalid treat")


def gormet():
    print("Gormet flavors:")
    for flavor in flavors["gormet"]:
        print("-", flavor)
    thing = input("Which flavor? ").lower().strip()
    if thing in flavors["gormet"]:
        size("gormet")
    else:
        print("Invalid flavor")


def regular():
    print("Regular flavors:")
    for flavor in flavors["regular"]:
        print("-", flavor)
    thing = input("Which flavor? ").lower().strip()
    if thing in flavors["regular"]:
        size("regular")
    else:
        print("Invalid flavor")


def complement():
    global cost
    if cost > 40:
        print("Please enjoy this complementary cup of popcorn or a bag of fresh butter popcorn")


def cupCount():
    global cups, cost
    while cups >= 3:
        print("Applying discount for 3 cups of popcorn")
        cost -= 2
        cups -= 3


def checkout():
    global cost, cups, receipt
    check = input("Are you sure you want to checkout? (Y/N) ").upper().strip()
    if check != "Y":
        print("Checkout canceled.")
        return

    print("Receipt:")
    for item in receipt:
        print(item)

    cupCount()
    complement()

    tax, total_after_tax = government(cost)

    print(f"Subtotal: ${cost:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total after tax: ${total_after_tax:.2f}")
    print("Thank you for shopping with us!")


if __name__ == "__main__":
    main()
