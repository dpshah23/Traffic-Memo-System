import tkinter as tk
import pyrebase
import subprocess

def submit_action():
    pass

root=tk.Tk()
root.title("Create New Road | Traffic Management Automation System")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

label=tk.Label(text="Create New Road",bg="blue",fg="white",height=4,width=screen_width)
label.config(font=("Sans-Serif",20))
label.pack()


label3=tk.Label(text="Enter Road Name",width=screen_width,height=2)
label3.config(font=("Sans-serif",16))
label3.pack()
roadnm=tk.Entry()
roadnm.pack()
roadname=roadnm.get()

label4=tk.Label(text="Enter Email ID:",width=screen_width,height=2)
label4.config(font=("Sans-serif",16))
label4.pack()
email=tk.Entry()
email.pack()
emailid=email.get()


label5=tk.Label(text="Enter Password:",width=screen_width,height=2)
label5.config(font=("Sans-serif",16))
label5.pack()
password=tk.Entry()
password.pack()
passwd=password.get()


label6=tk.Label(text="Enter Speed Limit (CAR):",width=screen_width,height=2)
label6.config(font=("Sans-serif",16))
label6.pack()
speed=tk.Entry()
speed.pack()
speedl=speed.get()

label7=tk.Label(text="Enter Approx Distance Between Two Points:",width=screen_width,height=2)
label7.config(font=("Sans-serif",16))
label7.pack()
dist=tk.Entry()
dist.pack()
distance=dist.get()



submit_button = tk.Button(root, text="Submit", command=submit_action,width=50,height=2)
submit_button.pack(pady=55)

root.mainloop()
