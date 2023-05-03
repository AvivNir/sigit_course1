import string


def check_guess(guess):
    if len(guess) > 1:
        if all(c.isalpha() and c in string.ascii_letters for c in guess):
            print("E1")
        else:
            print("E3")
    elif not guess.isalpha():
        print("E2")
    else:
        print(guess.lower())


if __name__ == '__main__':
    guess = input("Guess a letter: ")
    check_guess(guess)
