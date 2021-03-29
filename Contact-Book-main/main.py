
# This is basic contacts book that saves its contains on txt file.

import os # To Get current file path.
import shutil # used to move the file.
import time

# user selection function helps user to select option from many options

def user_selection():
    # press 0) to Exit. 
    # press 1) For new users only.    
    # press 2) For adding new contact.
    # press 3) View all contacts.     
    # press 4) Create BackUp.
    # press 5) FAQs section.
    os.system("cls")
    print("\n\n\t\tContact Book Ver. 2.0\n\npress 0) to Exit. \npress 1) For new users only.\npress 2) For adding new contact.\npress 3) View all contacts.\npress 4) Create BackUp.\npress 5) FAQs section.\n")
    
    try: # try and except is used here to prevent breaking program when errors occur.
        inp = int(input("Enter you're choices: "))
    except:
        print("\nERROR: Unable to read try again\n")
        inp = input("Do you want to try again? Y = Yes | N = No ").upper()
        if inp[0] == "Y":
            user_selection()
    if inp == 0:
        print("Thank you for using my program. Now you can close the window")
        time.sleep(10)
    elif inp == 1:
        new_user()
    elif inp == 2:
        add_new_contact()
    elif inp == 3:
        view_all_contacts()
    elif inp == 4:
        create_backUp()
    elif inp == 5:
        FAQs_section()
    else:
        print("\nERROR: Unable to proceed try again\n")
        inp = input("Do you want to try again? Y = Yes | N = No ").upper()
        if inp[0] == "Y":
            user_selection()
        else:
            print("Thank you for using my program. Now you can close the window")
            time.sleep(10)



# FAQs Section
def FAQs_section():
    os.system("cls")
    print("\nYou have selected FAQs Section option\n\n1. What is source file and where I can find it?\nAns: Source file is a file that is created when you select press 1) For new users only and it is used to save all your contacts data. You can find it where this program is located.\n\n2. I cannot find source file.\nAns: Source file is created when you select (press 1) For new users only) option. If you have selected this option and still unable to find your source file where this program is located do not worry, select press 4) Create BackUp and copy all of source file contains to new file and move your file to your desired location or at default location at C:\n\n3. Is this program safe?\nAns: Yes! This program runs on your machine locally and saves data locally (only on your machine)\n\n4. I am unable to find my question / answer in FAQs section.\nAns: Do not worry we got that covered too! Contact me on email id: 5kchqvw6r@relay.firefox.com and type subject like I am unable to find my question / answer in FAQs section. To get quick reply. If you're sending an attachment through given email id make sure the attachment size is less than 150KB.")
    repeat()



# Simple repeat loop used to add multiple contacts
def repeat_add_contacts():
    inp = input("\nGreat! Do you want to add another contact? if yes = y | no = n: ").upper()
    if inp[0] == "Y":
        add_new_contact()
    else:
        repeat()



# Simple repeat loop used to loop program
def repeat():
    inp = input("\nDo you want to open Main menu? if yes = y | no = n: ").upper()
    if inp[0] == "Y":
        user_selection()
    else:
        print("Thank you for using my program. Now you can close the window.")
        time.sleep(10)



# This function will add new user's name to txt file and it will also delete previous data
def new_user():
    
    os.system("cls")
    print("\nNOTE: Run this option only if you are running this program for first time or your source file is deleted / missing. This option will create New Source file and it will overwrite / Delete previous Source file (if exist).\n")
    inp = input("Do you want to continue? Y = continue | N = Go back to Main menu: ").upper()

    if inp[0]=="N":
        user_selection()

    else:
        os.system("cls")
        name = input("\nyou have selected new user option.\nEnter your name here: ")
    
        f = open("source.txt", "w+")  # to find this file search in same directory where you have saved the program.
        f.write(f"\t{name}'s Contacts List\n")
        f.close()
        os.system("cls")
        inp = int(input("\nDone!\nPress 0) To exit current mode\nPress 1) To add contact\n"))

        if inp == 1:
            add_new_contact()
        else:
            repeat()



# This function will add new contacts
def add_new_contact():
    
    os.system("cls")
    print("\nYou have selected add contacts option\n")

    cont_name = input("Enter Contact name here: ")
    phone_no = input("Enter Contact's phone number here: ")
    e_mail = input("Enter Contact's E-mail here: ")
    address = input("Enter Contact's address here: ")
    f = open("source.txt", "a+")
    f.write(f"Name: {cont_name}\n")
    f.write(f"Phone no.: {phone_no}\n")
    f.write(f"E-mail: {e_mail}\n")
    f.write(f"Address: {address}\n\n")
    f.close()
    os.system("cls")
    repeat_add_contacts()



# This function will view all contacts in command line
def view_all_contacts():

    os.system("cls")
    try: # try and except is used here to prevent breaking program when errors occur.
        print("\nYou have selected view all contacts option\n")
        f = open("source.txt", "r")
        print(f.read())
        f.close()
        repeat()
    except:
        print("\nERROR: Unable to read data. Don't worry there are some possibilities given below: \n1.Source file does not exists. Please select 'press 1) for new users only' to resolve this issue from main menu.\n")
        inp = input("Do you want to open main menu? Y = Yes | N = No ").upper()
        if inp[0] == "Y":
            user_selection()
            

# This function will create backup and move it to desired location or default location.
def create_backUp():

    os.system("cls")
    print("\nYou have Selected Create BackUp Option:\n")
    
    file_name = input("Enter name of your New BackUp file: ")
    file_name += ".txt" 
    
    path = input("\nEnter file path of your choice or enter N to use default path.\nDefault path will be C:").upper()
    
    if path != "N": # if input is not equal to "N" execute following code (specified location).
        try: # try and except is used here to prevent breaking program when errors occur.
            f = open("source.txt", "r")
            f1 = open(file_name, "w")
            f1.write(f.read())
            f.close()
            f1.close()
            source_path = os.getcwd()
            source_path += f"\\{file_name}"
            shutil.move(source_path, f'{path}//{file_name}')
            os.system("cls")
            print(f"\nDone! your {file_name} is saved at {path}\n")
            repeat()
        except:
            print(f"\nERROR: Something went wrong. Don't worry there are some possibilities given below: \n1. File already exists in {path}.\n2. Given {path} is wrong / Does not exists.\n3. Source file does not exists\n")
            inp = input("Do you want to try again? Y = Yes | N = No ").upper()
            if inp[0] == "Y":
                create_backUp()
            else:
                repeat()

    else: # if input is equal to "N" execute following code (Default location (C:) Drive).
        try: # try and except is used here to prevent breaking program when errors occur.
            f = open("source.txt", "r")
            f1 = open(file_name, "w")
            f1.write(f.read())
            f.close()
            f1.close()
            source_path = os.getcwd()
            source_path += f"\\{file_name}"
            shutil.move(source_path, f'C://{file_name}')
            os.system("cls")
            print(f"\nDone! your {file_name} is saved at C:\n")
            repeat()
        except:
            print("\nERROR: Something went wrong. Don't worry there are some possibilities given below: \n1.File already exists in C: .\n2.Given path is wrong / Does not exists.\n3. Source file does not exists\n")
            inp = input("Do you want to try again? Y = Yes | N = No ").upper()
            if inp[0] == "Y":
                create_backUp()
            else:
                repeat()


user_selection()
