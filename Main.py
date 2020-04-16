from zeep import Client


# client = Client('http://localhost:58008/hangman_remote?WSDL')
# asd = client.service.informConnect()
# print(asd)

def fridgeMenu():
    while True:
        print("")
        print("##################################################")
        print("#                                                #")
        print("#             FRIDGE MANAGEMENT MENU             #")
        print("#                                                #")
        print("#              > 1 LIST FRIDGES                  #")
        print("#              > 2 ADD FRIDGE ITEM               #")
        print("#              > 3 LIST FRIDGE ITEMS             #")
        print("#              > 4 UPDATE FRIDGE ITEM            #")
        print("#              > 5 DELETE FRIDGE ITEM            #")
        print("#              > 6 GO BACK                       #")
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
        elif selection == "6":
            break
        else:
            print("Unrecognized input.")


def itemMenu():
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
        print("#              > 5 GO BACK                       #")
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
            break
        else:
            print("Unrecognized input.")


def typeMenu():
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
        print("#              > 5 GO BACK                       #")
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
            break
        else:
            print("Unrecognized input.")


def mainMenu():
    while True:
        print("")
        print("##################################################")
        print("#                                                #")
        print("#                   ADMIN MENU                   #")
        print("#                                                #")
        print("#              > 1 MANAGE FRIDGES                #")
        print("#              > 2 MANAGE FOOD ITEMS             #")
        print("#              > 3 MANAGE FOOD TYPES             #")
        print("#                                                #")
        print("##################################################")
        selection = input("> ")
        if selection == "1":
            fridgeMenu()
        elif selection == "2":
            itemMenu()
        elif selection == "3":
            typeMenu()
        else:
            print("Unrecognized input.")


mainMenu()
