from manager import Manager

def main():
    name = input("Enter your name: ")
    print("Welcome", name)
    while True:
        print(f'What do you want to do, {name}?')
        print("1. Check password")
        print("2. Set password")
        print("3. Change password")
        print('4. List all websites')
        print('5. Change my name')
        print("6. Delete all credentials")
        print("7. Exit")
        choice = input("Enter your choice: ")
        user = Manager(name)
        if choice == "1":
            website = input("Enter the website: ")
            password = user.get_password(website)
            if password:
                print(f"The password for {website} is {password}")
            else:
                print("Invalid website")
                continue
        elif choice == "2":
            website = input("Enter the website: ")
            if user.check_if_website_exists(website):
                print("Website already exists")
                continue
            # password = input("Enter the password: ")
            while True:
                print("Do you want to create a random password or enter your own?")
                print("1. Random password")
                print("2. My password")
                choice = input("Enter your choice: ")
                if choice == "1":
                    length = int(input("Enter the length of the password: "))
                    if length < 8:
                        print("Password length should be at least 8 characters long")
                        continue
                    user.set_password(website, user.create_password(length))
                    break
                elif choice == "2":
                    password = input("Enter the password: ")
                    if len(password) < 8:
                        print("Password length should be at least 8 characters long")
                        continue
                    containsProhibited = user.contains_prohibited(password)
                    if containsProhibited:
                        print("Password contains prohibited characters")
                        continue
                    user.set_password(website, password)
                    break
                else:
                    print("Invalid choice")
                    continue
        elif choice == "3":
            website = input("Enter the website: ")
            credentials = user.get_credentials()
            if website not in credentials:
                print("Invalid website")
                continue
            old_password = input("Enter the old password: ")
            if old_password != credentials[website]:
                print("Old password is incorrect")
                continue
            new_password = input("Enter the new password: ")
            if len(new_password) < 8:
                print("Password length should be at least 8 characters long")
                continue
            user.change_password(website, old_password, new_password)
            continue
        elif choice == "4":
            print(user.list_websites())
            continue
        elif choice == "5":
            newName = input("Enter new name: ")
            user.name = newName
            name = newName
            print("Name successfully changed")
            continue
        elif choice == "6":
            secondChoice = input("Are you sure you want to delete all credentials? (yes/no):")
            if secondChoice == "yes":
                user.clear_passwords()
                print("All credentials successfully deleted")
            elif secondChoice == "no":
                print("Operation cancelled")  
            else:
                print("Invalid choice")
            continue    
        elif choice == "7":
            print("Goodbye")
            break
        else:
            print("Invalid choice")
            continue


if __name__ == "__main__":
    main()
