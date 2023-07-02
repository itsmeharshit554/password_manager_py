import tkinter
from tkinter import messagebox
import random
import pyperclip
import json
messagebox.showinfo(title="Locked & Loaded",message="Welcome to Locked & Loaded\n A Password Manager To Store Your passwords and create new ones to keep your account safe\n It is like a wallet for your passwords\n\n I hope you like it :)\nRegards\nHarshit ")
def gen_pass():
    input_pass.delete(0,"end")
    character=[]
    for x in range(33,123):
        x=chr(x)
        character.append(x)

    pass_gen=[]
    y=0
    while y<=11:
        pos=random.randint(0,(len(character)-1))
        ch=character[pos]
        pass_gen.append(ch)
        y+=1
    pass_final=""
    for cha in pass_gen:
        pass_final+=cha
    
    
    print(character)
    print(pass_gen)
    print(f"The random password gen: {pass_final}")
    input_pass.insert(0,string=pass_gen)

def save():
    web=input_web.get()
    mail=input_email.get()
    pass_word=input_pass.get()
    pass_word=pass_word.replace(" ","")
    new_data={
        web:{
        "email":mail,
        "password":pass_word,
        }
    }

    ans=messagebox.askokcancel(title="Locked & Loaded",message=f"Do You want to continue\n\n    Website Entered: {web}\n    Email Entered: {mail}\n    Password Entered: {pass_word}")
    if web=="" or mail=="" or pass_word=="":
        messagebox.showwarning(title="Lock & Loaded",message="Fill all the details!")
    
    if ans==False:
        input_web.delete("0","end")
        input_pass.delete("0","end")
        input_web.focus()     

    else:
        try:
            if ans!=True:
                messagebox.showerror("Lock & Loaded","Never gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you")
            with open("Tkinter\Password_Manager\data_ll.json","r") as data_file:
                data=json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("Tkinter\Password_Manager\data_ll.json","w") as data_file:
                json.dump(new_data,data_file)
                data.update(new_data)
        #     print(data)
        
        with open("Tkinter\Password_Manager\data_ll.json","w") as data_file:
            json.dump(data,data_file,indent=4)
        
        pyperclip.copy(pass_word)
        input_web.delete("0","end")
        # input_email.after(1000,input_email.destroy())
        input_pass.delete("0","end")
        input_web.focus()     
def search():
    web=input_web.get()
    with open("Tkinter\Password_Manager\data_ll.json") as data_file:
        data=json.load(data_file)
        
        if web in data:
            hold_mail=data[web]["email"]
            hold_pass=data[web]["password"]
            pyperclip.copy(hold_pass)
            messagebox.showinfo(f"{web}",f"Email: {hold_mail}\nPassword: {hold_pass}\n\nPassword has been copied to clipboard")
        else:
            messagebox.showerror("Locked & Loaded","No Data Found")



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
screen=tkinter.Tk()
screen.minsize(300,300)
screen.title("Lock & Loaded")
screen.config(padx=20,pady=20)
# screen.configure(bg="white")

# canvas=tkinter.Canvas(width=200,height=200)
# # pic=tkinter.PhotoImage(file=r"Tkinter\\Password_Manager\\lock2.png")
# canvas.create_image(100,100,image=pic)
# canvas.grid(row=0,column=1)

website_lab=tkinter.Label(text="Website:",font=(2))
website_lab.grid(row=1,column=0)
# website_lab.configure(bg="white")

email=tkinter.Label(text="Email/Username:",font=(2))
email.grid(row=2,column=0)
# email.configure(bg="white")

password=tkinter.Label(text="Password:",font=(2))
password.grid(row=3,column=0)
# password.configure(bg="white")


input_web=tkinter.Entry(width=35)
input_web.grid(row=1,column=1,columnspan=2)
input_web.focus()
# input_web.configure(bg="white")

input_email=tkinter.Entry(width=54)
input_email.grid(row=2,column=1,columnspan=3)
input_email.insert(0,"sainiharshit@gmail.com")

input_pass=tkinter.Entry(width=34)
input_pass.grid(row=3,column=1)

generate_pass=tkinter.Button(text="Generate Password",command=gen_pass)
generate_pass.config(padx=0)
generate_pass.grid(row=3,column=2,columnspan=2)


add=tkinter.Button(text="Add",width=45,command=save)
add.grid(row=4,column=1,columnspan=3)

search=tkinter.Button(text="Search",width=15,command=search)
search.grid(row=1,column=3)

screen.mainloop()
