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
