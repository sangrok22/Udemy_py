import os

print("Welcome to the secret auction program.")

person=[]

def auction_pro(name,bid_ch):
    person.append({"name": name,
                   "bid_ch": bid_ch})

next_people = True    
while next_people:
    max = 0
    name = input("What is your name?: ")
    bid_ch = int(input("What's your bid?: $"))
    more_people = input("Are there any other bidders? 'yes' or 'no'.\n")
    auction_pro(name, bid_ch)
    
    if more_people == 'yes':
        os.system('cls')
    else:
        next_people = False
        for i in range(len(person)):
            if max<person[i]["bid_ch"]:
                max_peo = person[i]["name"]
                max = person[i]["bid_ch"]
        print(f"The winner is {max_peo} with a bid of ${max}.")

