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
    done = False
    while not done:
        print("B - Butter")
        print("R - Regular")
        print("G - Gormet")
        print("C - Checkout and Quit")
        print("Q - Quit without checkout")
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
    options = menu.get(flavor, [])
    if not options:
        print("No sizes available for that flavor.")
        return

    for i, item in enumerate(options, start=1):
        print(f"{i}: {item['s']} - ${item['p']:.2f}")

    try:
        choice = int(input("Which size? ").strip())
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if 1 <= choice <= len(options):
        item = options[choice - 1]
        price = float(item["p"])
        cost += price
        receipt.append(f"{flavor} {item['s']} - ${price:.2f}")
        print("Item added to cart")
        # count cups when the size is a cup option
        if "cup" in item["s"].lower():
            cups += 1
    else:
        print("Invalid size")

def checkout():
    global cost, cups, receipt
    check = input("Are you sure you want to checkout? (Y/N) ").upper().strip()
    if check != "Y":
        print("Checkout canceled.")
        main()

    print("Receipt:")
    for item in receipt:
        print(item)

    # apply discount: $2 off for every 4 cups
    discount = (cups // 4) * 2
    cost_after_discount = cost - discount
    if discount > 0:
        print(f"Bulk cups discount applied: -${discount:.2f}")

    # complimentary item for orders over $40 (after discount)
    if cost_after_discount > 40:
        print("Please enjoy this complementary cup of popcorn or a bag of fresh butter popcorn")

    tax = round(cost_after_discount * 0.08, 2)
    total_after_tax = round(cost_after_discount + tax, 2)

    print(f"Subtotal: ${cost_after_discount:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total after tax: ${total_after_tax:.2f}")
    print("Thank you for shopping with us!")

if __name__ == "__main__":
    main()
