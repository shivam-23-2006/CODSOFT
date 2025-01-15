contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print(f"Contact {name} added.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"Name: {name}, Phone: {contacts[name]}")
    else:
        print(f"No contact found for {name}.")

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        print("Exiting Contact Book.")
        break
    else:
        print("Invalid choice. Please try again.")
