def print_menu():
    print("1. Print the list of products")
    print("2. Print the number of products in the list")
    print("3. Check if a product is on the list")
    print("4. Count how many times a certain product appears")
    print("5. Delete a product from the list")
    print("6. Add a product to the list")
    print("7. Print all invalid products")
    print("8. Remove duplicates from the list")
    print("9. Exit")


def print_products(products):
    print("List of products:")
    print(", ".join(products))


def count_products(products):
    print("Number of products:", len(products))


def check_product(products):
    product_name = input("Enter a product name: ")
    if product_name in products:
        print("Yes, this product is on the list.")
    else:
        print("No, this product is not on the list.")


def count_occurrences(products):
    product_name = input("Enter a product name: ")
    count = products.count(product_name)
    print("The product appears", count, "times.")


def delete_product(products):
    product_name = input("Enter a product name to delete: ")
    if product_name in products:
        products.remove(product_name)
        print("Product deleted.")
    else:
        print("This product is not on the list.")


def add_product(products):
    product_name = input("Enter a product name to add: ")
    products.append(product_name)
    print("Product added.")


def print_invalid_products(products):
    invalid_products = [product for product in products if len(product) < 3 or not product.isalpha()]
    if invalid_products:
        print("Invalid products:", ", ".join(invalid_products))
    else:
        print("There are no invalid products.")


def remove_duplicates(products):
    products = list(set(products))
    print("Duplicates removed.")
    return products


def main():
    products_string = input("Enter a list of products (comma-separated): ")
    products = products_string.split(",")

    while True:
        print_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print_products(products)
        elif choice == 2:
            count_products(products)
        elif choice == 3:
            check_product(products)
        elif choice == 4:
            count_occurrences(products)
        elif choice == 5:
            delete_product(products)
        elif choice == 6:
            add_product(products)
        elif choice == 7:
            print_invalid_products(products)
        elif choice == 8:
            products = remove_duplicates(products)
        elif choice == 9:
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
