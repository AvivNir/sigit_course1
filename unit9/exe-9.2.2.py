def copy_file_content(source, destination):
    with open(source, "r") as source_file:
        content = source_file.read()
    with open(destination, "w") as destination_file:
        destination_file.write(content)


if __name__ == '__main__':
    copy_file_content("D:/Desktop/python/equal1.txt", "D:/Desktop/python/equal2.txt")
