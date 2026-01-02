🐦 Flask Twitter-like Microblogging App

A microblogging web application built using Flask that mimics core Twitter features such as authentication, posting short blogs, liking posts, image uploads, and user profiles.

The focus of this project is working functionality, not UI design.

🚀 Features

User Authentication

Register

Login

Logout

Forgot Password

Reset Password (Email-based)

Microblogging

Post blogs with maximum 150 words

Upload images with posts

Blogs shown in LIFO (Latest First) order

Likes

Like counter visible to all users

Like count updates on page refresh

User Profile

Profile creation

Edit profile for logged-in users

Database

PostgreSQL with migrations

Security

Environment variables via .env

Password hashing

Error Handling

Proper validation and error messages

Templating

Jinja2 templates

Simple HTML & CSS

🛠️ Tech Stack

Python 3.8+

Flask

Flask-SQLAlchemy

Flask-Migrate

Flask-Login

Flask-Mail

PostgreSQL

Jinja2

HTML / CSS

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/meetfvtagline/twitter_app.git
cd twitter-app

2️⃣ Create & Activate Virtual Environment
On Linux / macOS:
python3 -m venv venv
source venv/bin/activate

On Windows:
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

🔐 Environment Variables (.env)

This project uses environment variables for security.

Create a .env file in the root directory
SECRET_KEY=super-secret-key
DATABASE_URL=postgresql://postgres:root@localhost:5432/twitter_db
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_google_app_password


⚠️ Important:
The .env file is NOT pushed to Git. Each user must create it manually.

🗄️ PostgreSQL Database Setup
1️⃣ Install PostgreSQL

Download from: https://www.postgresql.org/download/

Install and note:

Username (default: postgres)

Password (example used: root)

2️⃣ Create Database

Open PostgreSQL shell (psql) or PgAdmin and run:

CREATE DATABASE twitter_db;

3️⃣ Database Migration

Initialize migrations (only first time):

flask db init


Create migration files:

flask db migrate -m "Initial migration"


Apply migrations:

flask db upgrade

📧 Email Configuration (Forgot / Reset Password)

This project uses Gmail SMTP with Google App Passwords.

🔹 How MAIL_USERNAME is obtained

Use your Gmail address

Example:

MAIL_USERNAME=meetfv.tagline@gmail.com

🔹 How to Create Google App Password

⚠️ You must enable 2-Step Verification on your Google account.

Steps:

Go to Google Account

https://myaccount.google.com

Click Security

Enable 2-Step Verification

After enabling, go to:

Security → App Passwords

Select:

App: Mail

Device: Other

Generate password

Copy the 16-character password

Paste it into .env

MAIL_PASSWORD=abcdefghijklmnop


✅ Use this password instead of your Gmail password.

▶️ Running the Application

Make sure:

Virtual environment is activated

PostgreSQL is running

.env file exists

Run the app:

python run.py


The app will be available at:

http://127.0.0.1:5000/

👤 How Users Can Access the App

Open browser

Go to http://127.0.0.1:5000

Register a new account

Login

Create blogs (15-word limit)

Upload images

Like other users’ blogs

Edit profile

Reset password if forgotten (via email)

❗ Error Handling

Invalid login credentials

Duplicate email registration

Blog text exceeding 15 words

Unauthorized access prevention

Invalid password reset tokens

File upload validation

All handled with proper messages.

🔒 Security Notes

.env file is ignored via .gitignore

Passwords are hashed

CSRF protection enabled

Secure email-based password reset