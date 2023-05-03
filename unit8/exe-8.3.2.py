# Define the dictionary
mariah = {
    "first_name": "Mariah",
    "last_name": "Carey",
    "birth_date": "27.03.1970",
    "hobbies": ["Sing", "Compose", "Act"]
}

# Ask the user for input
choice = int(input("Enter a number between 1 and 7: "))

# Perform actions based on user input
if choice == 1:
    print(mariah["last_name"])
elif choice == 2:
    birth_month = mariah["birth_date"].split(".")[1]
    print(birth_month)
elif choice == 3:
    num_hobbies = len(mariah["hobbies"])
    print(num_hobbies)
elif choice == 4:
    last_hobby = mariah["hobbies"][-1]
    print(last_hobby)
elif choice == 5:
    mariah["hobbies"].append("Cooking")
    print(mariah["hobbies"])
elif choice == 6:
    birth_date = mariah["birth_date"].split(".")
    birth_tuple = (int(birth_date[0]), int(birth_date[1]), int(birth_date[2]))
    print(birth_tuple)
elif choice == 7:
    birth_year = int(mariah["birth_date"].split(".")[2])
    current_year = 2023
    age = current_year - birth_year
    mariah["age"] = age
    print(mariah["age"])


