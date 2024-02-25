## API Documentation

### Overview:
This API is designed to generate and send memos regarding overspeeding violations to vehicle owners. It integrates with various services such as Firebase for data storage, Twilio for SMS notifications, and Gmail for email notifications. The API receives vehicle details and violation information via HTTP requests and then generates and sends memos to the respective vehicle owners.

### Libraries Used:
- **Flask**: A micro web framework for building web applications in Python.
- **Pyrebase**: A Python wrapper for the Firebase platform, enabling interaction with Firebase services.
- **FPDF**: A Python library for creating PDF documents.
- **Random**: A Python library for generating random numbers.
- **Smtplib**: A Python library for sending email messages.
- **Email.mime**: Python modules for creating email messages with attachments.
- **Twilio**: A Python library for sending SMS messages.
- **Pyshorteners**: A Python library for shortening URLs.

### API Endpoints:
- **POST /api**:
  - **Description**: Receives vehicle details and violation information as parameters in the request.
  - **Parameters**:
    - `plateno`: Vehicle number plate.
    - `roadnm`: Road name where the violation occurred.
    - `datetime`: Date and time of the violation.
    - `imgurl`: URL of the image capturing the violation.
    - `speed`: Speed of the vehicle at the time of the violation.
  - **Functionality**:
    - Downloads the image capturing the violation from Firebase storage.
    - Generates a PDF memo containing details of the violation.
    - Sends an email notification with the PDF memo attached.
    - Sends an SMS notification with a short URL to download the memo.
  - **Returns**: None.

### Implementation Details:
1. **Firebase Integration**:
   ```python
   firebaseconfig = {...}  # Firebase configuration
   firebase = pyrebase.initialize_app(firebaseconfig)
   storage = firebase.storage()
   db = firebase.database()
   ```

2. **PDF Memo Generation**:
   ```python
   class PDF(FPDF):
       def header(self):
           ...
       def footer(self):
           ...
       def add_custom_table(self, numberplate, fine, url):
           ...
   ```

3. **Email Notification**:
   ```python
   body = """HTML email message"""
   msg = MIMEMultipart()
   msg['Subject'] = subject
   msg['From'] = from_email
   msg['To'] = email
   msg.attach(MIMEText(body, 'html'))
   ```

4. **SMS Notification**:
   ```python
   message = client.messages.create(
       from_='+17248973287',
       body="""SMS message""",
       to='+916352972571'
   )
   ```

5. **Randomization**:
   ```python
   no = random.randint(0, 10000)
   urlname = name + plateno + str(no)
   ```

### Explanation of Code:
- The `/api` endpoint receives vehicle details and violation information as parameters.
- It downloads the image capturing the violation from Firebase storage.
- A custom PDF memo is generated using FPDF, embedding the captured image.
- An HTML email message containing violation details is constructed and sent via Gmail SMTP server.
- An SMS notification is sent using Twilio, providing a short URL to download the memo.

### Running the API:
- The API can be run locally using the Flask development server with the command `python api.py`.
- It runs in debug mode to facilitate testing and debugging.

### Note:
- Ensure that the Firebase, Twilio, and Gmail configurations are correctly set up for the API to function properly.

# Traffic Management Automation System Documentation

## Overview:
The Traffic Management Automation System is a Python-based application designed to automate various tasks related to traffic management. It comprises modules for user authentication, road data management, and vehicle speed detection. This documentation provides an overview of each module, its implementation details, and usage instructions.

## Modules:

### 1. User Authentication:
- **Description:** This module facilitates user authentication, allowing users to log in or sign up to access system features.
- **Implementation:** Utilizes Tkinter for the graphical user interface (GUI) and Pyrebase for authentication with Firebase.
- **Function Calls:**
  - Firebase Authentication Functions from Pyrebase: Responsible for user login, registration, and token verification.
  - GUI Elements Management with Tkinter: Manages GUI elements such as labels, entry fields, and buttons to set up the login and signup screens.

### 2. Road Data Management:
- **Description:** Enables users to create and manage road data, including road names, speed limits, and distances between points.
- **Implementation:** Integrates with Firebase Realtime Database for data storage.
- **Function Calls:**
  - Firebase Database Functions from Pyrebase: Handles storing and retrieving road data from the Firebase Realtime Database.

### 3. Speed Detection Module:
- **Description:** Detects and monitors vehicle speeds using computer vision techniques.
- **Implementation:** Utilizes YOLO object detection, object tracking, and Optical Character Recognition (OCR) for number plate detection.
- **Function Calls:**
  - Object Tracking Functions from `tracker.py`: Used for updating object positions and IDs for vehicle tracking.
  - Number Plate Detection Functions from `numplatedetection.py`: Responsible for number plate detection using OCR.
  - YOLO Object Detection Functions from `ultralytics`: Enables object detection, including vehicles, within video frames.

## Installation:
1. Install Python and required dependencies: `opencv-python`, `pandas`, `numpy`, `ultralytics`, `easyocr`, `pyrebase`.
2. Place all files in the same directory.



   ```python
    pip install -r requirements.txt
   ```

## Usage:
- Run Python scripts:
  - For user authentication: `login.py` or `signup.py`.
  - For road data management: `signup.py`.
  - For speed detection: `speed.py`.

## Dependencies:
- **OpenCV:** Image processing and computer vision.
- **Pandas/Numpy:** Data manipulation and numerical computing.
- **Ultralytics:** YOLO object detection.
- **EasyOCR:** Optical Character Recognition.
- **Pyrebase:** Interaction with Firebase.

## Limitations:
- Accuracy of speed detection may vary based on environmental conditions.
- Limited error handling and validation.

## Future Enhancements:
- Implement advanced vehicle tracking algorithms.
- Enhance user interface and error handling.
- Add support for additional features like traffic pattern analysis.

This documentation provides an overview of the Traffic Management Automation System, including its modules, implementation details, usage instructions, dependencies, limitations, and future enhancement possibilities.