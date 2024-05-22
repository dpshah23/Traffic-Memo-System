from datetime import datetime
import flask
from flask import Flask,render_template,redirect,request,jsonify
import pyrebase
from fpdf import FPDF
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from twilio.rest import Client
import pyshorteners



#  Add your firebase config
    
firebase=pyrebase.initialize_app(firebaseconfig)
storage=firebase.storage()
db=firebase.database()

app=Flask(__name__)

from_email = 'hackathon344@gmail.com'
password = 'idiy xlrh vqzu omfd'
subject="Memo Regarding Overspeeding Violation"
time1=datetime.now()
print(time1)

@app.route("/api",methods=["POST","GET"])
def api():
    account_sid = 'ACf4d75a2dc02ed30b1772e79351a9af1b'
    auth_token = 'f2b7c680d940eb45c5db569e0aad9577'
    client = Client(account_sid, auth_token)

    
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

    body=f"""

    <h1 style="text-align:center;">Government Of Gujarat</h1>

    <p>Dear {name},</p>

    <p>We hope this message finds you well. We regret to inform you that your vehicle with the number plate {plateno} was observed overspeeding on {time1}. This violation is a breach of traffic regulations and poses a risk to road safety.</p>

    <p>Memo Details:
        <ul>
            <li>Number Plate: {plateno}</li>
            <li>Date and Time: {time1}</li>
        </ul>
    </p>
    For your reference, we have generated a memo regarding this overspeeding incident. You can download the    memo using the link below:

    </p>

    <p><button style="border-radius:3px; background-color:#2383E2; padding:5px; width:250px; height:40px" align-item:center;>&nbsp;&nbsp;<a href="{attachment}" style="color:white;" target="_blank" rel="noopener noreferrer">Download Memo</a>&nbsp;&nbsp;</button></p>

    <p>Please take this matter seriously, and we urge you to adhere to speed limits for the safety of yourself and others on the road.</p>

    <p>If you have any concerns or would like to discuss this further, feel free to <a href="mailto:hackathon344@gmail.com">contact our traffic control department</a>.</p>

    <p>Thank you for your cooperation.</p>

    <p>Sincerely,<br>
    Government Of Gujarat<br>
    Traffic Control Department</p>



    """
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = email
    msg.attach(MIMEText(body, 'html'))


    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, email, msg.as_string())
        isdone=True
        print("Email Send Successfully with attachment")

    s = pyshorteners.Shortener()  
    short_url = s.tinyurl.short(attachment)
    message = client.messages.create(
    from_='+17248973287',
    body=f"""
        We hope this message finds you well. We regret to inform you that your vehicle with the number plate {plateno} was observed overspeeding on {time1}. This violation is a breach of traffic regulations and poses a risk to road safety.
       
        Number Plate : {plateno}
        Time : {time1}
      
        For your reference, we have generated a memo regarding this overspeeding incident. You can download the memo using the link below:
        Download Your Memo :- {short_url}
       
        Please take this matter seriously, and we urge you to adhere to speed limits for the safety of yourself and others on the road.

        If you have any concerns or would like to discuss this further, feel free to mail at {from_email}
      
        Thank you for your cooperation.

        Sincerely,
            Government Of Gujarat
            Traffic Control Department

        """,
        to='+916352972571'
        ) 

    issms=True



if __name__=="__main__":
    app.run(debug=True)
