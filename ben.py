import random


def choose_country():
    countries = ["CHina", "United Kingdom", "United States","France","Germany",'Netherlands',"Iceland","Canada"]
    return random.choice(countries)


def display_word(secret_word, guessed_letters):
    displayed_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word


def process_guess(secret_word, guessed_letters, guess):
    guessed_letters.append(guess)
    if guess not in secret_word:
        return False
    else:
        return True


def main():
    secret_word = choose_country().lower()
    guessed_letters = []
    chances = len(secret_word) + 1

    print("Welcome to Country Hangman Game!")
    print("You have {} chances to guess the country name.".format(chances))

    while chances > 0:
        print("\nCurrent Word:", display_word(secret_word, guessed_letters))
        guess = input("Enter a letter guess: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again!")
            continue

        if process_guess(secret_word, guessed_letters, guess):
            print("Correct guess!")
        else:
            print("Incorrect guess!")

        guessed_letters.append(guess)

        if display_word(secret_word, guessed_letters) == secret_word:
            print("\nCongratulations! You win the game:", secret_word)
            break

        chances -= 1
        print("Chances left:", chances)

    if chances == 0:
        print("\nSorry, you've run out of chances. The country was:", secret_word)


if __name__ == "__main__":
    main()