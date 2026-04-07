# Event-registration
Event Registration System (Cloud-Based College Project)
A serverless-inspired web application for seamless student event registrations.
Built using Flask (Python), HTML/CSS, and MySQL, this project demonstrates full-stack development along with cloud deployment concepts.

Objectives
Develop a web-based event registration system
Store and manage student data using a database
Provide a clean and user-friendly interface
Design a cloud-ready and scalable architecture

# System Architecture
Flow:
User → Frontend (HTML/CSS Form) → Flask Backend → MySQL Database → Data Display

# ☁️ Cloud Integration (Google Cloud Ready)
This project is designed to be easily migrated to cloud platforms.
🔹 Google Cloud Services
Cloud Run
Deploy Flask app as a container
Automatic scaling
Serverless execution

Cloud SQL
Managed MySQL database
Secure and scalable storage

✅ Benefits
High scalability
Remote accessibility
Reduced infrastructure management
Pay-as-you-use pricing

# Installation & Setup
git clone https://github.com/tanishkaprabhu7/event-registration-system.git
cd event-registration-system
# 2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate       

# 2️⃣ Install Dependencies
pip install flask flask_sqlalchemy pymysql

# 3️⃣ Configure Database
Update your MySQL credentials in app.py:
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/eventdb'
Then create database:
CREATE DATABASE eventdb;

# 4️⃣ Run Application
python app.py
Visit:
👉 http://127.0.0.1:5000/

# 📂 Project Structure
├── app.py
├── templates/
│   ├── index.html
│   ├── success.html
│   └── view.html
├── static
└── README.md

# ✨ Features
📋 Event registration form
💾 MySQL database storage
📊 View all registrations
🎨 Animated UI with CSS
🌐 Deployed web app (Render)
☁️ Cloud-ready architecture

# ⚠️ Challenges Faced
MySQL connection and authentication issues
Debugging backend form handling
Fixing template rendering bugs

# 📚 Key Learnings
Full-stack development with Flask
Database integration using SQLAlchemy
Understanding cloud architecture 

#  Future Improvements
Full migration to Google Cloud

# Google Cloud Integration
1️⃣ Google Cloud Run (Backend Deployment)
A serverless platform to deploy containerized Flask applications.
It automatically scales based on incoming traffic and removes the need for manual server management.

2️⃣ Google Cloud SQL (Database Service)
A fully managed MySQL database service that provides secure, reliable, and scalable data storage.
It can replace the local MySQL database used in this project.

3️⃣ Cloud-Based Architecture Benefits
High scalability and availability
Remote access from anywhere
Reduced infrastructure management
Pay-as-you-use cost model

