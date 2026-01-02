🐦 Flask Twitter-Like Microblogging App

A Twitter-inspired microblogging application built with Flask.
Focused on authentication, posting short blogs, likes, image uploads, and profiles, with PostgreSQL and email-based password recovery.

📸 What This Project Does

✔ Allows users to register & login securely
✔ Users can post short blogs (15-word limit)
✔ Blogs support image uploads
✔ Users can like posts (count updates on refresh)
✔ Blogs are shown in LIFO order (latest first)
✔ Users can create & edit profiles
✔ Forgot / Reset Password via email
✔ Uses PostgreSQL + Flask-Migrate
✔ Proper error handling at every level

🎯 Design is minimal — functionality is the priority

🧱 Project Structure
TWITTER_APP/
│
├── app/
│   ├── models/          # Database models
│   ├── routes/          # Application routes (auth, blog, profile)
│   ├── static/          # CSS, uploaded images
│   ├── templates/       # Jinja2 templates
│   ├── __init__.py
│   ├── config.py        # App configuration
│   └── extensions.py   # DB, LoginManager, Mail
│
├── migrations/          # Database migrations
│
├── .env                 # Environment variables (NOT pushed to Git)
├── .gitignore
├── requirements.txt
├── pyproject.toml
├── run.py               # App entry point
├── uv.lock
└── README.md

🚀 Features Overview
🔐 Authentication

Register

Login

Logout

Forgot Password

Reset Password (Email-based)

✍️ Microblogging

Maximum 15 words per blog

Image upload support

Latest posts shown first (LIFO)

❤️ Likes

Like counter visible to all users

Count updates on page refresh

👤 User Profile

Create profile

Edit profile (logged-in users)

🛡️ Security & Validation

Password hashing

CSRF protection

Secure email tokens

Proper error messages

🛠️ Tech Stack
Category	Technology
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

Take note of:

Username (default: postgres)

Password (example used: root)

2️⃣ Create Database
CREATE DATABASE twitter_db;

3️⃣ Run Database Migrations
flask db init       # only first time
flask db migrate -m "Initial migration"
flask db upgrade

📧 Email Setup (Forgot / Reset Password)

This app uses Gmail SMTP with Google App Passwords.

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

Ensure:

Virtual environment is active

PostgreSQL is running

.env file exists

Run:

python run.py


Open browser:

http://127.0.0.1:5000

👤 How Users Use the App

Open the app URL

Register a new account

Login

Create blogs (15-word limit)

Upload images

Like other users’ posts

Edit profile

Reset password via email if needed

❗ Error Handling

Handled scenarios include:

Invalid login credentials

Duplicate registration

Blog exceeding word limit

Unauthorized access

Invalid reset token

Invalid file uploads

🔒 Security Notes

.env excluded from version control

Passwords are hashed

Secure email tokens

CSRF protection enabled

📌 Future Enhancements

Follow / Unfollow users

AJAX likes

Comments

Pagination

Deployment (Docker / AWS / Render)

👨‍💻 Author

Meet FV Tagline
GitHub: https://github.com/meetfvtagline

If you want, I can also:

Add screenshots section

Add API documentation

Optimize README for interview submission

Make a deployment README

Just say the word 🚀