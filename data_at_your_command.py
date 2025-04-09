#Data At Your Command Assignment
#By Payton Mouzin

def clearScreen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
import keyboard
import tkinter as tk
from tkinter import messagebox
import time
import webbrowser

def on_exit():
    for _ in range(2):
        messagebox.showerror("Error", "GPU driver failed (0x69C00L)")
        time.sleep(0.5)

    messagebox.showinfo("System", "Attempting to refresh graphics driver...")

    keyboard.press_and_release('win+ctrl+shift+b')

    time.sleep(2) 

    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    messagebox.showinfo("Gotcha", "Graphics restored. You’ve been Rickrolled.")


    
def main():
    #Clear the Screen
    clearScreen()
    
    #Welcome Message
    menuSelection = menuMessage()
        
    
    #Main Menu Loop
    while menuSelection != "5":
        if menuSelection == "1":
            print("Add a Contact")
            addContact()
        elif menuSelection == "2":
            view_contacts()
        elif menuSelection == "3":
            print("Search Contacts")
            searchContacts()
        elif menuSelection == "4":
            print("Delete a Contact")
            deleteContact()
        elif menuSelection == "5":
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
    print("4. Delete a Contact")
    print("5. Exit")
    print("---------------------")
    try:
        userinput = input("Please select an option (1-5): ")
        return userinput
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
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
    with open("contact_data.json", 'r+') as f:
        data = json.load(f)
        data.append(contact)
        f.seek(0)
        json.dump(data, f, indent=4)
        print("Contact added successfully!")
        #Close the file
        f.close()
        
    print("Contact added successfully!")


import json

def view_contacts():
    try:
        with open('contact_data.json', 'r') as file:
            contacts = json.load(file)
            
            for contact in contacts:
                print(f"Name: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
                print("-" * 30)
            
            input("Press Enter to return to the menu...")
            
    except FileNotFoundError:
        print("Contact file not found!")
    except json.JSONDecodeError:
        print("Error reading JSON file. Check if the format is correct.")


def searchContacts():
    search_name = input("Enter the name of the contact you want to search for: ")
    
    try:
        with open('contact_data.json', 'r') as file:
            contacts = json.load(file)
            
            while True:
                for contact in contacts:
                    if contact['name'].lower() == search_name.lower():
                        print(f"Name: {contact['name']}")
                        print(f"Phone: {contact['phone']}")
                        print(f"Email: {contact['email']}")
                        break
                else:
                    print("Contact not found.")
                    break
                input("Press Enter to return to the menu...")
            
    except FileNotFoundError:
        print("Contact file not found!")
    except json.JSONDecodeError:
        print("Error reading JSON file. Check if the format is correct.")

def deleteContact():
    delete_name = input("Enter the name of the contact you want to delete: ")
    
    try:
        with open('contact_data.json', 'r') as file:
            contacts = json.load(file)
            
        for contact in contacts:
            if contact['name'].lower() == delete_name.lower():
                contacts.remove(contact)
                print(f"Contact '{delete_name}' deleted successfully.")
                break
        else:
            print("Contact not found.")
        
        with open('contact_data.json', 'w') as file:
            json.dump(contacts, file, indent=4)
            
    except FileNotFoundError:
        print("Contact file not found!")






main()
on_exit()



