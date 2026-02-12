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
cost = [0]
cups = [0]

def main():
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
              #add flavor chosen to a list
              size("regular")
          else:
              print("Invalid flavor")
        elif choice == "G":
          for flavor in flavors["gormet"]:
            print(flavor)
          thing = input("Which flavor? ").lower().strip()
          if thing in flavors["gormet"]:
              #add flavor chosen to a list
              size('gormet')
          else:
              print("Invalid flavor")
        elif choice == "C":
            checkout()
        elif choice == "Q":
            print("Exiting Program")
            done = False
def size(flavor):
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
    if thing in range (1,4):
        cost[0] += menu[flavor][thing-1]["p"]
    if thing == 1 and (flavor == "gormet" or flavor == "regular"):
        cups[0] += 1
    else:
        print("Invalid size")

main()