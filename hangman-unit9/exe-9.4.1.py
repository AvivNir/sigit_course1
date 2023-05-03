def choose_word(file_path, index):
    valid_path = False
    while not valid_path:
        try:
            with open(file_path, 'r') as file:
                words = file.read().split()
                num_words = len(words)
                index = (index - 1) % num_words
                word = words[index]
                unique = set(words)
                unique_number = len(unique)
                valid_path = True
        except FileNotFoundError:
            file_path = input(
                "Invalid path. Please enter the path to your words collection\n")

    return unique_number, word


if __name__ == '__main__':
    print(choose_word("D:/Desktop/python/hang.txt", 5))
