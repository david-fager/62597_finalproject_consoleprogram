from zeep import Client
from prettytable import PrettyTable

# Connecting via SOAP (Zeep in python) to the server
client = None
while True:
    print("Welcome to the admin terminal.")
    print("Are you connecting to a local or remote host?")
    print("(LOCAL/REMOTE)")
    answer = input("> ")
    if answer.upper() == "LOCAL":
        try:
            client = Client('http://localhost:58008/my_fridge_soap_remote?WSDL')
        except:
            print("Local host connection failed\n")
        else:
            print("Local host connection successful")
            break

    elif answer.upper() == "REMOTE":
        try:
            client = Client('http://dist.saluton.dk:58008/my_fridge_soap_remote?WSDL')
        except:
            print("Remote host connection failed\n")
        else:
            print("Remote host connection successful")
            break

    else:
        print("Unrecognized input\n")


def fridge_menu():
    while True:
        print("")
        print("##################################################")
        print("#                                                #")
        print("#             FRIDGE MANAGEMENT MENU             #")
        print("#                                                #")
        print("#              > 1% LIST FRIDGES                 #")
        print("#              > 2% ADD FRIDGE ITEM              #")
        print("#              > 3% LIST FRIDGE ITEMS            #")
        print("#              > 4% UPDATE FRIDGE ITEM           #")
        print("#              > 5% DELETE FRIDGE ITEM           #")
        print("#              > B BACK                          #")
        print("#                                                #")
        print("##################################################")
        selection = input("> ")
        if selection == "1":
            print("Selected: 1")
        elif selection == "2":
            print("Selected: 2")
        elif selection == "3":
            print("Selected: 3")
        elif selection == "4":
            print("Selected: 4")
        elif selection == "5":
            print("Selected: 5")
        elif selection.upper() == "B":
            break
        else:
            print("Unrecognized input.")


def item_menu():
    while True:
        print("")
        print("##################################################")
        print("#                                                #")
        print("#            FOOD ITEM MANAGEMENT MENU           #")
        print("#                                                #")
        print("#              > 1% ADD FOOD ITEM                #")
        print("#              > 2% LIST FOOD ITEMS              #")
        print("#              > 3% UPDATE FOOD ITEM             #")
        print("#              > 4% DELETE FOOD ITEM             #")
        print("#              > B BACK                          #")
        print("#                                                #")
        print("##################################################")
        selection = input("> ")
        if selection == "1":
            print("Selected: 1")
        elif selection == "2":
            client.service.getItems()
        elif selection == "3":
            print("Selected: 3")
        elif selection == "4":
            print("Selected: 4")
        elif selection.upper() == "B":
            break
        else:
            print("Unrecognized input.")


def type_menu():
    while True:
        print("")
        print("##################################################")
        print("#                                                #")
        print("#            FOOD TYPE MANAGEMENT MENU           #")
        print("#                                                #")
        print("#              > 1 ADD FOOD TYPE                 #")
        print("#              > 2 LIST FOOD TYPES               #")
        print("#              > 3% UPDATE FOOD TYPE             #")
        print("#              > 4 DELETE FOOD TYPE              #")
        print("#              > B BACK                          #")
        print("#                                                #")
        print("##################################################")
        selection = input("> ")
        if selection == "1":
            print("Provide new food type information (Type 'D' to discard)")
            newTypeId = input("ID: ")
            if newTypeId.upper() == 'D':
                print("Discarding new type")
                continue
            newTypeName = input("Name: ")
            if newTypeName.upper() == 'D':
                print("Discarding new type")
                continue
            newTypeKeep = input("Keep (d): ")
            if newTypeKeep.upper() == 'D':
                print("Discarding new type")
                continue

            success = client.service.createType(newTypeId, newTypeName, newTypeKeep)
            if success:
                print("Successfully created new type")
            else:
                print("Failed creating new type")

            input("\nPRESS ENTER TO CONTINUE")
        elif selection == "2":
            types = client.service.getTypes()

            pt = PrettyTable(types[0].item)
            for type in types[1:]:
                pt.add_row(type.item)
            print(pt)

            input("\nPRESS ENTER TO CONTINUE")
        elif selection == "3":
            print("Selected: 3")
        elif selection == "4":
            print("Provide the ID of the type you wish to delete")
            delete_id = input("ID: ")
            success = client.service.deleteType(delete_id)

            if success:
                print("Successfully deleted type with ID: " + delete_id)
            else:
                print("Failed deleting type with ID: " + delete_id)

            input("\nPRESS ENTER TO CONTINUE")
        elif selection.upper() == "B":
            break
        else:
            print("Unrecognized input.")


def main_menu():
    while True:
        print("")
        print("##################################################")
        print("#                                                #")
        print("#                   ADMIN MENU                   #")
        print("#                                                #")
        print("#              > 1% MANAGE FRIDGES               #")
        print("#              > 2% MANAGE FOOD ITEMS            #")
        print("#              > 3 MANAGE FOOD TYPES             #")
        print("#              > E EXIT                          #")
        print("#                                                #")
        print("##################################################")
        selection = input("> ")
        if selection == "1":
            fridge_menu()
        elif selection == "2":
            item_menu()
        elif selection == "3":
            type_menu()
        elif selection.upper() == "E":
            exit(0)
        else:
            print("Unrecognized input.")


print("\nREAD: menu items with a % is not yet implemented")
input("PRESS ENTER TO CONTINUE")

main_menu()  # The call starting this program
