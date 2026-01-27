"""
This is for chapter 1

Note:
    Make a title screen
"""
import random

ursula = {
    "aura": 0,
    "health": 10,
    "energy": 10
}


def titleScreen():
    print("--------------------------------------------------------------------------")
    print("--------------------------The Life of Ursula -----------------------------")
    print("----------------------------- Chapter 1 ----------------------------------")
    print("--------------------------Number of Plays: 0 -----------------------------")
    print("--------------------------------------------------------------------------")

def showStats():
    print(f"Ursula Aura: {ursula["aura"]}")
    print(f"Ursula Health: {ursula["health"]}")
    print(f"Ursula Energy: {ursula["energy"]}")

def ticTacToe():
    print("Starting Tic-Tac-Toe")
    board = [" " for i in range(9)]
    print("|1| |2| |3|")
    print("|4| |5| |6|")
    print("|7| |8| |9|")

    def printBoard(): 
        row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
        row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
        row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])
        
        print()
        print(row1)
        print(row2)
        print(row3)
        print()

    def playerMove():
        while True:
            try:
                choice = int(input("Enter your move (1-9): "))
                if 1 <= choice <= 9 and board[choice-1] == " ":
                    board[choice-1] = "X"
                    break
                else:
                    print("That space is taken or invalid!")
            except ValueError:
                print("Enter a number between 1 and 9.")

    def computerMove():
        print("Computer's turn...")
        while True:
            choice = random.randint(1, 9)
            if board[choice-1] == " ":
                board[choice-1] = "O"
                break

    def isVictory(icon): 
        return (
            (board[0] == icon and board[1] == icon and board[2] == icon) or
            (board[3] == icon and board[4] == icon and board[5] == icon) or
            (board[6] == icon and board[7] == icon and board[8] == icon) or
            (board[0] == icon and board[3] == icon and board[6] == icon) or
            (board[1] == icon and board[4] == icon and board[7] == icon) or
            (board[2] == icon and board[5] == icon and board[8] == icon) or
            (board[0] == icon and board[4] == icon and board[8] == icon) or
            (board[2] == icon and board[4] == icon and board[6] == icon)
        )

    def isDraw(): 
        return " " not in board

    # -------- Main Game Loop --------
    while True: 
        printBoard()
        playerMove()
        
        if isVictory("X"): 
            printBoard()
            print("You win! 🎉")
            return "Win"
        elif isDraw(): 
            printBoard()
            print("It's a draw!")
            return "Draw"
            
        computerMove()
        
        if isVictory("O"):
            printBoard()
            print("Computer wins!")
            return "Lose"




playing = True
def hangman():
    global ursula
    print("Starting Hangman")
    def printPrettyList(lst):
        # Replace empty strings with underscores
        formatted = [x if x != "" else "_" for x in lst]
        # Join the list into a single string with spaces between elements
        print(" ".join(formatted))

    randWord = "forgive"
    # Turn word into a list
    randomWord = list(randWord)

    # Create base
    print("Random Word Chosen")
    guessedLetters = [""] * len(randomWord) 

    lives = 10
    while (lives > 0):
        printPrettyList(guessedLetters)
        chosenLetter = input("choose a letter: ")
        if(chosenLetter in randomWord):
            print("yes")
            guessedLetters[randomWord.index(chosenLetter)] = chosenLetter
        else:
            print("no")
            lives -= 1
        if("" not in guessedLetters):
            print("You have deciphered the word: forgiveness")
            print("Prudencio Aguilar slowly fades away.")
            ursula["aura"] += 1000
            break

        print("Lives: ", lives)
    else:
        play = input("You lost this round, play again?[y/n]: ")
        if (play.lower() == "y"):
            print("You ask him if you can play again.")
            hangman()
        else:
            print("The next day, he takes out the board again.")

def introduction():
    print("Welcome Ursula. Welcome to your life.")
    print("You have married your cousin, Jose Arcadio Buendia, and now pregnant with a child.")
    print("Your husband/cousin has recently killed a man named Prudencio Aguilar.")
    print("Every now and then, you see Prudencio Aguilar's ghost, clutching at the gaping hole in his neck.")
    print("One day, he invites you to play a game of hangman.")
    hangman()
    print("After seeing Prudencio Aguilar for so long, feeling the guilt, JAB decides to take you, and a few\nother families, and found a new town.")
    print("Your only worry now is that your child doesn't have a pig-tail.")

def jungleJourney():
    leftRightBreak = input("Eventually, you come upon a break in the road, \ndo you tell your husband to go left [l] or right[r]?: ")
    if (leftRightBreak == "l"):
        print("JAB decides to ignore you and go right.")
    elif(leftRightBreak == "r"):
        print("JAB decides to ignore you and go left")
    arcadioName = input("Your first child has been born, without a pigtail! What do you want to name him?: ")
    print("You tell the name to JAB, who thinks it is a terrible idea and wants to name him Jose Arcadio Buendia.")
    print("You sigh, and decide to name him Jose Arcadio Buendia, or Arcadio for short.")
    print("Your second child has been born, whom you decide to name him Aureliano. He doesn't have a pigtail either!")
    print("Eventually, traveling through much jungle, JAB finally gives up his quest and decides to found a \ntown right here.")

def macondoFounding():
    print("JAB sets up all the houses to be equidistant from the river and have the same structure, so \neveryone is equal.")
    print("You set up your home.")

