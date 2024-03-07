import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    my_cards=[]
    com_cards=[]

    for i in range(2):
        my_cards.append(random.choice(cards))
    score=sum(my_cards)
    com_cards = random.choice(cards)
    print(f"Your cards: {my_cards}, current score: {score}")
    print(f"Computer's first card: {com_cards}")

    should_continue = True
    while should_continue:
        more_card= input("Type 'y' to get another card, type 'n' to pass: ")
        if more_card == 'y' and score <= 21:
            my_cards.append(random.choice(cards))
            score=sum(my_cards)
            print(f"Your cards: {my_cards}, current score: {score}")
            if score > 21:
                should_continue = False
                print("You lose...")