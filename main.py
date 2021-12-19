# Importing Libraries

from pysqlitecipher import sqlitewrapper
import os, sys
from tabulate import tabulate

# Importing config
from extra import *


# Checking is the database already exists
if not os.path.isfile('noPasswordsHere.db'):
    # Welcome Message
    print("="*101)
    print("="*46, end=' ')
    print("Welcome", end=" ")
    print("="*46)
    print("="*101, end="\n\n")
    print("Set Up a master Password. ")

    # Validating the password Strength
    passwd = validate()

    # Creating the Encrypted database
    obj = sqlitewrapper.SqliteCipher(dataBasePath="noPasswordsHere.db" , checkSameThread=False , password=passwd)

    # Table Columns
    colList = [
        ["id" , "TEXT"],
        ["passwd" , "TEXT"],
        ["des" , "TEXT"],
    ]

    # Creating the table
    obj.createTable('data' , colList , makeSecure=True , commit=True)


else:
    # Welcome Message
    print("="*105)
    print("="*46, end=' ')
    print("Hello again", end=" ")
    print("="*46)
    print("="*105, end="\n\n")

    # Master Password Validation
    count = 3
    while count > 0:
        passwd = input("Please Enter your Master Password : ")
        try:
            obj = sqlitewrapper.SqliteCipher(dataBasePath="noPasswordsHere.db" , checkSameThread=False , password=passwd)
            break
        except:
            print("Wrong Password. Try Again")
            count -= 1
    else:
        print("Too Many invalid attempts")
        sys.exit(0)



while True:
    while True:
        # Action Menu (Main Loop)
        print("")
        print("0. Get Data")
        print("1. Insert New Data")
        print("2. Change Data")
        print("3. Delete Data")
        print("4. Change Master Password")
        print("5. Exit", end="\n\n")
        try:
            op = int(input("Please Select : "))
            if op > 5 or op < 0:
                print("Incorrect Input")
                continue
            break
        except:
            print("Please Enter the number.")

    if op ==  0:
        print("")
        try:
            lst = []
            # Getting table data
            for dat in obj.getDataFromTable('data' , raiseConversionError = True , omitID = False)[1]:
                lst.append([dat[1], dat[2], dat[3]])

            # Printing the table
            print(tabulate(lst, headers=["ID", "Password", "Description"], tablefmt='orgtbl'))

        except:
            print("Please Insert Data First")

    if op == 1:
        # Getting Input Data from the user
        id = input("Please Enter the ID : ")
        pwd = input("Please Enter the Password : ")
        des = input("Please Enter the Description : ")
        inList = [id, pwd, des]

        # Inserting data to the table
        obj.insertIntoTable('data' , inList , commit = True)

        print("Successfully Saved")

    if op == 2:

        while True:
            print("")
            # Getting Data from the database
            for dat in obj.getDataFromTable('data' , raiseConversionError = True , omitID = False)[1]:
                print(f"{dat[0]}. {dat[1]} -->  {dat[3]}")
            try:
                ch = int(input("Please Select : "))
                break
            except:
                print("Please Enter the number.")


        while True:
            # Getting data from the user
            print("")
            print("What do you wanna change: ")
            print("1. ID")
            print("2. Password")
            print("3. Description")
            print("please Select: ")

            try:
                fl = int(input("Please Select : "))
                break
            except:
                print("Please Enter the number.")

        up = input("Please Enter the new Value: ")

        # Updating the Database
        obj.updateInTable('data' , ch , cols[fl] , up , commit = True , raiseError = True)

        print("")
        print("Successfully Updated")

    if op == 3:
        while True:
            print("")
            # Getting data from the database
            for dat in obj.getDataFromTable('data' , raiseConversionError = True , omitID = False)[1]:
                print(f"{dat[0]}. {dat[1]} -->  {dat[3]}")
            try:
                ch = int(input("Please Select : "))
                break
            except:
                print("Please Enter the number.")

        # Deleting Records
        obj.deleteDataInTable('data' , ch , commit = True , raiseError = True , updateId = True)

        print("")
        print("Successfully Deleted")

    if op == 4:
        count = 3
        while count > 0:
            # Getting the Master Password from the user
            passwd = input("Please Enter your Master Password : ")
            try:
                # Checking the password
                obj = sqlitewrapper.SqliteCipher(dataBasePath="noPasswordsHere.db" , checkSameThread=False , password=passwd)
                break
            except:
                print("Wrong Password. Try Again")
                count -= 1
        else:
            print("Too Many invalid attempts")
            sys.exit(0)

        # Validating the new password
        newpass = validate()
        # Changing the password
        for i in obj.changePassword(newpass):
            pass

        print("Successfully Changed the Password")

    if op == 5:
        # Exiting the programme
        sys.exit(0)