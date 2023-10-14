# Define a list of contacts as tuples (name, email, phone)
contacts = [
    ("John Doe", "johndoe@example.com", "1234567890"),
    ("Jane Smith", "janesmith@example.com", "0987654321"),
    ("Alice Johnson", "alicejohnson@example.com", "9876543210")
]

# Function to add a new contact
def add_contact():
    name = input("Enter the name: ")
    email = input("Enter the email: ")
    phone = input("Enter the phone number: ")
    contact = (name, email, phone)
    contacts.append(contact)
    print(f"Contact {name} added successfully.")

# Function to search for a contact
def search_contact():
    name = input("Enter the name to search: ")
    for contact in contacts:
        if contact[0].lower() == name.lower():
            print(f"Name: {contact[0]}")
            print(f"Email: {contact[1]}")
            print(f"Phone: {contact[2]}")
            return
    print("Contact not found.")

# Function to display all contacts
def display_contacts():
    print("Contacts:")
    for contact in contacts:
        print(f"Name: {contact[0]}")
        print(f"Email: {contact[1]}")
        print(f"Phone: {contact[2]}")
        print()

while True:
    print("""Tell me what do you want to do: 
        \nType 1 to add contact 
        Type 2 to search contact
        \nType 3 to display all contacts
        \nType 0 to exit.""")
    choice = int(input())
    if choice == 1:
        add_contact()
    elif choice == 2:
        search_contact()
    elif choice == 3:
        display_contacts()
    else:
        print("Thanks for your time!")
        break











