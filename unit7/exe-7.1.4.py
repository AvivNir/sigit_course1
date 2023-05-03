def squared_numbers(start, stop):
    res = []
    num = start

    while num <= stop:
        res.append(num ** 2)
        num += 1

    return res


if __name__ == "__main__":
    print(squared_numbers(4, 8))
    print(squared_numbers(-3, 3))
    