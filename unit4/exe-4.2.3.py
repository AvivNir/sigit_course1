if __name__ == '__main__':
    temp = input("Insert the temperature you would like to convert: ")
    # convert from Celsius to Fahrenheit
    if temp[-1].lower() == 'c':

        celsius = float(temp[:-1])
        fahrenheit = celsius * 1.8 + 32
        print(f"{fahrenheit:.1f}F")

    # convert from Fahrenheit to Celsius
    elif temp[-1].lower() == 'f':
        fahrenheit = float(temp[:-1])
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"{celsius:.1f}C")

    else:
        print("Invalid input. only 'numberC' / 'numberF'.")