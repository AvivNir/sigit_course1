def numbers_letters_count(my_str):
    num_count = 0
    letter_count = 0
    for char in my_str:
        if char.isdigit():
            num_count += 1
            letter_count += 1

        elif char.isalpha():
            letter_count += 1
    return [num_count, letter_count]


if __name__ == '__main__':
    print(numbers_letters_count("Python 3.6.3"))
