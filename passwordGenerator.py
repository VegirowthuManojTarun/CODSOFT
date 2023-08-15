import random
import string
from tkinter import *
from tkinter import messagebox


def generate_random_password():
    global length_input, generated_password
    try:
        length = int(length_input.get())
        if length < 8:
            messagebox.showwarning('WARNING', "Password length should be at least 8")
        else:
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''
            for i in range(length):
                char = random.choice(characters)
                password += char
            generated_password.insert(END, password)
    except:
        messagebox.showwarning('WARNING', "!!Enter Valid Input!!")


def reset_password():
    global user_name, length_input, generated_password
    user_name.delete(0, END)
    length_input.delete(0, END)
    generated_password.delete(0, END)


def accept_the_value():
    global length_input, generated_password, user_name
    your_user_name = user_name.get()
    your_password = generated_password.get()
    if your_password and your_user_name:
        msg = 'Username:  ' + your_user_name + '\nPassword:  ' + your_password
        messagebox.showinfo(title='Your Details', message=msg)
    else:
        messagebox.showwarning('WARNING', "!!Please enter username and generate the password!")


def main():
    global length_input, generated_password, user_name

    root = Tk()
    root.geometry('800x250')
    root.minsize(800, 250)
    root.title("Random Password Generator")

    # info Section
    info_label1 = Label(root, text="NOTE:", font=("Helvetica", 20, 'bold'), fg='red', bg='Blue')
    info_label1.grid(row=0, column=1)

    info_label2 = Label(root, text="Fill all the details Correctly", font=("Helvetica", 20, 'bold'), bg='blue')
    info_label2.grid(row=0, column=2)

    # username section
    user_name_label = Label(root, text="User name:", font=("Helvetica", 17),)
    user_name_label.grid(row=1, column=2)

    user_name = Entry(root)
    user_name.grid(row=1, column=3, pady=10)

    # Password length section
    length_input_label = Label(root, text="Enter length of the password:", font=("Helvetica", 17),)
    length_input_label.grid(row=2, column=2)

    length_input = Entry(root)
    length_input.grid(row=2, column=3, pady=10)

    # generated password length section
    generated_password_label = Label(root, text="Generated Password:", font=("Helvetica", 17),)
    generated_password_label.grid(row=3, column=2, pady=10)

    generated_password = Entry(root)
    generated_password.grid(row=3, column=3)

    # buttons section
    generate_password_btn = Button(root, text="Generate", bg='green', font=("Helvetica", 15),
                                   borderwidth=2, border=3,
                                   command=generate_random_password)
    generate_password_btn.grid(row=4, column=1,padx=20)

    reset_btn = Button(root, text='Reset', bg='yellow', font=("Helvetica", 15),
                       borderwidth=2, border=3,
                       command=reset_password)
    reset_btn.grid(row=4, column=2)

    accept_btn = Button(root, text='Accept', bg='pink', font=("Helvetica", 15),
                        borderwidth=2, border=3,
                        command=accept_the_value)
    accept_btn.grid(row=4, column=3, padx=80)

    root.mainloop()


if __name__ == '__main__':
    main()
