import tkinter as tk
import pyrebase

def submit_action():
    email_val = email_entry.get()
    passwd_val = password_entry.get()

    print("inside Function")
    firebaseconfig = {
        "apiKey": "AIzaSyA_8MxSW42rjlkYTFqC0SBggRmbHWto0Lo",
        "authDomain": "traffic-memo-system.firebaseapp.com",
        "databaseURL": "https://traffic-memo-system-default-rtdb.asia-southeast1.firebasedatabase.app",
        "projectId": "traffic-memo-system",
        "storageBucket": "traffic-memo-system.appspot.com",
        "messagingSenderId": "924362054158",
        "appId": "1:924362054158:web:79ea6de2d743672581ba5f",
        "measurementId": "G-7NTYGR515N"
    }
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    road = db.child("road").get()
    data = road.val()
    for record_id, record_data in data.items():
        email_db = record_data.get('email', '')
        password_db = record_data.get('password', '')
        print(email_db, password_db)
        print(email_val, passwd_val)

        if email_db == email_val and password_db == passwd_val:
            print("Login Successful")
            root.destroy()
            break

root = tk.Tk()
root.title("Create New Road | Traffic Management Automation System")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

label = tk.Label(text="Login", bg="blue", fg="white", height=4, width=screen_width)
label.config(font=("Sans-Serif", 20))
label.pack()

label4 = tk.Label(text="Enter Email ID:", width=screen_width, height=2)
label4.config(font=("Sans-serif", 16))
label4.pack()

email_entry = tk.Entry()
email_entry.pack()

label5 = tk.Label(text="Enter Password:", width=screen_width, height=2)
label5.config(font=("Sans-serif", 16))
label5.pack()

password_entry = tk.Entry()
password_entry.pack()

submit_button = tk.Button(root, text="Submit", command=submit_action, width=50, height=2)
submit_button.pack(pady=55)

root.mainloop()
