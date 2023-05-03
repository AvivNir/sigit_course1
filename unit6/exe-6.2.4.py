def extend_list_x(list_x, list_y):
    [list_x.insert(i, j) for i, j in enumerate(list_y) if i < len(list_y)]
    return list_x


if __name__ == "__main__":
    x = [4, 5, 6]
    y = [1, 2, 3]
    print(extend_list_x(x, y))
