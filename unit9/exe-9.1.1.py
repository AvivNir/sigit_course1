def are_files_equal(file1, file2):
    with open(file1, 'r') as f1,\
            open(file2, 'r') as f2:
        return f1.read() == f2.read()


if __name__ == '__main__':
    print(are_files_equal("D:/Desktop/python/equal1.txt", "D:/Desktop/python/equal2.txt"))
