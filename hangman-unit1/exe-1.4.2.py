
from colorama import Fore


# start screen for hangman game
def draw_hangman_figure():
    print(Fore.LIGHTYELLOW_EX + """
  picture 1:
    x-------x

picture 2:
    x-------x
    |
    |
    |
    |
    |

picture 3:
    x-------x
    |       |
    |       0
    |
    |
    |

picture 4:
    x-------x
    |       |
    |       0
    |       |
    |
    |

picture 5:
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |

picture 6:
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |

picture 7:
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    """)


if __name__ == '__main__':
    a, b = "q" not in "snow", type(-200) == type(200)
    print(a != b)
