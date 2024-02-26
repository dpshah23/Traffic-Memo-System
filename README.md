# Important Note
<h4>This Site is hosted on free server so it may take a while to load so please be patient . Thank you</h4>

Link Of Admin Panel :- https://admin-panel-traffic-management-system.onrender.com


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
- **Random:** Python library for generating random numbers, useful for tasks like OTP generation.
- **Yolov8:** Object detection algorithm for real-time detection in images and videos.
- **OpenCV:** Open-source computer vision library providing functions for image and video processing.
- **Russian Cascade:** Haar Cascade classifier trained for detecting Russian license plate numbers.
- **EasyOCR:** Python package for optical character recognition, simplifying text extraction from images.

### Additional Technologies

- Computer Vision Convolutional Neural Network (CNN): Utilized within the Yolov8 algorithm for object detection tasks, CNNs are deep learning models designed to 
  automatically and adaptively learn spatial hierarchies of features directly from image data. They are commonly employed in computer vision tasks for their 
  ability to extract intricate patterns and features from images.

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

### Model Explanation

The Traffic Management Automation System is built upon a modular architecture, comprising distinct components for user authentication, road data management, and vehicle speed detection.

## User Authentication Module:

- Responsible for managing user access to the system. Users can log in or sign up to utilize the system's functionalities securely. This module employs Tkinter 
  for the graphical user interface and Pyrebase for authentication with Firebase.

## Road Data Management Module: 

- Enables users to create, update, and retrieve road-related data such as road names, speed limits, and distances between points. This module integrates with the 
  Firebase Realtime Database for seamless data storage and retrieval.

## Vehicle Speed Detection Module: 

- Utilizes computer vision techniques for real-time detection and monitoring of vehicle speeds. The core of this module lies in the Yolov8 object detection 
  algorithm, which identifies vehicles within video frames. Object tracking techniques are then applied to track vehicle movements over consecutive frames. 
  Furthermore, the module employs a Russian Cascade classifier for detecting Russian license plate numbers, and EasyOCR for extracting text from the detected 
  number plates. This comprehensive approach allows the system to accurately monitor and record vehicle speeds, ensuring adherence to traffic regulations.

By leveraging these interconnected modules, the Traffic Management Automation System streamlines traffic management tasks, enhances road safety, and facilitates efficient monitoring of vehicular activities.



#  Web Application Documentation

## Introduction:
The web application component of the Automatic Memo System for Overspeeding provides a user-friendly interface for staff and admin functionalities. This documentation outlines the key features, modules, and functionalities of the web application.

## 1. Main Admin HTML:
The main admin HTML serves as the entry point for the web application. Upon accessing the main admin page, users are prompted to enter their email and password for authentication. Additionally, a two-factor authentication (2FA) mechanism is implemented using OTP (One-Time Password) sent to the user's email address. This ensures an added layer of security for user authentication.

## 2. Login Module:
Once authenticated, users are directed to their respective interfaces based on their roles (staff or admin). The login module verifies user credentials and OTP authentication before granting access to the application.

## 3. Staff Interface:
Staff members have access to specific functionalities:
- Viewing specific memos: Staff can view memos related to overspeeding violations. Memos are displayed in a tabular format, showing relevant details such as vehicle number plate, speed, timestamp, and road name.
- Sorting memos: Staff can sort memos based on different parameters such as date, vehicle number plate, or speed.

## 4. Admin Interface:
Admins have access to advanced functionalities for managing the system:
- Viewing all memos: Admins can view all memos generated by the system, including those generated by staff members. Memos are displayed in a comprehensive table format with filtering and sorting options.
- Managing user and vehicle details: Admins can view and manage user accounts and vehicle details registered in the system. This includes adding new users, updating user information, and removing users if necessary.
- Applying filters: Admins have access to various filters to narrow down the data displayed on the interface. Filters include date range, road name, speed range, and more.

## 5. Technology Stack:
The web application is developed using a combination of frontend and backend technologies:

- Frontend: HTML, CSS, jQuery for user interface design and interactivity.
- Backend: Python with Flask and Django frameworks for server-side logic, API integration, and routing.
- Database: Firebase for real-time database management, storage, and retrieval of user, vehicle, and memo data.

## 6. Security: 
- To ensure data security and user privacy, the web application implements secure authentication mechanisms, such as password hashing, HTTPS encryption, and OTP-based 2FA. Access control is enforced to restrict 
  unauthorized access to sensitive functionalities and data.

## Conclusion:
The web application component of the Automatic Memo System for Overspeeding enhances user experience and system manageability by providing intuitive interfaces for staff and admin operations. It plays a crucial role in streamlining the process of managing overspeeding violations and promoting road safety and compliance.
