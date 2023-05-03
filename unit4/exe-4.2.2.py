
if __name__ == '__main__':
    s = input("Enter a word: ").replace(" ", "").lower()
    print("OK" if s == s[::-1] else "NOT")