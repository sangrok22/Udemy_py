import random
import hangman_art
import hangman_words


chosen_word = random.choice(hangman_words.word_list)
lives = 6
print(hangman_art.logo)
print(f'Pssst, the solution is {chosen_word}.')
chosen_list = []
for i in range(len(chosen_word)):
    chosen_list += "_"

while '_' in chosen_list:
    guess = input("Guess a letter: ").lower()

    if guess not in chosen_word:
        print(hangman_art.stages[lives])
        lives -= 1
    
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            chosen_list[i] = guess
    
    print(f"{' '.join(chosen_list)}")
    if lives < 0:
        print("You lose...")
        break
if lives > 0:
    print("You win!")  



    