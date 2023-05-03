import string


def check_guess(guess):
    if len(guess) > 1:
        if all(c.isalpha() and c in string.ascii_letters for c in guess):
            return "E1"
        else:
            return "E3"
    elif not guess.isalpha():
        return "E2"
    else:
        return "ok"


def main():
    letter_guessed = input("Guess a letter: ")
    if check_guess(letter_guessed) == "ok":
        print("Valid input")
    else:
        print("Invalid input")


if __name__ == "__main__":
    main()
