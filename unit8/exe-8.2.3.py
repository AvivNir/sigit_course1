def mult_tuple(tuple1, tuple2):
    result = ()
    for i in tuple1:
        for j in tuple2:
            result += ((i, j), (j, i))
    return result


if __name__ == '__main__':
    first_tuple = (1, 2)
    second_tuple = (4, 5)
    print(mult_tuple(first_tuple, second_tuple))

    first_tuple = (1, 2, 3)
    second_tuple = (4, 5, 6)
    print(mult_tuple(first_tuple, second_tuple))