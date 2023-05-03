def chocolate_maker(small, big, x):
    total_length = small + (big * 5)

    if total_length < x:
        return False

    if x % 5 > small:
        return False

    return True


if __name__ == '__main__':
    print(chocolate_maker(3, 2, 10))