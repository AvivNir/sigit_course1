def sequence_del(my_str):
    new_str = my_str[0]
    for i in range(1, len(my_str)):
        if my_str[i] != my_str[i-1]:
            new_str += my_str[i]
    return new_str


if __name__ == '__main__':
    print(sequence_del("ppyyyyythhhhhooonnnnn"))
    print(sequence_del("SSSSsssshhhh"))
    print(sequence_del("Heeyyy   yyouuuu!!!"))
