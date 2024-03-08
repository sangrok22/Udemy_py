import random

print("Welcome to the Numbering Guess Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
ran_number= random.randint(1,100)
# print(f"psst, the correct number = {ran_number}")

easy = 10
hard = 5

if difficulty =='easy':
    difficulty = easy
else:
    difficulty = hard

should_continue = True

while should_continue:

    print(f"You have a {difficulty} attempts remaining to guess the number.")

    guess_num = int(input("Make a guess: "))
    if guess_num > ran_number:
        print("Too high")
        difficulty -=1
        if difficulty == 0:
            print("You've run out of guesses, You lose...")
            print(f"Answer is {ran_number}")
            should_continue = False
    elif guess_num < ran_number:
        print("Too low")
        difficulty -= 1
        if difficulty == 0:
            print("You've run out of guesses, You lose...")
            print(f"Answer is {ran_number}")
            should_continue = False
    elif guess_num == ran_number:
        print(f"You got it! Answer is {guess_num}")
        should_continue = False

    