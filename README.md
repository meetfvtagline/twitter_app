# 🐦 Flask Twitter-Like Microblogging App

A **Twitter-inspired microblogging application** built using **Flask** and **PostgreSQL**.
This project focuses on **backend fundamentals**, **secure authentication**, **role-based access**, and a **clean, scalable architecture** rather than UI design.

---

## ✨ Overview

This application allows users to:

* Create short microblogs
* Upload images
* Like posts
* Manage profiles
* Securely recover passwords via email

🧑‍💼 An **Admin Panel** is included for managing users and content.

🎯 **Goal:** Demonstrate Flask fundamentals, authentication, authorization, database design, and clean project structure.

---

## 🔥 Key Features

### 🔐 Authentication

* User Registration
* Login & Logout
* Forgot Password
* Reset Password via Email (Token-based)

### ✍️ Microblogging

* Create blogs (**max 150 words**)
* Upload images with posts
* Blogs displayed in **LIFO order** (latest first)

### ❤️ Likes

* Like posts from other users
* Like count updates on page refresh

### 👤 User Profiles

* Profile creation
* Edit profile (**logged-in users only**)

### 🛡️ Security & Validation

* Password hashing
* CSRF protection
* Secure email tokens
* Proper validation & user-friendly error messages

### 🧑‍💼 Admin Panel (NEW)

* Admin dashboard
* View & delete users
* View & delete blogs
* Role-based access control (**admin vs user**)
* Admins created **only via Flask shell**

---

## 🧱 Updated Project Structure

```text
TWITTER_APP/
│
├── app/
│   ├── models/              # Database models
│   │   └── user.py
│   │
│   ├── routes/
│   │   ├── admin.py         # Admin routes (protected)
│   │   ├── auth.py          # Authentication routes
│   │   ├── home.py          # User dashboard & blogs
│   │   └── utils.py
│   │
│   ├── static/              # CSS & uploaded images
│   │
│   ├── templates/
│   │   ├── admin/           # Admin templates
│   │   │   ├── admin_dashboard.html
│   │   │   ├── all_blog.html
│   │   │   └── all_users.html
│   │   │
│   │   ├── create_blog.html
│   │   ├── dashboard.html
│   │   ├── forget_pass.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── password_change.html
│   │   ├── profile.html
│   │   ├── register.html
│   │   ├── reset_password.html
│   │   └── update_blog.html
│   │
│   ├── __init__.py
│   ├── config.py            # Application configuration
│   └── extensions.py        # SQLAlchemy, LoginManager, Mail
│
├── migrations/              # Flask-Migrate files
│
├── .env                     # Environment variables (not tracked)
├── .gitignore
├── requirements.txt
├── pyproject.toml
├── run.py                   # Application entry point
├── uv.lock
└── README.md
```

---

## 🛠️ Tech Stack

| Layer     | Technology    |
| --------- | ------------- |
| Backend   | Flask         |
| Database  | PostgreSQL    |
| ORM       | SQLAlchemy    |
| Auth      | Flask-Login   |
| Migration | Flask-Migrate |
| Email     | Flask-Mail    |
| Templates | Jinja2        |
| Frontend  | HTML, CSS     |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/meetfvtagline/twitter_app.git
cd twitter_app
```

### 2️⃣ Create & Activate Virtual Environment

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**

```bash
python -m venv venv
venv\\Scripts\\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables (`.env`)

Create a `.env` file in the project root:

```env
SECRET_KEY=super-secret-key
DATABASE_URL=postgresql://postgres:root@localhost:5432/twitter_db
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_google_app_password
```

⚠️ `.env` is ignored by Git for security reasons.

---

## 🗄️ PostgreSQL Database Setup

### 1️⃣ Install PostgreSQL

👉 [https://www.postgresql.org/download/](https://www.postgresql.org/download/)

**Default credentials:**

* Username: `postgres`
* Password: `root`

### 2️⃣ Create Database

```sql
CREATE DATABASE twitter_db;
```

### 3️⃣ Run Database Migrations

```bash
flask db init        # Run once
flask db migrate -m "Initial migration"
flask db upgrade
```

---

## 📧 Email Configuration (Password Reset)

Uses **Gmail SMTP** with **Google App Passwords**.

⚠️ **2-Step Verification must be enabled**

**Steps:**

1. Go to 👉 [https://myaccount.google.com](https://myaccount.google.com)
2. Security → Enable 2-Step Verification
3. Security → App Passwords
4. App → Mail
5. Device → Other
6. Generate password

```env
MAIL_PASSWORD=abcdefghijklmnop
```

✅ Use this **instead of your Gmail password**.

---

## ▶️ Running the Application

Ensure:

* Virtual environment is active
* PostgreSQL is running
* `.env` file exists

```bash
python run.py
```

Open in browser:
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧑‍💼 Admin Panel Guide (IMPORTANT)

### 🔑 Admin Access

* Admin users have `role = "admin"`
* Normal users have `role = "user"`
* Admin panel is **not publicly accessible**

### 🌐 Admin Panel URL

```
http://127.0.0.1:5000/admin/dashboard
```

### 🛠️ Creating an Admin User (Flask Shell)

Admins **cannot** be created via UI.

```bash
flask shell
```

```python
from app import db
from app.models.user import User
from werkzeug.security import generate_password_hash

admin = User(
    username="admin",
    email="admin@example.com",
    password_hash=generate_password_hash("admin123"),
    role="admin"
)

db.session.add(admin)
db.session.commit()
```

Login:

* Email: `admin@example.com`
* Password: `admin123`

Then visit:

```
/admin/dashboard
```

---

## 👤 User Flow

1. Open application URL
2. Register a new account
3. Login
4. Create short blogs (150-word limit)
5. Upload images
6. Like other users’ posts
7. Edit profile
8. Reset password via email if needed

---

## ❗ Error Handling

* Invalid login credentials
* Duplicate email registration
* Blog text exceeding word limit
* Unauthorized access
* Invalid reset tokens
* Invalid image uploads

---

## 🔒 Security Notes

* `.env` excluded from version control
* Passwords are securely hashed
* CSRF protection enabled
* Secure email-based password reset
* Admin routes protected via role-based access

---

## 📌 Future Enhancements

* Follow / Unfollow users
* AJAX-based likes
* Comments system
* Pagination
* Deployment (Docker / AWS / Render)
* Super-Admin roles
* Admin activity logs

---

## 👨‍💻 Author

**Meet FV Tagline**
GitHub 👉 [https://github.com/meetfvtagline](https://github.com/meetfvtagline)

⭐ *If you like this project, consider giving it a star on GitHub!*
