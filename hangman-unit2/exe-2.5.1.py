
import random

from colorama import Fore

MAX_TRIES = random.randint(5, 10)

HANGMAN_ASCII_ART = Fore.LIGHTYELLOW_EX + """ 
    \n Welcome to Aviv's Hangman game
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/
        \n
      Number of guesses: """ + str(MAX_TRIES)


if __name__ == '__main__':
    print(HANGMAN_ASCII_ART)
