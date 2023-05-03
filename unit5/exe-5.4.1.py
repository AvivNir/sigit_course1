
def func(num1, num2):
    """
        * This function takes two numbers, num1 and num2, and returns their multiply.
        * Parameters:
        * num1 (int or float): number
        * num2 (int or float): number
        * Returns:
        * The multiply of num1 and num2.
    """
    return num1 * num2


def main():
    # Call the function func
    result = func(8, 8)
    print("The result is:", result)

    # Display the documentation for the func function
    help(func)


if __name__ == "__main__":
    main()
