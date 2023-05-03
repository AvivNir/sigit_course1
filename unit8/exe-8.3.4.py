def inverse_dict(my_dict):
    inverse = {}
    for key, value in my_dict.items():
        inverse.setdefault(value, []).append(key)
    for key in inverse:
        inverse[key].sort()
    return inverse


if __name__ == '__main__':
    course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
    print(inverse_dict(course_dict))