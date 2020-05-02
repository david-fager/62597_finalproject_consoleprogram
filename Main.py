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


def tablify_list(list):
    pt = PrettyTable(list[0].item)
    for element in list[1:]:
        pt.add_row(element.item)
    print(pt)


def user_menu():
    while True:
        print("")
        print("##################################################")
        print("#                                                #")
        print("#              USER MANAGEMENT MENU              #")
        print("#                                                #")
        print("#                > 1% ADD USER                   #")
        print("#                > 2% LIST USERS                 #")
        print("#                > 3% UPDATE USER                #")
        print("#                > 4% DELETE USER                #")
        print("#                > B BACK                        #")
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

        elif selection.upper() == "B":
            break
        else:
            print("Unrecognized input.")


def fridge_menu():
    while True:
        print("")
        print("##################################################")
        print("#                                                #")
        print("#             FRIDGE MANAGEMENT MENU             #")
        print("#                                                #")
        print("#              > 1 LIST FRIDGES                  #")
        print("#              > 2% ADD FRIDGE ITEM              #")
        print("#              > 3 LIST FRIDGE ITEMS             #")
        print("#              > 4% UPDATE FRIDGE ITEM           #")
        print("#              > 5% DELETE FRIDGE ITEM           #")
        print("#              > B BACK                          #")
        print("#                                                #")
        print("##################################################")
        selection = input("> ")
        if selection == "1":

            tablify_list(client.service.getAllFridgeRows())
            input("\nPRESS ENTER TO CONTINUE")

        elif selection == "2":
            print("Selected: 2")
        elif selection == "3":

            fridgeID = input("Fridge ID: ")

            tablify_list(client.service.getFridge(fridgeID))
            input("\nPRESS ENTER TO CONTINUE")

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
        print("#              > 1 ADD FOOD ITEM                 #")
        print("#              > 2 LIST FOOD ITEMS               #")
        print("#              > 3% UPDATE FOOD ITEM             #")
        print("#              > 4% DELETE FOOD ITEM             #")
        print("#              > B BACK                          #")
        print("#                                                #")
        print("##################################################")
        selection = input("> ")
        if selection == "1":

            print("Provide new food item information (Type 'D' to discard)")
            newItemID = input("ID: ")
            if newItemID.upper() == 'D':
                print("Discarding new type")
                continue
            newItemName = input("Name: ")
            if newItemName.upper() == 'D':
                print("Discarding new type")
                continue
            newItemTypeKey = input("Type Key (ID): ")
            if newItemTypeKey.upper() == 'D':
                print("Discarding new type")
                continue

            success = client.service.createItem(newItemID, newItemName, newItemTypeKey)
            if success:
                pass #print("Successfully created new type")
            else:
                pass #print("Failed creating new type")

            input("\nPRESS ENTER TO CONTINUE")

        elif selection == "2":

            tablify_list(client.service.getItems())
            input("\nPRESS ENTER TO CONTINUE")

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
        print("#              > 3 UPDATE FOOD TYPE              #")
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

            tablify_list(client.service.getTypes())
            input("\nPRESS ENTER TO CONTINUE")

        elif selection == "3":

            print("Provide updated food type information (Type 'D' to discard)")
            updateTypeID = input("The type's current ID: ")
            if updateTypeID.upper() == 'D':
                print("Discarding new type")
                continue
            updateTypeName = input("New name for the type: ")
            if updateTypeName.upper() == 'D':
                print("Discarding new type")
                continue
            updateTypeKeep = input("New keep (d) for the type: ")
            if updateTypeKeep.upper() == 'D':
                print("Discarding new type")
                continue
            updateTypeNewID = input("New ID for the type: ")
            if updateTypeNewID.upper() == 'D':
                print("Discarding new type")
                continue

            success = client.service.createType(updateTypeID, updateTypeName, updateTypeKeep, updateTypeNewID)
            if success:
                pass #print("Successfully created new type")
            else:
                pass #print("Failed creating new type")

            input("\nPRESS ENTER TO CONTINUE")

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
        print("#              > 1% MANAGE USERS                 #")
        print("#              > 2% MANAGE FRIDGES               #")
        print("#              > 3% MANAGE FOOD ITEMS            #")
        print("#              > 4 MANAGE FOOD TYPES             #")
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


main_menu()  # The call starting this program
