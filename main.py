from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import pyperclip as pyperclip


def randomPass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)

    if e3.get() == "":
        e3.insert(0, password)
    else:
        e3.delete(0, END)
        e3.insert(0, password)

    pyperclip.copy(password)
    messagebox.showinfo(title="Password", message="Generated Password Copied To Clipboard")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def search():
    try:
        f1 = open("password.json", "r")
        dict = json.load(f1)
        messagebox.showinfo(title=e1.get(),
                            message=f"Email : {dict[e1.get()]['email']}\nPassword : {dict[e1.get()]['password']}")
    except KeyError:
        messagebox.showerror(title="Error", message=f"{e1.get()} Website Not Found In Database")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def addData():
    website = e1.get()
    email = e2.get()
    password = e3.get()
    newDict = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Empty Fields", message="Hey You Left Some Fields Empty!!")
    else:
        try:
            f1 = open("password.json", "r")
        except FileNotFoundError:
            f1 = open("password.json", "w")
            json.dump(newDict, f1, indent=4)
            f1.close()
        else:
            data = json.load(f1)
            data.update(newDict)
            f1 = open("password.json", "w")
            json.dump(data, f1, indent=4)
            f1.close()
        finally:
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(400, 400)
window.config(padx=30, pady=30)
canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)
l1 = Label(text="Website:")
l1.grid(row=1, column=0)
e1 = Entry(width=36)
e1.grid(row=1, column=1, )
e1.focus()
l1 = Label(text="Email/Username:")
l1.grid(row=2, column=0)
e2 = Entry(width=55)
e2.grid(row=2, column=1, columnspan=2)
l1 = Label(text="Password:")
l1.grid(row=3, column=0)
e3 = Entry(width=36)
e3.grid(row=3, column=1)
b1 = Button(text="Generate Password", command=randomPass)
b1.grid(row=3, column=2)
b2 = Button(text="Add", width=47, command=addData)
b2.grid(row=4, column=1, columnspan=2)
b3 = Button(text="Search", width=15, command=search)
b3.grid(row=1, column=2)
window.mainloop()
