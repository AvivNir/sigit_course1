

def format_list(my_list):
    return ', '.join(my_list[::2][:-1]) + ', and ' + my_list[-1]


if __name__ == "__main__":
    my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
    print(format_list(my_list))