def is_greater(my_list, n):
    result = []
    for num in my_list:
        if num > n:
            result.append(num)
    return result


if __name__ == "__main__":
    result = is_greater([1, 30, 25, 60, 27, 28], 28)
    print(result)
    