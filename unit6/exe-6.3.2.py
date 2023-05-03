def longest(my_list):
    return max(my_list, key=len)


if __name__ == "__main__":
    list1 = ["111", "234", "2000", "goru", "birthday", "09"]
    print(longest(list1))