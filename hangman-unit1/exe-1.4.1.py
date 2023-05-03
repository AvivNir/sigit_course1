
from colorama import Fore
import random


# start screen for hangman game
def start_screen():
    print(Fore.LIGHTYELLOW_EX + " \n Welcome to Aviv's Hangman game")
    print(Fore.LIGHTYELLOW_EX + """
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
    """)
    print(Fore.LIGHTYELLOW_EX + "Number of guesses: ", random.randint(5, 10))


if __name__ == '__main__':
    start_screen()
