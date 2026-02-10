'''
Title: Trivia
Author: Owen Chavanel
Description: 
Let's create a trivia game.

1. Include an appropriate title, name of yourself, and a description for your
program as comments and as output for the user to see.
2. Ask the user for their name.
3. Trivia Game consists of at least 3 categories and 10 questions and
answers stored in dictionaries.
4. In the main function, create a menu with the following options:

S - Start Game
D - Display Scores
Q - Quit Game

5. At the end of the game, print the % of correct answers. Save the name of
the player and their score to a dictionary. When the user selects Display
Scores from the menu, print the names and scores of the people who played
the game.
6. Collaborate appropriately.
7. Program runs as expected.
8. Extra Credit: Trivia Game consists of 10 or more questions that includes
questions from your Math, English and/or History classes.
'''
trivia = {
    "history": [{"q":"who was the first president of the united states? ","a":"george washington"}, {"q":"what wall fell in 1989","a":"berlin wall"}, {"q":"what ancient civilization built the pyramids of mexico","a":"aztecs"}, {"q":"what is the capital of france?","a":"paris"}],
    "english": [{"q":"what is the antynonym of happy?","a":"sad"}, {"q":"what is the main character in a story called?","a":"protagonist"}, {"q":"what is the past tense of go?","a":"went"}, {"q":"what figure of speach compares two like things using like or as","a":"simile"}],
    "math": [{"q":"what is 2 + 2?","a":"4"}, {"q":"what kind of triangle has 3 equal sides?","a":"equilateral"}, {"q":"what do you call the instantanious rate of change","a":"derivative"}, {"q":"what is the integral of e^x","a":"e^x + C"}]
}
def main():
    leaderboard = {}
    done = False
    while not done:
        print("==========")
        print("S - Start")
        print("D - Display")
        print("Q - Quit")
        choice = input("Choice: ").lower().strip()
        if choice == "s" or choice == "start":
            print("Starting Game")
            name = input("What's your name? ")
            print("Welcome to the game", name + "!")
            category = input("Choose a category (History, English, Math): ").lower().strip()
            if category == "q" or category == "quit":
                done = True
            elif category in trivia:
                score = 0
                for question in trivia[category]:
                    answer = input(question["q"] + " ").lower().strip()
                    if answer == question["a"]:
                        score += 1
                        print("Correct!")                
                    elif answer == "q" or answer == "quit":
                        done = True
                print("Your score is:", score)
                leaderboard[name] = score
            else:
                print("Invalid category")
                continue
        elif choice == "q" or choice == "quit":
            print("Exiting Program")
            done = True
        elif choice == "d" or choice == "display":
            print("Leaderboard:")
            for player in leaderboard:
                print(player + ":", leaderboard[player])
main()
