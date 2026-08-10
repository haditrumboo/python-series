import random

number = random.randint(1, 100)
guesses = 0
max_guesses = 7

while guesses < max_guesses:
    a = int(input("Guess the number (1-100): "))
    guesses += 1

    if a > number:
        print("Too high!")
    elif a < number:
        print("Too low!")
    else:
        print(f" Correct! You guessed it in {guesses} guesses.")
        break
else:
    print(f"you lost! The number was {number}.")