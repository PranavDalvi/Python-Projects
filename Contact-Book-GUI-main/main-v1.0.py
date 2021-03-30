
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("Contact Book (Ver. 1.0)")



def add_contacts():

    global name, phone, mail, dob, address, note

    top = Toplevel()
    top.title("Add new contact")

    nameLabel = Label(top, text= "Enter Full Name: ")
    name = Entry(top)

    phoneLabel = Label(top, text= "Enter Contact Number: ")
    phone = Entry(top)

    mailLabel = Label(top, text= "Enter E-mail ID: ")
    mail = Entry(top)

    dobLabel = Label(top, text= "Enter Date of birth: ")
    dob = Entry(top)

    addressLabel = Label(top, text= "Enter Address: ")
    address = Entry(top)

    noteLabel = Label(top, text= "Enter Note: ")
    note = Entry(top)

    button_save = Button(top, text = "Save Contact", width= 13, command = lambda:(saveContact()))
    button_clear = Button(top, text = "Clear", width= 13, command = lambda:(clear()))

    nameLabel.grid(row= 0, column= 0, padx= 5, pady=5)
    name.grid(row= 0, column= 1, padx= 5, pady=5)
    
    phoneLabel.grid(row= 1, column= 0, padx= 5, pady=5)
    phone.grid(row= 1, column= 1, padx= 5, pady=5)
    
    mailLabel.grid(row= 2, column= 0, padx= 5, pady=5)
    mail.grid(row= 2, column= 1, padx= 5, pady=5)
    
    dobLabel.grid(row= 3, column= 0, padx= 5, pady=5)
    dob.grid(row= 3, column= 1, padx= 5, pady=5)
    
    addressLabel.grid(row= 4, column= 0, padx= 5, pady=5)
    address.grid(row= 4, column= 1, padx= 5, pady=5)
    
    noteLabel.grid(row= 5, column= 0, padx= 5, pady=5)
    note.grid(row= 5, column= 1, padx= 5, pady=5)

    button_save.grid(row= 6, column= 1, padx= 10, pady=10)
    button_clear.grid(row= 6, column= 0, padx= 10, pady=10)



# Save button function
def saveContact():

    # To check inappropriate null values
    if name.get() == "":
        messagebox.showerror(title="Error", message="Sorry, You cannot keep Name as null value")
    elif phone.get() == "":
        messagebox.showerror(title="Error", message="Sorry, You cannot keep Phone Number as null value")
    elif mail.get() == "":
        messagebox.showerror(title="Error", message="Sorry, You cannot keep E-mail as null value")
    else:
        # Saving contact into the file
        source_file = open("source.txt", "a+")
        source_file.write(f"Name: {name.get()}\n")
        source_file.write(f"Phone no.: {phone.get()}\n")
        source_file.write(f"E-mail: {mail.get()}\n")
        source_file.write(f"Date of Birth: {dob.get()}\n")
        source_file.write(f"Address: {address.get()}\n")
        source_file.write(f"Note: {note.get()}\n\n")
        source_file.close()
        # Message Box for end user's relief
        messagebox.showinfo(title="Successful", message="You're contact has been saved")
    clear()



# Clear function to clear user's input
def clear():

    name.delete(0, END),
    phone.delete(0, END),
    mail.delete(0, END),
    dob.delete(0, END),
    address.delete(0, END),
    note.delete(0, END)
  


# view all function to read contacts from source.txt
def viewAll():

    top = Toplevel()
    top.title("View all")
    source_file = open("source.txt", "r")
    data = Label(top, text =f"{source_file.read()}")
    source_file.close()

    data.grid(row = 1, column= 1, rowspan= 10, columnspan= 5, padx= 50, pady=10)



# Backup function
def backup():
    backup_file = filedialog.asksaveasfilename(defaultextension = "*", initialdir = "C://", title = "Save Backup as", filetypes = (("Text File (.txt)", "*.txt"), ("All Files", "*.*")))

    source_file = open("source.txt", "r")
    backup_file = open(backup_file,'w')
    backup_file.write(source_file.read())

    source_file.close()
    backup_file.close()



def about():
    top = Toplevel()
    info = Label(top, text="Name: Contact Book\nVersion: 1.0\nBuilt using: Python 3.9.x & Tkinter\nLicence: None")
    data = Label(top, text ="Contact me on email id: 5kchqvw6r@relay.firefox.com\nIf you're sending an attachment through given email id make sure the attachment size is less than 150KB.")
    info.grid(padx= 10, pady=10)
    data.grid(padx= 10, pady=10)
    

# Main Menu
info = Label(root, text= "Hey there\nI made this program to learn\ncore concepts of Tkinter\nI'm still beginner in designing,\nIf you have some great ideas contact me\non github or send me email,\nemail id provided in FAQs")

button_addContacts = Button(root, text = "Add new contact", width= 13, command = lambda:(add_contacts()))
button_view = Button(root, text = "View all contacts", width= 13, command = lambda:(viewAll()))
button_Backup = Button(root, text = "Create Backup", width= 13, command = lambda:(backup()))
button_faqs = Button(root, text = "About", width= 13, command = lambda:(about()))

info.grid(row= 0, column= 1, rowspan= 4, padx= 10)

button_addContacts.grid(row = 0 ,column = 0, padx= 10, pady=10)
button_view.grid(row = 1 ,column = 0,padx= 10, pady=10)
button_Backup.grid(row = 2 ,column = 0,padx= 10, pady=10)
button_faqs.grid(row = 3 ,column = 0,padx= 10, pady=10)


mainloop()