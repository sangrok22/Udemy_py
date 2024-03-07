rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

your_ch = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if your_ch >=3 or your_ch < 0:
    print("Your choose wrong number, You lose")
    
if your_ch==0:
    print(rock)
if your_ch == 1:
    print(paper)
if your_ch==2:
    print(scissors)

com_ch = random.randint(0,2)
print("Computer choose:")

if com_ch==0:
    print(rock)
if com_ch == 1:
    print(paper)
if com_ch==2:
    print(scissors)

if your_ch == com_ch:
    print("You draw")

if your_ch == 0:
    if com_ch ==1:
        print("You lose")
    if com_ch == 2:
        print("You win")

if your_ch == 1:
    if com_ch ==2:
        print("You lose")
    if com_ch == 0:
        print("You win")

if your_ch == 2:
    if com_ch ==1:
        print("You lose")
    if com_ch == 0:
        print("You win")