def arrow(my_char, max_length):
    arrow_str = ""
    for i in range(1, max_length + 1):
        arrow_str += my_char*i + "\n"
    for i in range(max_length - 1, 0, -1):
        arrow_str += my_char*i + "\n"
    return arrow_str


if __name__ == '__main__':
    print(arrow('*', 9))