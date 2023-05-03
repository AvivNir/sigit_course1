
def three_little_pigs():
    bricks = input("Enter three digits number")
    a = int(bricks[0])
    b = int(bricks[1])
    c = int(bricks[2])

    total = a + b + c
    each = total // 3
    remainder = total % 3

    print(total)
    print(each)
    print(remainder)
    print(remainder == 0)


if __name__ == '__main__':
    three_little_pigs()
