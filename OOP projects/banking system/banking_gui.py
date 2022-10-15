from tkinter import *
import os
from PIL import ImageTk, Image

master = Tk()
master.title('Banking App')

def finish_reg():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    all_accounts = os.listdir()

    if name == '' or age == '' or gender == '' or password == '':
        notif.config(fg='red', text='All fields required')
        return

    if len(password) < 7:
        notif.config(fg='red', text='Password needs to bee at least 7 characters long')
        return
    print('password good')

    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg='red', text = "Account already exists")
            return
        else:
            new_file = open(name,'w')
            new_file.write(name+'\n')
            new_file.write(age+'\n')
            new_file.write(gender+'\n')
            new_file.write(password+'\n')
            new_file.close()
            notif.config(fg="green", text="Account has been created")





        
def register():
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif
    
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()
    
    register_screen = Toplevel(master)
    register_screen.title("Register")

    Label(register_screen, text="Please enter your details below to register.", font=('Poppins', 12)).grid(row=0, sticky=N, pady=10)
    Label(register_screen, text="Name", font=('Poppins', 12)).grid(row=1, sticky=W)
    Label(register_screen, text="Age", font=('Poppins', 12)).grid(row=2, sticky=W)
    Label(register_screen, text="Gender", font=('Poppins', 12)).grid(row=3, sticky=W)
    Label(register_screen, text="Password", font=('Poppins', 12)).grid(row=4, sticky=W)
    notif = Label(register_screen, font=('Poppins', 12))
    notif.grid(row=6, sticky=N, pady=10)

    Entry(register_screen, textvariable=temp_name).grid(row=1, column=0)
    Entry(register_screen, textvariable=temp_age).grid(row=2, column=0)
    Entry(register_screen, textvariable=temp_gender).grid(row=3, column=0)
    Entry(register_screen, textvariable=temp_password, show="*").grid(row=4, column=0)

    Button(register_screen, text="Register", command = finish_reg, font=("Poppins", 12)).grid(row=5, sticky=N, pady=10)
           
        
def login():
    print("This is s a login page")


img = Image.open('vault.png')
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)


Label(master, text = 'Custom banking Beta', font=('Poppins', 14)).grid(row=0,sticky=N,pady=10)
Label(master, text = 'the most secure banking app you have ever used', font=('Poppins', 12)).grid(row=1,sticky=N)
Label(master, image=img).grid(row=2,sticky=N,pady=15)


Button(master, text="Register", font=('Poppins', 12),width=20, command=register).grid(row=3,sticky=N)
Button(master, text="Login", font=('Poppins', 12),width=20, command=login).grid(row=4,sticky=N, pady=10) 

master.mainloop()
