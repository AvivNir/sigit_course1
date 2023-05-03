
if __name__ == '__main__':
    data = ("self.py", "learner", 1.5)
    format_string = "Hello %s %s, you have only %.1f units" \
                    " left before you master the course!"
    print(format_string % data)
