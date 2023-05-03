def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True


if __name__ == '__main__':
    secret_word = "friends"
    old_letters_guessed = ['m', 'p', 'j', 'i', 's', 'k']
    print(check_win(secret_word, old_letters_guessed))
