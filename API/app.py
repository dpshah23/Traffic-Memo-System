from datetime import datetime
import flask
from flask import Flask,render_template,redirect,request,jsonify
import pyrebase
from fpdf import FPDF
import random
firebaseconfig={
    "apiKey": "AIzaSyA_8MxSW42rjlkYTFqC0SBggRmbHWto0Lo",
    "authDomain": "traffic-memo-system.firebaseapp.com",
    "databaseURL": "https://traffic-memo-system-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "traffic-memo-system",
    "storageBucket": "traffic-memo-system.appspot.com",
    "messagingSenderId": "924362054158",
    "appId": "1:924362054158:web:79ea6de2d743672581ba5f",
    "measurementId": "G-7NTYGR515N"

}
    
firebase=pyrebase.initialize_app(firebaseconfig)
storage=firebase.storage()
db=firebase.database()

app=Flask(__name__)

@app.route("/api",methods=["POST","GET"])
def api():
    plateno=request.args.get("plateno")
    roadnm=request.args.get("roadnm")
    datetime1=request.args.get("datetime")
    imgurl=request.args.get("imgurl")
    speed=request.args.get('speed')
    storage.child(imgurl).download("downloaded.jpg")
    url="downloaded.jpg"
    time1=datetime.now()
    class PDF(FPDF):
        def header(self):
            self.image('logo.png', 10, 8, 25)
            self.set_font("helvetica", 'B', 18)
            self.cell(0, 10, "Government Of Gujarat", ln=1, align='C')
            self.ln(20)
            self.image(url, x=40, y=(self.get_y()-5), w=50)
            self.ln(40)

        def footer(self):
            self.set_font("helvetica", "B", 14)
            self.set_y(-25)
            self.cell(0,10,f"This reciept genrated at {time1} at {roadnm}... Speed is {speed}",align='C')
            self.ln()
            self.cell(0, 10, "This Is Computer Generated Memo. No Need For Any Verification...", align='C')

        def add_custom_table(self, numberplate, fine,url):

            self.add_page()
            self.set_font("helvetica", '', 16)
            self.cell(40, 10, "       ")
        
             # Table Header
            self.cell(60, 10, "Challan No", 1,align="C")
            self.cell(60, 10, "Amount", 1,align="C")
            self.ln()

       

            #    Table Data
            self.cell(40, 10, "       ")
            self.cell(60, 10, numberplate, 1,align="R")
            self.cell(60, 10, f"INR {fine}", 1,align="C")  # Using "INR" as a prefix for Rupee
            self.ln()

            # Total Row
            self.cell(40, 10, "       ")
            self.cell(60, 10, "Total", 1, 0,align="R")
        
            self.cell(60, 10, f"INR {fine}", 1,align="C")

    
    jsond = db.child('users').get()
    data=jsond.val()
    if jsond:
        for record_id,record_data in data.items():
            noplatedb=record_data.get("plateno")
            if noplatedb==plateno:
                name=record_data.get("name")
                email=record_data.get("email")
                mobile=record_data.get("mobile")
                print(name)

                break
            else:
                continue

    else:
    
        print("No user found with the given plate number.")
    pdf = PDF('P', 'mm', 'A4')
    fine=500
    pdf.add_custom_table(plateno, fine,url)
    no=random.randint(0,10000)
    no=str(no)
    urlname=name+plateno+no
    pdf.output("challan.pdf")
    storage.child(name+plateno+no).put("challan.pdf")

    attachment=f"https://firebasestorage.googleapis.com/v0/b/traffic-memo-system.appspot.com/o/{urlname}?alt=media"
    print(attachment)


if __name__=="__main__":
    app.run(debug=True)