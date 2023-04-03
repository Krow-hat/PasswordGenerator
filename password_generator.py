from tkinter import *
import string
import random
import pyperclip


def generator():
    lower_alphabets=string.ascii_lowercase
    upper_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_character=string.punctuation

    all=lower_alphabets+upper_alphabets+numbers+special_character
    password_length=int(length_box.get())
    password=passlength=random.sample(all,password_length)
    passwordField.insert(0,password)

    if choice.get()==1:
        passwordField.insert(0,random.sample(lower_alphabets,password_length))

    if choice.get() ==2:
        passwordField.insert(0, random.sample(lower_alphabets+upper_alphabets, password_length))

        if choice.get()==3:
            passwordField.insert(0, random.sample(lower_alphabets+upper_alphabets+numbers+special_character,password_length))

def copy():
    random_password=passwordField.get()
    pyperclip.copy(random_password)

root=Tk()
root.config(bg='black')
choice=IntVar()
Font=('Bookman old style',12)
passwordLabel=Label(root,text="Password Generator", font=('Bookman old style',20,'italic'),bg='black',fg='chartreuse1')
passwordLabel.grid(pady=10)
weakradioButton=Radiobutton(root,text='Weak',value=1,variable=choice,font=Font,bg="black",fg='chartreuse1')
weakradioButton.grid(pady=5)

mediumradioButton=Radiobutton(root,text='Medium',value=2,variable=choice,font=Font,bg="black",fg='chartreuse1')
mediumradioButton.grid(pady=5)

StrongradioButton=Radiobutton(root,text='Strong',value=3,variable=choice,font=Font,bg="black",fg='chartreuse1')
StrongradioButton.grid(pady=5)

lengthLabel=Label(root,text="Password Length", font=('Bookman old style',20,'italic'),bg='black',fg='chartreuse1')
lengthLabel.grid()

length_box=Spinbox(root,from_=5,to_=20,width=5,font=Font,bg="black",fg='chartreuse1')
length_box.grid()

generateButton=Button(root,text='Generate',font=Font,bg='black',fg='chartreuse1',command=generator)
generateButton.grid(pady=20)

passwordField=Entry(root,width=25,bd=2,font=Font,bg='black',fg='chartreuse1')
passwordField.grid()

copyButton=Button(root,text='Copy',font=Font,bg='black',fg='chartreuse1',command=copy)
copyButton.grid(pady=20)

root.mainloop()