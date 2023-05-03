def fix_age(age):
    if 13 <= age <= 19 and age not in [15, 16]:
        return 0
    else:
        return age


def filter_teens(a=13, b=13, c=13):
    a = fix_age(a)
    b = fix_age(b)
    c = fix_age(c)
    return a + b + c


if __name__ == '__main__':
    print(filter_teens(2, 1, 15))
