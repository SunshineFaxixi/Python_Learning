from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    passwd_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = user_info_entry.get()
    passwd = passwd_entry.get()
    # record = f"{website} | {email} | {passwd}\n"

    new_data = {
        website:{
            "email": email,
            "passwd": passwd,
        }
    }
    if len(website) == 0 or len(passwd) == 0:
        messagebox.showinfo(title="error", message="There is field left empty.")
    else:
        # # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \n"
        #                                                       f"Password: {passwd}\n Is it ok to save?")
        # if is_ok:
        #     with open("data.txt", "a") as data:
        #         data.write(record)
        #     website_entry.delete(0, END)
        #     passwd_entry.delete(0, END)

        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            passwd_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
            if website in data:
                email = data[website]["email"]
                passwd = data[website]["passwd"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {passwd}\n")
            else:
                messagebox.showinfo(title="error", message=f"No details for {website}")
    except:
        messagebox.showinfo(title="error", message="No file found.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
user_info_label = Label(text="Email/Username:")
user_info_label.grid(row=2, column=0)
passwd_label = Label(text="Password:")
passwd_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=26)
website_entry.focus()
website_entry.grid(row=1, column=1)
user_info_entry = Entry(width=43)
user_info_entry.insert(END, "xiaoxiao@gmail.com")
user_info_entry.grid(row=2, column=1, columnspan=2)
passwd_entry = Entry(width=26)
passwd_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=12, command=find_password)
search_button.grid(row=1, column=2)
generate_passwd_button = Button(text="Generate Password", width=16, command=generate_password)
generate_passwd_button.grid(row=3, column=2)
add_button = Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()