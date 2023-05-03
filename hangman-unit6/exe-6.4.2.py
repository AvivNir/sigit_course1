
def check_valid_input(letter_guessed, old_letters_guessed):
    if len(letter_guessed) != 1 or not letter_guessed.isalpha():
        return False
    elif letter_guessed.lower() in old_letters_guessed:
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        print("old letters")
        print(old_letters_guessed)
        return True
    else:
        print("X\n" + " -> ".join(sorted(old_letters_guessed)))
        return False


def main():
    old_letters = ['a', 'p', 'c', 'f']
    print(try_update_letter_guessed('A', old_letters), "\n")
    print(try_update_letter_guessed('s', old_letters), "\n")
    print(try_update_letter_guessed('$', old_letters), "\n")
    print(try_update_letter_guessed('d', old_letters), "\n")


if __name__ == "__main__":
    main()
