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
            print("View Contacts")
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

def viewContacts():
    
def searchContacts():
    
def editContact():

def deleteContact():
    

