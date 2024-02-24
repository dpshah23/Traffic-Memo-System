from django.shortcuts import render,redirect
import pyrebase
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from datetime import datetime
import random
import time
import string
from django.contrib import messages

# Create your views here.

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
auth=firebase.auth()
db=firebase.database()
def admin(request):
    if 'email' not in request.session:
        return redirect('')
    return render(request=request,template_name='admin.html')

def login(request): 
    global email1,password1
    if request.method=="POST":
        data=request.POST
        email1=data['email']
        password1=data['password']
        sendmail()

        
    return render(request,"login.html")
    
            

def sendmail():
        global otp,roadnm,email,password
        from_email = 'hackathon344+noreply@gmail.com'
        password = 'idiy xlrh vqzu omfd'
        subject="One Time Password For Admin "
        length=8
        alphanumeric_characters = string.ascii_letters + string.digits
        otp=''.join(random.choice(alphanumeric_characters) for _ in range(length))
        otp=otp.upper()
        print(otp)
        body=f"""

        <h1 style="text-align:center">One Time Password For Sign-in</h1>

        <p>Thank you for registering on our admin panel. To complete the registration process, please use the following One-Time Password (OTP)</p>

        <h2>Your OTP : {otp}</h2>

        <p>
        Please enter this OTP on the registration page to verify your identity and activate your account.

        If you did not initiate this registration, please ignore this message.

        </p>

        Thank you,
        <br>
        Government Of India.

        """
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = email1
        msg.attach(MIMEText(body, 'html'))


        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(from_email, password)
            server.sendmail(from_email, email1, msg.as_string())
            print("OTP Send Successfully")

        return redirect('/send_verification')

def verify(request):
     if request.method=="POST":
          data=request.POST
          otp_entered=data['otp']
          data=db.child('admin').get()
          data2=data.val()
          for key,data_items in data2.items():
               if data_items['email']==email:
                    name=data_items['name']
                    roadnm=data_items['roadnm']
                    role=data_items['role']

          issignin=auth.sign_in_with_email_and_password(email1,password1)


          if otp_entered==otp and issignin is not None:
               request.session['email']=email1
               request.session['roadnm']=roadnm
               request.session['name']=name
               request.session['role']=role
               print("Login Successful")
               

               messages.success(request,"Login Successfully")
               return render(request,"admin.html")

               

          else:
               messages.error(request,"Login Unsucessfully")
               return redirect('/')
               
     return render(request,"verify.html")
