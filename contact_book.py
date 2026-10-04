def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email
    }
    print("Contact added successfully!\n")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.\n")
        return

    print("\n--- Contact Book ---")
    for name, details in contacts.items():
        print(f"Name : {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
        print("-" * 25)
    print()


def search_contact(contacts):
    name = input("Enter name to search: ").strip()

    if name in contacts:
        details = contacts[name]
        print("\nContact Found!")
        print(f"Name : {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}\n")
    else:
        print("Contact not found.\n")


def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!\n")
    else:
        print("Contact not found.\n")


def main():
    contacts = {}

    while True:
        print("===== Contact Book =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Thank you for using Contact Book!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
