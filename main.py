from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for item in range(nr_letters)]
    password_symbols = [random.choice(symbols) for item in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for item in range(nr_numbers)]

    password_list = password_numbers + password_letters + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email":email,
            "password":password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message="Please don't leave any fields empty!")

    else:
        web_entry.delete(0, END)
        password_entry.delete(0, END)

        try:
            with open("data.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json","w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open("data.json","w") as file:
                json.dump(new_data, file, indent=4)

def find_password():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")

    else:
        input = web_entry.get()
        if input == "":
            messagebox.showinfo(title="Error", message="No Data File Found.")
        else:
            email = data[input]["email"]
            password = data[input]["password"]

            messagebox.showinfo(title="Data", message=f"{input} \nEmail: {email} \nPassword:{password}")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)

photo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=photo)
canvas.grid(column=1, row=0)

# Setting up labels

web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Setting up entries
web_entry = Entry(width=21)
web_entry.grid(column=1, row=1, columnspan=1)
web_entry.focus()

email_entry = Entry(width=36)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "dummy@email.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Setting up buttons
search_button = Button(text="Search", width=11, command=find_password)
search_button.grid(column=2, row=1)

generate_password = Button(text="Generate Password", width=11, command=gen_password)
generate_password.grid(column=2, row=3)

add = Button(text="Add", width=33, command=save_password)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()