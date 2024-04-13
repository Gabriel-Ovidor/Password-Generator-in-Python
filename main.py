import random
import string as st
import tkinter as tk
from tkinter import ttk
from tkinter import *
from ttkthemes import ThemedTk

def password_generator():

    characters = st.ascii_letters + st.digits + st.punctuation
    user = int(user_entry.get())
    password  = "".join(random.choice(characters) for _ in range(user)) 
    output.config(text=password)
    output.config(text=password, font=('Montserrat classic', 10), justify='center')

def copy_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output['text'])
    
root = ThemedTk(theme='equilux')
root.title('Password Generator')
root.geometry('300x200')

user_entry = Entry(root)
user_entry.pack(pady=10)

generate_button = ttk.Button(root, text='Generate Password', command=password_generator)
generate_button.pack(pady=5)

copy = ttk.Button(root, text='Copy', command=copy_clipboard)
copy.pack(pady=5)

output = ttk.Label(root)
output.pack(pady=20)

root.mainloop()
