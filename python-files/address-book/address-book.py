# import json


# def address_booking():

#     address_book = {}

#     try:
#         user_input = input(
#             "Would you like to view existing contacts or add a new contact? \n Input 'v' for view or 'a' for add: ").lower()

#         if user_input == 'v':
#             if address_book:

#                 contact_name = input(
#                     f"Enter the name of the contact: ").capitalize()
#                 if contact_name in address_book:
#                     print(
#                         f"Contact details for {contact_name}: {address_book[contact_name]}")
#                 else:
#                     print("Contact does not exist")

#             else:
#                 print("Your address_book is empty")

#         elif user_input == 'a':
#             while True:
#                 name = input("Enter contact name: ").capitalize()
#                 phone_number = int(input("Enter contact phone number: "))
#                 address = input("Enter contact address: ").capitalize()
#                 relationship = input(
#                     "Enter relationship with contact: ").capitalize()

#                 address_book[name] = {
#                     'phone_number': phone_number,
#                     'address': address,
#                     'relationship': relationship
#                 }
#                 with open("contact.json", "w+") as f:
#                     json.dump(address_book, f)
#                 print(address_book)
#                 print(f"Contact '{name}' added successfully.")

#                 another_contact = input(
#                     "Do you want to add another contact? (y/n): ").lower()
#                 if another_contact != 'y':
#                     break

#         elif user_input == 'k':
#             pass

#         else:
#             print("Invalid input. Please enter 'v' to view or 'a' to add.")

#     except KeyboardInterrupt:
#         print(f"\n Error occurred")
#     except ValueError as e:
#         print("Invalid input, enter a number")


# address_booking()


import json
import os


def address_booking():

    address_book = {}

    if os.path.getsize("contact.json") == 0:
        with open("contact.json", "w") as file:
            file.write(json.dumps(address_book))
    with open("contact.json", 'r') as f:
        address_book = json.loads(f.read())
    try:
        user_input = input(
            "Would you like to view existing contacts or add a new contact? \n Input 'v' for view or 'a' for add: ")

        if user_input.lower() == 'v':

            contact_name = input(
                f"Enter the name of the contact: ").capitalize()
            if contact_name in address_book:
                print(
                    f"Contact details for {contact_name}: {address_book[contact_name]}")
            else:
                print("Contact does not exist")

        elif user_input.lower() == 'a':
            while True:
                name = input("Enter contact name: ").capitalize()
                phone_number = int(input("Enter contact phone number: "))
                address = input("Enter contact address: ").capitalize()
                relationship = input(
                    "Enter relationship with contact: ").capitalize()

                # Create a new contact dictionary
                new_contact = {name: {
                    'phone_number': phone_number,
                    'address': address,
                    'relationship': relationship
                }}

                # address_book[name] = {
                #     'phone_number': phone_number,
                #     'address': address,
                #     'relationship': relationship
                # }

                # Add the new contact to address_book
                address_book.update(new_contact)

                with open("contact.json", "w") as f:
                    # Dump the entire address_book to the JSON file
                    f.write(json.dumps(address_book))

                print(address_book)
                print(f"Contact '{name}' added successfully.")

                another_contact = input(
                    "Do you want to add another contact? (y/n): ").lower()
                if another_contact != 'y':
                    break

        elif user_input == 'k':
            pass

        else:
            print("Invalid input. Please enter 'v' to view or 'a' to add.")

    except KeyboardInterrupt:
        print(f"\n Error occurred")


address_booking()
