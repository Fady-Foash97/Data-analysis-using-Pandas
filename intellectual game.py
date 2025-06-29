## Intellectual game
## Attachments
import random
import pygame
## Initialize background music
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("792340__zhr__chill-background-music-3.wav")
pygame.mixer.music.play(-1)
## Introduction
print("Let's play a game to test your brains")
## Puzzle 1
print("\nPuzzle 1: Your computer is running slow")
puzzle1 = input("\n")
## Physical problem
if puzzle1 == "Cleaning the dust out of my computer":
    print("\nClever")
    tools = ["Screwdriver", "Cleaning cloth", "Spray", "Hair dryer"]
    print("\nTools to use:")
    for tool in tools:
        print(f"{tool}")
    print("\nYou are well prepared but you need a mask and sunglasses to cover your face from dust")
## Performance problem
elif puzzle1 == "If the problem is internal, I would use antivirus and antispyware programs":
    print("\nYou are well prepared for any cyber security problem")
else:
    print("\nTry again")
## Puzzle 2
print("\nPuzzle 2: Your warehouse is full of random supplies")
puzzle2 = input("\n")
if puzzle2 == "Arrange supplies based on category":
    print("\nExcellent, you are a smart manager")
elif puzzle2 == "Arrange supplies based on requirement":
    print("\nYou are a smart seller")
else:
    print("\nTry again")
## Puzzle 3
print("\nPuzzle 3: You are in a desert, you feel hungry, \nSuddenly! you saw an animal")
puzzle3 = input("\n")
if puzzle3 == "I would hunt it with whatever weapon I have":
    weapons = ["Hunting rifle", "Knife", "A bow and arrow"]
    for weapon in weapons:
        print(f"{weapon}")
else:
    print("\nTry again")
## Puzzle 4
print("\nPuzzle 4: Your baby is crying.")
Decisions = ["Make a funny face", "Give him milk to drink", "Give him his favourite toy"]
random.shuffle(Decisions)
for Decision in Decisions:
    print(f"{Decision}")
puzzle4 = input("\n")
if puzzle4 == "Make a funny face":
    print("\nYou made the baby laugh!")
    print("\nYou are a great parent")
elif puzzle4 == "Give him milk to drink":
    print("\nThat's what the baby needed")
    print("\nYou are a great parent")
elif puzzle4 == "Give him his favourite toy":
    print("\nHe stopped crying and started playing")
    print("\nYou are a great parent")
else:
    print("\nTry again")
## Puzzle 5
print("\nPuzzle 5: You are a spy on a top secret mission, there's a locked door in front of you.")
print("\nChoose your approach:")
options = ["Pick lock", "Kick the door"]
for option in options:
    print(f"{option}")
puzzle5 = input("\n")
if puzzle5 == "Pick lock":
    print("\nSmart way, no one will know you were really here")
elif puzzle5 == "Kick the door":
    print("\nCongratulations, your cover is blown!")
    print("\nGet your gun ready!")
    guard = input("two guards, one hiding behind a crate, the other behind a wall, \nwho will you shoot first? ")
    if guard == "The guard behind the wall then the other one":
        print("\nExcellent shot mister Wick!")
    else:
        print("\nMission failed!")
## Puzzle 6
print("\nPuzzle 6: You travel back in time to world war 2, you are part of the Russian army")
print("\nWhat primary choice of weapon you would have?")
puzzle6 = input("\n")


