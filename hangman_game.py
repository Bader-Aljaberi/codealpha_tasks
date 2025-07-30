import random

def hangman():
    words = ["python", "student", "engineer", "game", "movie"]
    word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    word_completion = "_" * len(word)

    print("Welcome to Hangman! I randomly chosed a word, I need you to start guessing it !")
    print(word_completion)

    while incorrect_guesses < max_incorrect_guesses and "_" in word_completion:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
            new_word_completion = ""
            for i in range(len(word)):
                if word[i] == guess:
                    new_word_completion += guess
                else:
                    new_word_completion += word_completion[i]
            word_completion = new_word_completion
        else:
            print("Incorrect guess.")
            incorrect_guesses += 1

        print("Word: ", word_completion)
        print("Incorrect guesses left: ", max_incorrect_guesses - incorrect_guesses)

    if "_" not in word_completion:
        print("Congratulations! You guessed the word:", word)
    else:
        print("Game over! The word was:", word)

hangman()

