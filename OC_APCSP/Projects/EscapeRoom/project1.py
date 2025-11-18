#add varibles lists and imports here
import random
import time
RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
RESET = '\033[0m'
def GT(text):
  return GREEN + text + RESET
def RT(text):
  return RED + text + RESET
def BT(text):
  return BLUE + text + RESET
def tw(text):
  for char in text:
    print(char,end="", flush=True)
    time.sleep(.005)
hints=1
act=1
life=3
codes = ['soap','boom','split','fight','club','plane','hotel']
code=random.choice(codes).upper()
free=False
#while True: #indent all of the code at the end
tw( '''
you wake up in a private casino wait room. you can tell because 
youve been in many similar to this one. your hands are tied behind 
you with fluffy hand cuffs. the only other exit in the room is a door 
guarded by a burley bald man in a tuxedo and sunglasses you 
go up to him but he only says one thing

Guard: What is the pascode 

you can do a few things
''')
tw(BT("CHECK")+": look around the room and see if anything can help you" )
print("")
tw(BT('CHAT')+': talk to the gaurd') 
print("")
tw(BT('CODE')+': guess the code') 
print("")

while life > 0:
  while act!=3:
    chance=random.randint(0,100)
    print("")
    ui=input(RESET+">").upper().strip()
    if ui == 'CHECK':
      tw('''
      you look around the room. there is a ''' + BT("DECK") + ''' of cards on the table and 
      a empty'''+ BT('GLASS')+ '''of somthing that smells like whiskey. The ''' + BT('COUCH') + '''you woke
      up on has sewn down cushions.  
      *input BACK to go back* (does not actually do anything but by typing it there is an error and sends you to the start)
            ''')
      ui=input("CHECK>").upper().strip()
      if ui=='GLASS':
        tw("when you smell the glasses there is a strong pungent whiff of alchol.")
        tw("but there is also a smell of blood, and then the memorires come back to you")
        tw("the reletnless fights in the basments, the greatest sense of freedom")
        tw("It's only after we've lost everything that we're free to do anything")
      elif ui=='DECK':
        if free==False:
          if chance>75:
            tw("you flip through the deck and you find half a sticky note that says:")
            tw("Code:"+ GREEN+code[0:2])
          else:
            tw("you fuble through the deck but can't open it with your hands tied")
        else:
          tw("you flip through the deck and you find half a sticky note that says:")
          tw("Code:"+ GREEN+code[0:2])
      elif ui=='COUCH':
        if free==False:
          if chance>95:
            tw("you mange to search through the couch and find half a sticky note that says")
            tw("Code:"+ GREEN+code[2:len(code)])
          else:
            tw("you sit down on the couch stil in your cuffs")
        else:
          tw("you mange to search through the couch and find half a sticky note that says")
          tw("Code:"+ GREEN+code[2:len(code)])
      else:
        tw('that might be a typo')    
    elif ui == "ESCAPE":
      if hints==0:
        tw('you dont have any hints to escape at the momment')
      else:
        tw('you manage to break out of your cuffs')
        free=True
    elif ui == 'HINT':
      if hints==0:
        tw("you dont have any HINTS/SKILLS")
      else: 
        if act==1:
          tw("you can use a HINT/SKILL to break out of your cuffs by typing ESCAPE")
          tw("you can try the same task serval times if you are still in cuffs")
          tw("the capitlized words in CHECK are actions that can be used")
          hints=hints-1
          print("you have", hints, "HINTS/SKILLS left")
    elif ui=='CHAT':
      if act==1:
        tw("the gaurd does not respond to any of your remarks")
        tw('*hint* type HINT to use a skill pt to make something eaiser')
      else: 
        tw("the gaurds says back to you, 'glad to see that you are coming to your senses tyler'.")
        print("")
        tw("but your name isnt tyler; regarless the guard asks you one last quetion: ")
        print("")
        tw("so tyler if you want to leave all i need to know is what the 1st rule is.")
    elif ui=='CODE':
      if act==1:
        print('you have', life ,'tries to get the code')
        ui=input(RESET+"CODE: ").upper()
        if ui==code:
          tw('so it is you boss good to hear it')
          act=act+1
          free=True
          tw(' welcome to act 2')
        else:
          tw('that was wrong')
          life=life-1
          if life==0:
            break
          print("you have",life,"tries left")
      elif act==2:
        tw("so what is the rule?")
        ui=input(RESET+"1st Rule: ").upper().strip()
        if ui=="DON'T TALK ABOUT FIGHT CLUB" or ui=="DO NOT TALK ABOUT FIGHT CLUB" or ui=="DO NOT TALK ABOUT THE FIGHT CLUB":
          tw('Thats right boss now lets go explode some bombs.')
          act=act+1
          tw('welcome to act 3')
        else:
          tw('that was wrong')
          life=life-1
          print("you have",life,"tries left")
    else:
      tw('that might be a typo please use capitialization')   
  #act 3
  secret = random.randint(1 ,16)
  while life>0:
    print("")
    print('only type numbers btw . . ')
    guess = int(input("HOW MANY BOMBS ARE THERE: "))
    if guess == secret:
      tw("then lets blow up them banks tyler")
      tw("")
      tw("you escaped and manegde to realise the you are actually tyler durden")
      tw("this was based on fight club btw I hope you had fun")
      tw("but you know how it end so . . . ")
      break
    else: 
      tw("thats wrong try again")
      life=life-1
      print(life," guess left")
      if guess > secret:
        tw("hint: you are too big")
      else:
        tw("hint: you are too small")
  break
tw('you died')