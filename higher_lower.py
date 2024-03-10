import random
import higher_game_data
import higher_lower_art
import os

A = random.choice(higher_game_data.data)
B = random.choice(higher_game_data.data)
if A == B:
    B = random.choice(higher_game_data.data)

should_continue= True


score= 0
while should_continue:
        
    print(higher_lower_art.logo)
    if score >= 1:
        print(f"Your right! Current score: {score}.")
    print("Compare A:",A['name'],", a", A['description'],", from",A['country'])
    print(higher_lower_art.vs)
    print("Against B:",B['name'],", a", B['description'],", from",B['country'])

    correct = ""
    if A['follower_count']>B['follower_count']:
        correct = "A"
    else:
        correct = "B"

    answer = input("Who has more follower? Type 'A' or 'B': ")

    if correct == answer.upper():
        score += 1
                
        A=B
        B = random.choice(higher_game_data.data)
    else:
        os.system('cls')
        print(higher_lower_art.logo)
        print(f"Sorry that's wrong... final score {score}")
        should_continue = False