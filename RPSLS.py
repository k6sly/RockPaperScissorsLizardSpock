#!/usr/bin/env python2

# Rock, Paper, Scissors, Lizard, Spock: The Video Game

import random
import time
import os

global player_score, computer_score, cpu_name, player_name

rock = 1
paper = 2
scissors = 3
lizard = 4
spock = 5

names = { rock: "Rock", paper: "Paper", scissors: "Scissors", lizard: "Lizard", spock: "Spock" }
rules1 = { scissors: paper, paper: rock, rock: lizard, lizard: spock, spock: scissors }
rules2 = { scissors: lizard, lizard: paper, paper: spock, spock: rock, rock: scissors }
intro = ( "Rock,", "Paper,", "Scissors,", "Lizard,", "Spock" )

player_score = 0
computer_score = 0

def player_name(self):
     return player_name

def cpu_name(self):
     return cpu_name

def start():
    global player_name, cpu_name
    os.system('cls')
    print ""
    print ""
    strIntro = " Let's play a game of"
    print strIntro
    time.sleep(2)
    os.system('cls')
    for x in range(0, 5):
        strIntro += " " + intro[x]
        print ""
        print ""
        print strIntro
        time.sleep(0.3)
        if x < 4:
            os.system('cls')
        x += 1
    player_name = raw_input(" What is your name? : ")
    cpu_name = raw_input(" What would you like your opponent's name to be? : ")
    print " Hello %s!" % (player_name)
    print ""
    print " Your opponent will be %s." % (cpu_name)
    while game():
        pass
    scores()

def game():
	player = move()
	computer = random.randint(1, 5)
	result(player, computer)
	return play_again()

def move():
    while True:
        print
        player = raw_input (" =========================\n \
| [1]Rock                |\n \
| [2]Paper               |\n \
| [3]Scissors            |\n \
| [4]Lizard              |\n \
| [5]Spock               |\n \
=========================\n\n \
            Make a move: ")
        try:
            player = int(player)
            if player in (1,2,3,4,5):
                return player
        except ValueError:
            pass
        print " Oops! I didn't understand that. Please enter 1, 2, 3, 4 or 5."
        
def result(player, computer):
    global player_score, computer_score, cpu_name, player_name
    print " 1..."
    time.sleep(1)
    print " 2..."
    time.sleep(1)
    print " 3!"
    time.sleep(0.5)
    print " %s threw {0}!".format(names[computer]) % (cpu_name)
    action = format(names[player])+format(names[computer])

    if player == computer:
        print " Tie game."
    else:
        if rules1[player] == computer:
            print (" %s %s %s" % (format(names[player]), f(action), format(names[computer])))
            print " You win! This time..."
            player_score += 1
        elif rules2[player] == computer:
            print (" %s %s %s" % (format(names[player]), f(action), format(names[computer])))
            print " You win! This time..."
            player_score += 1
        else:
            action = format(names[computer])+format(names[player])
            print (" %s %s %s" % (format(names[computer]), f(action), format(names[player])))
            print " %s laughs as you realise you have been defeated." % (cpu_name)
            computer_score += 1
            
def play_again():
    answer = raw_input(" Would you like to play again? y/n: ")
    if answer in ("y", "Y", "yes", "Yes", "Of course!"):
        return answer
    else:
        os.system('cls')
        print ""
        print ""
        print " Thank you very much for playing our game %s. See you next time!\n" % (player_name)
        
def scores():
    print " HIGH SCORES"
    print " %s: " % (player_name), player_score
    print " %s: " % (cpu_name), computer_score

def f(x):
    return {
        'ScissorsPaper': 'cut',
        'PaperRock': 'covers',
        'RockLizard': 'crushes',
        'LizardSpock': 'poison',
        'SpockScissors': 'smashes',
        'ScissorsLizard': 'decapitates',
        'LizardPaper': 'eats',
        'PaperSpock': 'disproves',
        'SpockRock': 'vaporizes',
        'RockScissors': 'crushes',
        }[x]

if __name__ == '__main__':
    start()
