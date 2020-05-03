from zeep import Client
from prettytable import PrettyTable
import urllib.request
import datetime

# Connecting via SOAP (Zeep in python) to the server
client = None
wsdl_local = "http://localhost:58008/my_fridge_soap_remote?WSDL"
wsdl_remote = "http://dist.saluton.dk:58008/my_fridge_soap_remote?WSDL"
website_address = "http://35.178.9.154"
connection_type = None

while True:
    print("Welcome to the admin terminal.")
    print("Are you connecting to a local or remote host?")
    print("(LOCAL/REMOTE)")
    connection_type = input("> ")
    if connection_type.upper() == "LOCAL":
        try:
            client = Client(wsdl_local)
        except:
            print("Local host connection failed")
            print("Check that you started the database program\n")
        else:
            print("Local host connection successful")
            break

    elif connection_type.upper() == "REMOTE":
        try:
            client = Client(wsdl_remote)
        except:
            print("Remote host connection failed")
            print("Check if you can connect to the WSDL:")
            print(wsdl_remote)
            print("Otherwise, it might be a server side error\n")
        else:
            print("Remote host connection successful")
            break

    else:
        print("Unrecognized input\n")


def tablify_list(list):
    if str(list) == "[]" or str(list) == "":
        print("Table is empty. See: " + str(list))
        return

    pt = PrettyTable(list[0].item)
    for element in list[1:]:
        pt.add_row(element.item)
    print(pt)


def assess_success(success, action, table):
    if success:
        print("Success " + action + " " + table)
    elif not success:
        print("Fail " + action + " " + table)
    else:
        print("Server sent no response on action")


