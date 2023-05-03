def count_chars(my_str):
    char_dict = {}
    for char in my_str:
        if char != " ":
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict


if __name__ == '__main__':
    magic_str = "abra cadabra"
    char_count = count_chars(magic_str)
    print(char_count)