from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from pyperclip import copy
import json

# search info
def find_password():
    website = website_input.get()
    
    try:
        with open("data.json", mode="r") as output:
            data = json.load(output)
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="No Data File Found")
    else:
        if website in data:
            # store the key's in the website searched into a list. info[0] is email, info[1] is password
            info = [web for web in data[website].values()]
            messagebox.showinfo(title=website, message=f"Email: {info[0]} \nPassword: {info[1]}")
        else:
            messagebox.showerror(title="Oops", message=f"No details for {website} exists")
# password generator
def generate_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = []

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    
    # password is automatically in user's clipboard once password is generated
    copy(password)
# save password to json file
def save():
    website = website_input.get()
    user_info = user_input.get()
    password = password_input.get()
    
    new_data = {
            website: {
                "email": user_info,
                "password": password
            }
        }
    if len(website) == 0 or len(user_info) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        confirm = messagebox.askokcancel(title=website, 
                            message=f"These are the details entered: \nEmail: {user_info} \nPassword: {password} \nIs it okay to save?")
        if confirm:
            try:
                # try open and read file
                with open("data.json", mode="r") as output:
                    data = json.load(output)
            except FileNotFoundError:
                # create and add new data into file if file doesn't exist
                with open("data.json", mode="w") as output:
                    json.dump(new_data, output, indent=4)
            else:                    
                # if file exists, update data with new data
                data.update(new_data)
                with open("data.json", mode="w") as output:
                    json.dump(data, output, indent=4)
            finally:
                # remove all the fields info regardless
                website_input.delete(0, END)
                user_input.delete(0, END)
                password_input.delete(0, END)
# UI setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(135, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Inputs
website_input = Entry(width=21)
website_input.grid(column=1, row=1)
user_input = Entry(width=38)
user_input.grid(column=1, row=2, columnspan=2)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# Buttons
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)
generate_password = Button(text="Generate Password", command=generate_pw)
generate_password.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
