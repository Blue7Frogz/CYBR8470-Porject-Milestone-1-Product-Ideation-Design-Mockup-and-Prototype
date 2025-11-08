# CYBR8470-Porject-Milestone-1-Product-Ideation-Design-Mockup-and-Prototype

# The executive summary
The UNO Activity Hub is a Django web application designed to centralize all campus events and activities at the University of Nebraska at Omaha (UNO). This includes sports games, academic lectures, student club meetings, and university wide announcements.

Currently, event information at UNO is scattered across different platforms (MavSYNC, Athletics, departmental pages, flyers, etc.). The UNO Activity Hub aims to unify this experience into a secure, interactive platform that students, faculty, and visitors can easily access via a web browser.

The application is built using Django for both the backend and frontend, leveraging Django’s built-in features for user authentication, database management, and URL routing. The platform uses a relational database (SQLite for development or PostgreSQL for production) to store events and user posts. Django’s templating system is used to render dynamic HTML pages, allowing rapid development, maintainable code, and integration of robust security features such as access control, HTTPS, and session management.


---

## Features

- User authentication (login/logout)
- Administrator account with full control over posts
- Users `user1` and `user2` can create posts
- All posts are visible to admin and users
- Simple and clean interface

---

## Getting Started

Follow these instructions to get the UNO Activity Hub running locally on your machine.

### Prerequisites

- **Python 3.11+** – [Download Python](https://www.python.org/downloads/)
- **pip** – Comes with Python
- **Virtualenv** (recommended)  
- Download Visual Studio Code - [Downlaod VSCode](https://code.visualstudio.com/download)
### Step1 1: Clone the Repository
- git clone <myrepo>
- cd uno_activity_hub
### Step 2: Create and activate a virtual environmnet
- python -m venv venv
- Windows CMD - .\venv\Scripts\activite
### Step 3: Install dependecies
- pip install -r requierments.txt
### Step 4: Apply database migrations
- python manage.py migrate
### Step 5: Create a superuser(admin)
- python manage.py createsuperuser
### Step 6: Run the development server
- python manage.py runserver (Open browser at http://127.0.0.1:8000)

# License
