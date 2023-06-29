from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
 
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_symbols + password_letters + password_numbers

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)

    entry_pw.insert(0, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    line = f'{entry_website.get()} | {entry_email.get()} | {entry_pw.get()}\n'
    new_data = {entry_website.get(): {
        "email": entry_email.get(),
        "password": entry_pw.get()
    }}

    if len(entry_website.get()) > 0 and len(entry_email.get()) > 0 and len(entry_pw.get()) > 0:
        is_ok = messagebox.askokcancel(title=entry_website.get(), message=f"These are the details of your new password:\nEmail: {entry_email.get()}\nPassword: {entry_pw.get()}\nIs it OK to save?")

        if is_ok:
            try:
                with open('data.json', mode='r') as data_file:
                    # Reading old data:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open('data.json', mode='w') as data_file:
                    # Create and write on the file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data:
                data.update(new_data)
                with open('data.json', 'w') as data_file:
                    # Saving updated data:
                    json.dump(data, data_file, indent=4)
            finally:
                entry_website.delete(0, END)
                entry_pw.delete(0, END)

    else:
        messagebox.showerror(title='Oops!', message="Please don't leave any fields empty!")

# ---------------------------- SEARCH ------------------------------- #

def find_password():
    search_term = entry_website.get()

    try:
        with open('data.json', mode='r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Oops!', message='You still have no information stored.')
    else:
        try:
            result = data[search_term]
        except KeyError:
            messagebox.showinfo(title='Oops!', message='Website not found.')
        else:
            messagebox.showinfo(title=search_term, message=f"E-mail/Username: {result['email']}\nPassword: {result['password']}")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
# window.minsize(width=500, height=500)
window.config(padx=50, pady=50, bg='#f1f1f1')

canvas = Canvas(width=200, height=200, bg='#f1f1f1', highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1, row=0)

label_website = Label(text='Website:', bg='#f1f1f1', highlightthickness=0, fg='#111111', pady=10)
label_website.grid(column=0, row=1)

entry_website = Entry(width=21, bg='#f1f1f1', highlightthickness=0, fg='#111111')
entry_website.grid(column=1, row=1)
entry_website.focus()

button_search = Button(text='Search', bg='#f1f1f1', highlightthickness=0, fg='#111111', highlightbackground='#f1f1f1', pady=2, command=find_password, width=13)
button_search.grid(column=2, row=1)

label_email = Label(text='Email/Username:', bg='#f1f1f1', fg='#111111', pady=10)
label_email.grid(column=0, row=2)

entry_email = Entry(width=38, bg='#f1f1f1', highlightthickness=0, fg='#111111')
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(0, 'jaguattt@gmail.com')

label_pw = Label(text='Password:', bg='#f1f1f1', highlightthickness=0, fg='#111111', pady=10)
label_pw.grid(column=0, row=3)

entry_pw = Entry(width=21, bg='#f1f1f1', highlightthickness=0, fg='#111111')
entry_pw.grid(column=1, row=3)

button_generate = Button(text='Generate Password', bg='#f1f1f1', highlightthickness=0, fg='#111111', highlightbackground='#f1f1f1', pady=2, command=generate_password)
button_generate.grid(column=2, row=3)

button_add = Button(text='Add', width=36, bg='#f1f1f1', highlightthickness=0, fg='#111111', highlightbackground='#f1f1f1', pady=5, command=save)
button_add.grid(column=1, row=4, columnspan=2)





window.mainloop()