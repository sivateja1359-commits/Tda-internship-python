# Contact Management System

# Dictionary to store contacts
contacts = {}

def add_contact(name, phone):
    """Add a new contact to the contacts dictionary."""
    contacts[name] = phone
    print(f"Contact '{name}' added successfully!")

def search_contact(name):
    """Search for a contact by name."""
    if name in contacts:
        print(f"Name: {name}, Phone: {contacts[name]}")
    else:
        print(f"Contact '{name}' not found.")

def display_contacts():
    """Display all contacts."""
    if contacts:
        print("\n--- Contact List ---")
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")
    else:
        print("No contacts to display.")

def main():
    """Main function to run the contact management system."""
    while True:
        print("\n=== Contact Management System ===")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display All Contacts")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone)
        elif choice == "2":
            name = input("Enter name to search: ")
            search_contact(name)
        elif choice == "3":
            display_contacts()
        elif choice == "4":
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()