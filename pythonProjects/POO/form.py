import tkinter
from tkinter import *

window = Tk()
window.geometry("650x550")
window.title("Registration Form")
window.resizable(False, False)
window.config(background="light grey")
main_title = Label(text="Python Form | TRUZZ BLOGG", font=("Cambria", 14), bg="royalblue3", fg="black", width="500",
                   height="2")
main_title.pack()

username_label = Label(text="Username", bg="light grey", font=("Open Sans", 12))
username_label.place(x=22, y=70)
password_label = Label(text="Password", bg="light grey", font=("Open Sans", 12))
password_label.place(x=22, y=130)
fullname_label = Label(text="Full name", bg="light grey", font=("Open Sans", 12))
fullname_label.place(x=22, y=190)
age_label = Label(text="Age", bg="light grey", font=("Open Sans", 12))
age_label.place(x=22, y=250)
genre_label = Label(text="Genre", bg="light grey", font=("Open Sans", 12))
genre_label.place(x=22, y=310)

username = StringVar()
password = StringVar()
fullname = StringVar()
age = StringVar()
genre = StringVar()

username_entry = Entry(textvariable=username, width="40")
username_entry.place(x=22, y=100)
password_entry = Entry(textvariable=password, width="40", show="*")
password_entry.place(x=22, y=160)
fullname_entry = Entry(textvariable=fullname, width="40")
fullname_entry.place(x=22, y=220)
age_entry = Entry(textvariable=age, width="40")
age_entry.place(x=22, y=280)
genre_entry = Entry(textvariable=genre, width="40")
genre_entry.place(x=22, y=340)


def exit():
    window.destroy()


def sumbit():
    userdate = username.get()
    passdate = password.get()
    namedate = fullname.get()
    agedate = age.get()
    genredate = genre.get()

    print(f"Username: {userdate}\nPassword: {passdate}\nFull name: {namedate}\nAge: {agedate}\nGenre: {genredate}")

    newfile = open("Registration", "a")
    newfile.write(userdate)
    newfile.write("\n")
    newfile.write(passdate)
    newfile.write("\n")
    newfile.write(namedate)
    newfile.write("\n")
    newfile.write(agedate)
    newfile.write("\n")
    newfile.write(genredate)
    newfile.write("\n")
    newfile.write("\n")
    newfile.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    fullname_entry.delete(0, END)
    age_entry.delete(0, END)
    genre_entry.delete(0, END)


submit_button = Button(window, text="Submit", width="30", height="2", bg="blue", fg="white", command=sumbit)
submit_button.place(x=22, y=380)

exitButton = tkinter.Button(window, text="Exit", height=1, width=4, command=exit, borderwidth=5)
exitButton.config(bg="red", fg="white", font=("Arial", 12))
exitButton.place(x=570, y=500)

window.mainloop()
