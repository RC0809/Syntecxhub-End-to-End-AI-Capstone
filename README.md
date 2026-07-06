# 🤖 AI Desktop Assistant with Face Authentication

A Python-based AI Desktop Assistant that authenticates users using facial recognition before granting access to a desktop assistant capable of executing various commands through a simple GUI.

---

## 📌 Project Overview

This project combines Computer Vision, GUI Development, and Desktop Automation to create a secure desktop assistant.

The application first verifies the user's identity using Face Recognition. Once authentication is successful, the assistant allows the user to execute various desktop and web commands through a clean graphical interface.

---

## ✨ Features

### 🔐 Face Authentication
- Face detection using OpenCV
- Face recognition using LBPH Face Recognizer
- 3-second continuous verification
- Authentication status display
- Embedded webcam inside GUI

### 💻 Desktop Assistant
- Open Google
- Open YouTube
- Google Search
- YouTube Search
- Open Gmail
- Open LinkedIn
- Open GitHub
- Open ChatGPT
- Open Calculator
- Open Notepad
- Open Paint
- Open Command Prompt
- Open Visual Studio Code
- Display Current Time
- Display Current Date
- Display Current Day
- Help Command
- Exit Assistant

### 🎨 GUI
- Built using CustomTkinter
- Live webcam feed
- Authentication progress bar
- Command input interface
- User-friendly status updates

---

## 🛠 Technologies Used

- Python 3.11
- OpenCV
- OpenCV-Contrib
- CustomTkinter
- Pillow
- NumPy
- Webbrowser
- OS
- Datetime

---

## 📂 Project Structure

```
AI-Desktop-Assistant/
│
├── trainer/
│   └── .gitkeep
│
├── screenshots/
│
├── FaceCapture.py
├── TrainModel.py
├── FaceAuthentication.py
├── commands.py
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Desktop-Assistant.git
```

Navigate to the project directory

```bash
cd AI-Desktop-Assistant
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙ Setup

Since the face model is user-specific, every user must generate their own training model.

### Step 1

Capture face images

```bash
python FaceCapture.py
```

### Step 2

Train the face recognition model

```bash
python TrainModel.py
```

This generates:

```
trainer/trainer.yml
```

### Step 3

Run the application

```bash
python main.py
```

---

## 📷 Screenshots

### Face Authentication

(Add authentication screenshot here)

---

### Assistant Interface

(Add assistant screenshot here)

---

### Command Execution

(Add command execution screenshot here)

---

## 💬 Example Commands

```
open google

open youtube

search machine learning

search youtube for python tutorial

open calculator

open notepad

open paint

open command prompt

open vs code

tell me the time

what is today's date

what day is today

help

exit
```

---

## 🔄 Application Workflow

```
Launch Application
        │
        ▼
Initialize Camera
        │
        ▼
Face Detection
        │
        ▼
Face Authentication
        │
        ▼
Authentication Successful
        │
        ▼
Launch Desktop Assistant
        │
        ▼
Accept User Commands
        │
        ▼
Execute Commands
```

---

## 🔮 Future Enhancements

The current version of the project focuses on secure face authentication and text-based command execution. In future releases, the following features are planned:

- 🎙️ Voice Command Recognition for hands-free interaction.
- 🔊 Text-to-Speech responses for a more interactive assistant.
- 👥 Multi-user Face Authentication with individual user profiles.
- 🌦️ Weather updates and news integration.
- 📁 File and folder management through natural language commands.
- 🤖 Integration with AI models (e.g., OpenAI/Gemini) for intelligent conversations.
- 📧 Email and calendar management.
- 💻 System monitoring (CPU, RAM, Battery, Network).
- 🌐 Smart web automation and productivity commands.
- 🎵 Media playback and system volume controls. Word

---

## 👨‍💻 Author

**Rakshit Chugh**

GitHub: https://github.com/RC0809

---

## 📄 License

This project is developed for educational and learning purposes.
