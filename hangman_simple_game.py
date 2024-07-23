import random
import hangman_words
import hangman_art

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
print(f"cw - {chosen_word}")
display = ["_" for i in chosen_word]
lives = 6

while True:
    guessed_letter = input("Guess a letter: ").lower()
    if guessed_letter in display:
        print(f"You've already guessed {guessed_letter}")
    for ind, letter in enumerate(chosen_word):
        if letter == guessed_letter:
            display[ind] = guessed_letter
    if guessed_letter not in chosen_word:
        lives -= 1
        print(f"You guessed {guessed_letter}, that's not in the word. You lose a life.")
        if lives == 0:
            print("You Lose 😥")
            break
    print(f"{' '.join(display)}")
    if "_" not in display:
        print("You Win 👏🎉")
        break
    print(hangman_art.stages[lives])