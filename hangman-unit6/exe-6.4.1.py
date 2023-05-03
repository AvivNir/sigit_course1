

def check_valid_input(letter_guessed, old_letters_guessed):
    if len(letter_guessed) != 1 or not letter_guessed.isalpha():
        return False
    elif letter_guessed.lower() in old_letters_guessed:
        return False
    else:
        return True


def main():
    old_letters = ['a', 'b', 'c']
    print(check_valid_input('C', old_letters))
    print(check_valid_input('ep', old_letters))
    print(check_valid_input('$', old_letters))
    print(check_valid_input('s', old_letters))


if __name__ == "__main__":
    main()
