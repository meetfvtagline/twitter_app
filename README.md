🐦 Flask Twitter-Like Microblogging App

A Twitter-inspired microblogging application built using Flask and PostgreSQL.
This project focuses on core backend functionality rather than UI design.

✨ Overview

This application allows users to create short microblogs, upload images, like posts, and manage profiles with secure authentication and email-based password recovery.

🎯 Goal: Demonstrate Flask fundamentals, authentication, database design, and clean project structure.

🔥 Key Features
🔐 Authentication

User Registration

Login & Logout

Forgot Password

Reset Password via Email (Token-based)

✍️ Microblogging

Create blogs with maximum 15 words

Upload images with posts

Blogs displayed in LIFO order (latest first)

❤️ Likes

Like posts from other users

Like counter updates on page refresh

👤 User Profiles

Profile creation

Edit profile (logged-in users only)

🛡️ Security & Validation

Password hashing

CSRF protection

Secure email tokens

Proper validation & error messages

🧱 Project Structure
TWITTER_APP/
│
├── app/
│   ├── models/          # Database models
│   ├── routes/          # Auth, blog, profile routes
│   ├── static/          # CSS & uploaded images
│   ├── templates/       # Jinja2 templates
│   ├── __init__.py
│   ├── config.py        # Application configuration
│   └── extensions.py   # SQLAlchemy, LoginManager, Mail
│
├── migrations/          # Flask-Migrate files
│
├── .env                 # Environment variables (not tracked)
├── .gitignore
├── requirements.txt
├── pyproject.toml
├── run.py               # Application entry point
├── uv.lock
└── README.md

🛠️ Tech Stack
Layer	Technology
Backend	Flask
Database	PostgreSQL
ORM	SQLAlchemy
Auth	Flask-Login
Migration	Flask-Migrate
Email	Flask-Mail
Templates	Jinja2
Frontend	HTML, CSS
⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/meetfvtagline/twitter_app.git
cd twitter_app

2️⃣ Create & Activate Virtual Environment
Linux / macOS
python3 -m venv venv
source venv/bin/activate

Windows
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

🔐 Environment Variables (.env)

Create a .env file in the project root:

SECRET_KEY=super-secret-key
DATABASE_URL=postgresql://postgres:root@localhost:5432/twitter_db
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_google_app_password


⚠️ .env is ignored by Git for security reasons.

🗄️ PostgreSQL Database Setup
1️⃣ Install PostgreSQL

Download from:
👉 https://www.postgresql.org/download/

Default credentials used in this project:

Username: postgres

Password: root

2️⃣ Create Database
CREATE DATABASE twitter_db;

3️⃣ Run Database Migrations
flask db init       # run once
flask db migrate -m "Initial migration"
flask db upgrade

📧 Email Configuration (Password Reset)

This project uses Gmail SMTP with Google App Passwords.

🔹 MAIL_USERNAME

Use your Gmail address:

MAIL_USERNAME=meetfv.tagline@gmail.com

🔹 How to Create Google App Password

⚠️ 2-Step Verification must be enabled

Steps:

Go to 👉 https://myaccount.google.com

Open Security

Enable 2-Step Verification

Go to Security → App Passwords

Select:

App → Mail

Device → Other

Generate password

Copy the 16-character password

MAIL_PASSWORD=abcdefghijklmnop


✅ Use this instead of your Gmail password.

▶️ Running the Application

Make sure:

Virtual environment is active

PostgreSQL is running

.env file exists

Run the app:

python run.py


Open in browser:

http://127.0.0.1:5000

👤 User Flow

Open application URL

Register a new account

Login

Create short blogs (15-word limit)

Upload images

Like other users’ posts

Edit profile

Reset password via email if needed

❗ Error Handling

Handled scenarios include:

Invalid login credentials

Duplicate email registration

Blog text exceeding word limit

Unauthorized access

Invalid reset tokens

Invalid image uploads

🔒 Security Notes

.env excluded from version control

Passwords are hashed

CSRF protection enabled

Secure email-based password reset

📌 Future Enhancements

Follow / Unfollow users

AJAX-based likes

Comments system

Pagination

Deployment (Docker / AWS / Render)

👨‍💻 Author

Meet FV Tagline
GitHub: https://github.com/meetfvtagline
