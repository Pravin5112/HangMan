import random
from hangman_art import stages, logo
from hangman_word import word_list

lives = 6
print(logo)
placeholder = ""
chosen_word = random.choice(word_list)
print(chosen_word)
word_length = len(chosen_word)
for blank in range(word_length):
    placeholder += "_"
    
print(placeholder)

correct_list = []
game_over = False
while not game_over:

    print(f"*******************************{lives}/6 LIVES FEST******************************")

    guess = input("Guess a letter: ").lower()
    if guess in correct_list:
        print(f"You have already guessed {guess} letter.")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_list.append(guess)
        elif letter in correct_list:
            display += letter

        else:
            display += "_"       

    print("Word to guess: "+display)  

    if guess not in chosen_word:
        print(f"You guessed {guess} that letter was not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"************************************{chosen_word} YOU LOSE********************************")

    if "_" not in display:
        game_over = True
        print(f"**************************************{chosen_word} YOU WIN***********************************")      

    print(stages[lives])    