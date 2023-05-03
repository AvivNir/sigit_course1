from colorama import Fore

# dictionary which holds the levels of the game
HANGMAN_PHOTOS = {0: "    x-------x",
                  1: "    x-------x\n    |\n    |\n    |\n    |\n    |",
                  2: "    x-------x\n    |       |\n    |       0\n    |\n    |\n    |",
                  3: "    x-------x\n    |       |\n    |       0\n    |       |\n    |\n    |",
                  4: "    x-------x\n    |       |\n    |       0\n    |      /|\ \n    |\n    |",
                  5: "    x-------x\n    |       |\n    |       0\n    |      /|\ \n    |      / \n    |",
                  6: "    x-------x\n    |       |\n    |       0\n    |      /|\ \n    |      / \\\n    |"}

# a number which represent the maximum tries the player gets
MAX_TRIES = 6


def start_screen():
    """
        Displays the title of the game, the hangman ASCII art,
         and the maximum number of tries allowed in the game.
    """
    print(Fore.LIGHTBLUE_EX + " \n Welcome to Aviv's Hangman game")
    print(Fore.LIGHTBLUE_EX + """
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/
        """)


def show_hidden_word(secret_word, old_letters_guessed):
    """
    returns a string which is the shown version of the secret
    word, with the un-guessed letters represented by underscores,
    and the guessed letters are displayed in their corresponding
    positions in the word, separated by spaces.

    Parameters:
    secret_word (str): the secret word to guess
    old_letters_guessed (list): a list of guessed letters

    Returns:
    shown_word (str): the shown version of the secret word,
                      with guessed letters shown, and un-guessed letters
                      replaced by underscores.
    """
    shown_word = ""
    for letter in secret_word.lower():
        if letter in old_letters_guessed:
            shown_word += letter + " "
        else:
            shown_word += "_ "
    return shown_word.rstrip()


def is_guess_successful(letter_guessed, secret_word):
    """
    checks if a letter guessed by the player
    matches any of the letters in the secret word.

    Parameters:
    letter_guessed (str): A string representing the letter guessed by the player.
    secret_word (str): A string representing the secret word that the
                       player is trying to guess.

    Returns:
    bool: Returns True if the letter guessed is found
          in the secret word, otherwise returns False.
    """
    if secret_word.lower().find(letter_guessed) != -1:
        return True

    return False


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    Checks if a guessed letter is a valid input or not.

    Parameters:
    letter_guessed (str): the letter guessed by the player.
    old_letters_guessed (list): a list of previously guessed letters.

    Returns:
    bool: True if the guessed letter is a valid input, False otherwise.
    """
    if len(letter_guessed) != 1 or not letter_guessed.isalpha():
        return False
    elif letter_guessed.lower() in old_letters_guessed:
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    tries to update the list of old letters guessed with the current letter guessed.
    if the input letter is valid it adds the letter to the list of old letters guessed.
    Otherwise, it prints a message indicating that the input is invalid and shows the
    list of old letters guessed.

    Parameters:
    letter_guessed (str): the letter guessed by the player.
    old_letters_guessed (list): a list of letters that have already
                                been guessed by the player.
    Returns:
    True if the letter is added to the list of old letters guessed successfully,
    False otherwise.
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print("X \n" + " -> ".join(sorted(old_letters_guessed)))
        return False


def choose_word(file_path, index):
    """
        A function that chooses a word from a text file based on the given index.

        Parameters:
        file_path (str): A string representing the path to the text file.
        index (int): An integer representing the position of the desired word in the file.

        Returns:
        word (str): the chosen word in the given index from the text file
    """
    valid_path = False
    while not valid_path:
        try:
            with open(file_path, 'r') as file:
                words = file.read().split()
                num_words = len(words)
                index = (index - 1) % num_words
                word = words[index]
                valid_path = True
        except FileNotFoundError:
            file_path = input(
                "Invalid path. Please enter the path to your words collection\n")

    return word


def print_hangman(num_of_tries):
    """
    Prints the corresponding image of the Hangman game according
    to the number of tries left.

    Parameters:
    num_of_tries (int): the current number of tries the player has
    """
    print("\n " + HANGMAN_PHOTOS[num_of_tries])


def check_win(secret_word, old_letters_guessed):
    """
    checks whether the player has guessed all the letters in the secret word.

    Parameters:
    secret_word (str): the secret word to be guessed.
    old_letters_guessed (list): a list of all the letters the player has guessed so far.

    Returns:
    bool: True if all the letters in the secret word have been guessed, False otherwise.
    """
    for letter in secret_word:
        if letter.lower() not in old_letters_guessed:
            return False
    return True


def handle_game():
    """
    runs the hangman game. Displays the start screen, inputs path to the words file
    ,the index of the secret word, and runs the game loop. The game loop allows
    the player to enter letter guesses until the player has used up all their guesses,
    or they guess the secret word.
    """

    start_screen()
    # Get path to word collection and index of secret word from player's input
    words_path = input("Please enter the path to your words collection\n")
    index = int(input("Please enter the index of the secret word \n"))
    # Get the secret word from the choose_word function
    secret_word = choose_word(words_path, index)

    # Use global MAX_TRIES variable and initialize old_letters_guessed
    global MAX_TRIES
    old_letters_guessed = []
    # run the game loop
    while MAX_TRIES != 0:
        print("\n Number of guesses: " + str(MAX_TRIES))
        # print hangman photo, according to the remaining guesses
        print_hangman(6 - MAX_TRIES)
        # show secret word with underscores
        print(show_hidden_word(secret_word, old_letters_guessed))
        guess = input("Please enter a letter \n")

        # Check if guess is successful
        if (not is_guess_successful(guess, secret_word)) and \
                check_valid_input(guess, old_letters_guessed):
            # subtract one from global variable MAX_TRIES
            print("not this one :(")
            MAX_TRIES -= 1

        else:
            try_update_letter_guessed(guess, old_letters_guessed)
            # Check if the player won, if so, finish the game
            if check_win(secret_word, old_letters_guessed):
                print("\n" + secret_word)
                print("good job! u actually won \n"
                      ",with " + str(MAX_TRIES) + " guesses left")
                break

    # if the player lost
    if MAX_TRIES == 0:
        print("maybe next time :)")
        print("the secret word was: " + secret_word)
        print_hangman(6)


def main():
    handle_game()


if __name__ == '__main__':
    main()
