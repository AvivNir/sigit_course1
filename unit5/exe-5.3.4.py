def last_early(my_str):
    my_str = my_str.lower()
    last_char = my_str[-1]
    if my_str.count(last_char) > 1:
        return True
    else:
        return False


if __name__ == '__main__':
    print(last_early("X"))
