def menu():
    print("1. Option 1")
    print("2. Option 2")
    print("3. Exit")


def main():
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            print("Option 1 selected")
        elif choice == '2':
            print("Option 2 selected")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()