if __name__ == '__main__':
    sentence = input("Please enter a sentence: ")
    first_char = sentence[0]
    new_string = first_char + sentence[1:].replace(first_char, 'e')

    print(new_string)
