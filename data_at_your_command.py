#Data At Your Command Assignment
#By Payton Mouzin

def clearScreen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
def main():
    #Clear the Screen
    clearScreen()
    
    #Welcome Message
    menuSelection = menuMessage()
        
    
    #Main Menu Loop
    while menuSelection != "6":
        if menuSelection == "1":
            print("Add a Contact")
            addContact()
        elif menuSelection == "2":
            viewContacts()
        elif menuSelection == "3":
            print("Search Contacts")
            searchContacts()
        elif menuSelection == "4":
            print("Edit a Contact")
            editContact()
        elif menuSelection == "5":
            print("Delete a Contact")
            deleteContact()
        elif menuSelection == "6":
            print("Exiting...")
        #Clear the Screen and display the menu again
        clearScreen()
        menuSelection = menuMessage()

# This displays the Main Menu, and prompts the user for input
def menuMessage():
    print("  Contact Database")
    print("---------------------")
    print("1. Add a Contact")
    print("2. View Contacts")
    print("3. Search Contacts")
    print("4. Edit a Contact")
    print("5. Delete a Contact")
    print("6. Exit")
    print("---------------------")
    try:
        userinput = input("Please select an option (1-6): ")
        return userinput
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")
        clearScreen()
        menuMessage()

def addContact():
    import json
    #Contact dictionary
    contact = {}
    
    #Get contact information from user
    contact["name"] = input("Enter the contact's name: ")
    contact["phone"] = input("Enter the contact's phone number: ")
    contact["email"] = input("Enter the contact's email address: ")
    
    #Open the json file and append the new contact
    with open("contacts.json", 'r+') as f:
        data = json.load(f)
        data.append(contact)
        f.seek(0)
        json.dump(data, f, indent=4)
        print("Contact added successfully!")
        #Close the file
        f.close()
        
    print("Contact added successfully!")


def viewContacts():
    import json
    with open('contact_data.json', 'r') as json_file:
        contact_data = json.load(json_file)
        for contact in contact_data:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print("---------------------")
        
        print("Contacts viewed successfully!")

    





main()