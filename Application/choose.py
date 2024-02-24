import tkinter as tk
import subprocess

def login():
    print("login button clicked")
    root.destroy()
    subprocess.run(["python", "login.py"])

def signup():
    print("signup button clicked")
    root.destroy()
    subprocess.run(["python", "signup.py"])

root=tk.Tk()

root.title("Traffic Management Automation System")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

label=tk.Label(text="Traffic Management System",bg="blue",fg="white",height=4,width=screen_width)
label.config(font=("Sans-Serif",20))
label.pack()

btn=tk.Button(root,text="Login",command=login,width=50,height=3)
btn.pack(pady=50)

btn=tk.Button(root,text="Create New",command=signup,width=50,height=3)
btn.pack(pady=20)

root.mainloop()
