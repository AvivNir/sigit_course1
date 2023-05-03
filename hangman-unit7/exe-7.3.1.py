def show_hidden_word(secret_word, old_letters_guessed):
    shown_word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            shown_word += letter + " "
        else:
            shown_word += "_ "
    return shown_word.rstrip()


if __name__ == '__main__':
    secret_word = "mammals"
    old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
    print(show_hidden_word(secret_word, old_letters_guessed))
