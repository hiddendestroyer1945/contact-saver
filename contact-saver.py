class ContactSaver:

    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name = input("Enter name: ")
        place = input("Enter place: ")
        email = input("Enter email: ")
        mobile = input("Enter mobile number: ")
        self.contacts[name] = {
            "place": place,
            "email": email,
            "mobile": mobile
        }
        print("Contact added successfully!")

    def find_contact(self):
        name = input("Enter name to find: ")
        if name in self.contacts:
            contact = self.contacts[name]
            print(f"Name: {name}")
            print(f"Place: {contact['place']}")
            print(f"Email: {contact['email']}")
            print(f"Mobile: {contact['mobile']}")
        else:
            print("Contact not found!")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts found!")
        else:
            for name, contact in self.contacts.items():
                print(f"Name: {name}")
                print(f"Place: {contact['place']}")
                print(f"Email: {contact['email']}")
                print(f"Mobile: {contact['mobile']}")
                print("------------------------")


def main():
    contact_saver = ContactSaver()
    while True:
        print("1. Add Contact")
        print("2. Find Contact")
        print("3. Display Contacts")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            contact_saver.add_contact()
        elif choice == "2":
            contact_saver.find_contact()
        elif choice == "3":
            contact_saver.display_contacts()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