def delete_table_element(delete_id, table):
    table = str(table).upper()
    if table == "USER":
        success = client.service.deleteUser(delete_id)
    elif table == "FRIDGE":
        success = client.service.deleteFridge(delete_id)
    elif table == "ITEM":
        success = client.service.deleteItem(delete_id)
    elif table == "TYPE":
        success = client.service.deleteType(delete_id)
    else:
        print("Unrecognized table")
        return

    if success:
        print("Successfully deleted " + table + " with ID: " + delete_id)
    elif not success:
        print("Failed deleting item with ID: " + delete_id)


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
        print("#              > 5 DELETE FRIDGE ITEM            #")
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

            print("Provide the ID of the fridge to list items for")
            tablify_list(client.service.getFridge(input("Fridge ID: ")))
            input("\nPRESS ENTER TO CONTINUE")

        elif selection == "4":

            print("Selected: 4")

        elif selection == "5":

            print("Provide the ID of the fridge you wish to delete")
            delete_table_element(input("ID: "), "fridge")
            input("\nPRESS ENTER TO CONTINUE")

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
        print("#              > 3 UPDATE FOOD ITEM              #")
        print("#              > 4 DELETE FOOD ITEM              #")
        print("#              > B BACK                          #")
        print("#                                                #")
        print("##################################################")
        selection = input("> ")
        if selection == "1":

            print("Provide new food item information (Type 'D' to discard)")
            new_item_id = input("ID: ")
            if new_item_id.upper() == 'D':
                print("Discarding new item")
                continue
            new_item_name = input("Name: ")
            if new_item_name.upper() == 'D':
                print("Discarding new item")
                continue
            new_item_type_key = input("Type Key (ID): ")
            if new_item_type_key.upper() == 'D':
                print("Discarding new item")
                continue

            assess_success(client.service.createItem(new_item_id, new_item_name, new_item_type_key),
                           "creating new", "item")
            input("\nPRESS ENTER TO CONTINUE")

        elif selection == "2":

            tablify_list(client.service.getItems())
            input("\nPRESS ENTER TO CONTINUE")

        elif selection == "3":

            print("Provide updated food item information (Type 'D' to discard)")
            update_item_id = input("The item's current ID: ")
            if update_item_id.upper() == 'D':
                print("Discarding item update")
                continue
            update_item_name = input("New name for the item: ")
            if update_item_name.upper() == 'D':
                print("Discarding item update")
                continue
            update_type_id = input("New type ID for the item: ")
            if update_type_id.upper() == 'D':
                print("Discarding item update")
                continue
            update_item_new_id = input("New ID for the item: ")
            if update_item_new_id.upper() == 'D':
                print("Discarding item update")
                continue

            assess_success(client.service.updateItem(update_item_id, update_item_name, update_type_id,
                                                     update_item_new_id), "updating", "item")
            input("\nPRESS ENTER TO CONTINUE")

        elif selection == "4":

            print("Provide the ID of the item you wish to delete")
            delete_table_element(input("ID: "), "item")
            input("\nPRESS ENTER TO CONTINUE")

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
            new_type_id = input("ID: ")
            if new_type_id.upper() == 'D':
                print("Discarding new type")
                continue
            new_type_name = input("Name: ")
            if new_type_name.upper() == 'D':
                print("Discarding new type")
                continue
            new_type_keep = input("Keep (d): ")
            if new_type_keep.upper() == 'D':
                print("Discarding new type")
                continue

            assess_success(client.service.createType(new_type_id, new_type_name, new_type_keep), "creating new", "type")
            input("\nPRESS ENTER TO CONTINUE")

        elif selection == "2":

            tablify_list(client.service.getTypes())
            input("\nPRESS ENTER TO CONTINUE")

        elif selection == "3":

            print("Provide updated food type information (Type 'D' to discard)")
            update_type_id = input("The type's current ID: ")
            if update_type_id.upper() == 'D':
                print("Discarding type update")
                continue
            update_type_name = input("New name for the type: ")
            if update_type_name.upper() == 'D':
                print("Discarding type update")
                continue
            update_type_keep = input("New keep (d) for the type: ")
            if update_type_keep.upper() == 'D':
                print("Discarding type update")
                continue
            update_type_new_id = input("New ID for the type: ")
            if update_type_new_id.upper() == 'D':
                print("Discarding type update")
                continue

            assess_success(client.service.createType(update_type_id, update_type_name, update_type_keep,
                                                     update_type_new_id), "updating", "type")
            input("\nPRESS ENTER TO CONTINUE")

        elif selection == "4":

            print("Provide the ID of the type you wish to delete")
            delete_table_element(input("ID: "), "type")
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
        print("#              > 1 MANAGE USERS                  #")
        print("#              > 2 MANAGE FRIDGES                #")
        print("#              > 3 MANAGE FOOD ITEMS             #")
        print("#              > 4 MANAGE FOOD TYPES             #")
        print("#              > 5 CHECK SERVER STATUS           #")
        print("#              > E EXIT                          #")
        print("#                                                #")
        print("##################################################")
        selection = input("> ")
        if selection == "1":
            user_menu()
        elif selection == "2":
            fridge_menu()
        elif selection == "3":
            item_menu()
        elif selection == "4":
            type_menu()
        elif selection == "5":

            handler=urllib.request.HTTPHandler(debuglevel=0)
            opener=urllib.request.build_opener(handler)
            urllib.request.install_opener(opener)

            # Checking if the database wsdl is up:
            if connection_type.upper() == "REMOTE":
                print("############# CHECKING DATABASE WSDL #############")
                try:
                    time_start = datetime.datetime.now()
                    wsdl_running = urllib.request.urlopen(wsdl_remote).getcode() == 200
                    time_end = datetime.datetime.now()
                    time_difference = time_end - time_start
                except:
                    wsdl_running = False

                if wsdl_running:
                    print("TRIED URL     - " + wsdl_remote)
                    print("STATUS        - is running")
                    print("RESPONSE TIME - " + str(round(time_difference.total_seconds() * 1000, 3)) + "ms")
                else:
                    print("TRIED URL     - " + wsdl_remote)
                    print("STATUS        - NOT running; the server or database program might be down")
                    print("RESPONSE TIME - N/A")
                print("")

            # Querying the database to see if it has any problems
            print("########### TEST QUERYING THE DATABASE ###########")
            try:
                time_start = datetime.datetime.now()
                database_tables = client.service.getTables()
                time_end = datetime.datetime.now()
                time_difference = time_end - time_start
            except:
                database_tables = None

            if database_tables:
                print("TRIED METHOD  - getTables()")
                print("STATUS        - success")
                print("RESPONSE TIME - " + str(round(time_difference.total_seconds() * 1000, 3)) + "ms")
            elif str(database_tables) == "[]":
                print("TRIED METHOD  - getTables()")
                print("STATUS        - failed; program is responsive, but database queried unsuccessfully")
                print("RESPONSE TIME - N/A")
            else:
                print("TRIED METHOD  - getTables()")
                print("STATUS        - failed; program is unresponsive, program or server might be down")
                print("RESPONSE TIME - N/A")
            print("")

            # Checking if the website is up and running
            print("################ CHECKING WEBSITE ################")
            try:
                time_start = datetime.datetime.now()
                website_running = urllib.request.urlopen(website_address).getcode() == 200
                time_end = datetime.datetime.now()
                time_difference = time_end - time_start
            except:
                website_running = False

            if website_running:
                print("TRIED URL     - " + website_address)
                print("STATUS        - is running")
                print("RESPONSE TIME - " + str(round(time_difference.total_seconds() * 1000, 3)) + "ms")
            else:
                print("TRIED URL     - " + website_address)
                print("STATUS        - NOT running; the server or webserver program might be down")
                print("RESPONSE TIME - N/A")

            input("\nPRESS ENTER TO CONTINUE")

        elif selection.upper() == "E":
            exit(0)
        else:
            print("Unrecognized input.")


main_menu()  # The call starting this program
