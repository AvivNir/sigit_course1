def who_is_missing(file_name):
    with open(file_name, 'r') as f:
        numbers = f.read().strip().split(',')
    numbers = sorted(map(int, numbers))
    missing_number = None
    for i in range(1, len(numbers) + 1):
        if numbers[i-1] != i:
            missing_number = i
            break
    with open('found.txt', 'w') as f:
        f.write(str(missing_number))
    return missing_number


if __name__ == '__main__':
    print(who_is_missing("D:/Desktop/python/findme.txt"))