def gypsies1():
    print("Everything is fine for a few years, when one day, the gypsies come to town. One of the gypsies is\nnamed Melquiades.")
    print("Melquiades wants to sell JAB some metal stones in exchange for the two donkeys that provide your livelyhood.")
    giveDonkey = input("Do you give JAB the donkies? [y/n]")
    if giveDonkey == "y":
        print("JAB ignores you and just takes the donkies.")
    elif giveDonkey == "n":
        print("JAB ignores you and just takes the donkies.")
    else:
        exit("Please make sure you do everything exactly. This is your only warning. You will be ignored in the future.")
    print("JAB exchanges the donkies for some metal stones from Melquiades. He says that he will make back triple the money that \nwas lost.")
    print("donkies -2")
    print("After the gypsies leave, JAB leaves to try his 'plan', but it doesn't work. Instead, he just finds some old armor.")
    print()

def gypsies2():
    print("Everything is fine for a while, but then the gypsies return. This time, JAB wants to buy a large\nglass lens from Melquiades.")
    giveMoney = input("Do you give him the money? [y/n]: ")
    if giveMoney == "y":
        print("JAB immediately runs off to go buy it.")
    elif giveMoney == "n":
        print("Ignoring your refusal, he barges into your room and digs up the money.")
        print("Not even caring about your tears, he rushes out with the  money in hand")
    
    print("With the new item, JAB starts setting things, even himself, on fire, like a child. He almost burns the house down.")
    stopJAB = input("Do you tell him to stop? [y/n]: ")
    if stopJAB == "y":
        print("JAB ignores you and goes on with his experiments")
    if stopJAB == "n":
        print("You decide to just ignore JAB and focus on raising the kids, since JAB refuses to.")
        ursula["aura"] += 10
        print("You have gained 10 aura.")

    print("After enough of his 'experiments', JAB holes himself up in his room and writes manuscripts on \n'solar warfare' whatever that means.")
    print("A few months later, he mails it to the government. What he thinks will happen, you don't know.")
    print("JAB gets the money he used to buy the lens back from Melquiades.")
    print()

def gypsies3():
    print("The gypsies are back, and this time, Melquiades starts encouraging JAB in his experiments and alchemy.")
    print("They make a shack they call a 'lab' in the backyard. Melquiades gives JAB lots of stuff for his experiments.")
    print("Melquiades has decided he wants to be in your home and tell his stories to your children.")
    print("A few days later, you enter a room with Melquiades and smell an acidic, corrosive stench.")
    melSay = input("Do you want to say:\n1. That is the smell of the Devil.\n2. What is that terrible stench?")
    if melSay == "1":
        print("Melquiades says, 'Actually, the Devil smells like sulfur, this is just a corrosive sublimate.'")
    elif melSay == "2":
        print("JAB says, 'Oh Ursula, stop worrying so much.'")
    print()

def gypsiesReflection():
    print("You reflect on JAB. He used to be a kind of youthful patriarch, who would give advice for planting and advice\nfor raising children and animals, and who collaborated with everyone.")
    print("Now, all he does is run around trying to catch birds, setting traps, going crazy in that shack in the backyard.")
    print()

def JABStopJourney():
    print("JAB has decided to scout the region with some men. He leaves for many weeks. When he returns, he says that Macondo is\n surrounded on all sides by water.")
    print("After many months, JAB has decided to move Macondo to a better place. You are heavily against it.")
    print("You decide to talk to the other women of Macondo to stop the move, so you all meet in the middle of the night.")
    print("Because it is such an even split, for and against the move, you must play tic-tac-toe to decide the winner.")
    keepPlaying = True
    while keepPlaying:
        result = ticTacToe()
        if result != "Win":
            print("A strange force pauses and rewinds time. You get another try.")
        elif result == "Win":
            print("You have successfully convinced them to stop their husbands.")
            keepPlaying = False

def JABJourney():
    print("Even knowing that no one else will follow him, JAB still wants to leave. He says that someone doesn't belong in a town\nuntil someone dies.")
    stopJABChoice = input("What do you want to say?:\n1. If someone needs to die in Macondo for the family will stay, you will gladly die.\n2. No")
    if stopJABChoice == "1":
        print("You gain 1 million aura.")
        ursula["aura"] += 1000000
    print("Seeing that he can't convince you, he eventually give up.")
    print("You tell him that instead of chasing his fantasies, he should take care of his children.")
    ursula["aura"] += 100
    print("Something seems to finally click in his head. From then on, he starts acting like a real parent, taking care of the kids.")
    print()

def ice():
    print("JAB decides to take Arcadio and Aureliano to the gypsies as a show. Even though you don't like Melquiades, it will allow\nthem to bond, so you let them go.")
    print("A few hours later, they come back.")
    input("Do you ask them how it went? [y/n]: ")
    print("Aureliano pauses and turns to you. 'We saw ice', he says.")

def credits():
    print("You have lived the first chapter of the life of Ursula. See the reflection for the stuff, but a good chunk of your\nchoices had very little to no effect on the story.")
    print("The only thing that changed was how much aura you have.")
    print("Ursula:")
    print(f"\tAura: {ursula["aura"]}")
    pass

while playing:
    showStats()
    introduction()
    print("Please fill out the instructions EXACTLY as shown (including capitals, no spaces for y/n questions.)")
    showStats()
    jungleJourney()
    showStats()
    macondoFounding()
    showStats()
    gypsies1()
    showStats()
    gypsies2()
    showStats()
    gypsies3()
    showStats()
    gypsiesReflection()
    showStats()
    JABStopJourney()
    showStats()
    JABJourney()
    showStats()
    ice()
    break
