import random

# set up variables
ANSWERS = ["python", "java", "swift", "javascript"]

menu_choice = ""
wins = 0
losses = 0
count = 0

# gameplay loop
print("H A N G M A N" + "  # " + str((8 - count)) + " attempts")
while menu_choice != "exit":
    menu_choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if menu_choice == "results":
        print("You won: " + str(wins) + " times")
        print("You lost: " + str(losses) + " times")
        continue
    elif menu_choice == "play":
        pass
    else:
        continue

    ANSWER = random.choice(ANSWERS)
    display_answer = []
    guesses = set()
    letters = set(ANSWER)

    # create the displayed letters
    for i in range(len(ANSWER)):
        display_answer.append("-")

    while count < 8 and ("-" in display_answer):
        guess = input("\n" + "".join(display_answer) + "\nInput a letter:")
        if len(guess) != 1:
            print("Please, input a single letter.")
            continue
        if guess.isupper() or (not guess.isalpha()):
            print("Please, enter a lowercase letter from the English alphabet.")
            continue
        if guess in letters and (guess not in guesses):
            guesses.add(guess)
            i = 0
            for letter in ANSWER:
                if guess == letter:
                    display_answer[i] = letter
                i += 1
            print("  # " + str((8 - count)) + " attempts")
        elif guess in guesses:
            print("You've already guessed this letter.  # " + str((8 - count)) + " attempts")
        else:
            count += 1
            print("That letter doesn't appear in the word.  # " + str((8-count)) + " attempts")
    if "-" not in display_answer:
        print("\n" + "".join(display_answer))
        print("You guessed the word " + "".join(display_answer) + "!")
        print("You survived!")
        wins += 1
        count = 0
    else:
        print("\nYou lost!")
        losses += 1
        count = 0
