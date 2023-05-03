
def shift_left(my_list):
    return my_list[1:] + [my_list[0]]


if __name__ == "__main__":
    print(shift_left([0, 1, 2])) # [1, 2, 0]
    print(shift_left(['monkey', 2.0, 1]))

