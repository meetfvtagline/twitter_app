# 🐦 Flask Twitter‑Like Microblogging App

A **Twitter‑inspired microblogging application** built using **Flask** and **PostgreSQL**.
This project focuses on **core backend functionality**, clean architecture, and secure authentication rather than UI design.

---

## ✨ Overview

This application allows users to create short microblogs, upload images, like posts, and manage profiles with **secure authentication** and **email‑based password recovery**.

🎯 **Goal:** Demonstrate Flask fundamentals, authentication, database design, and a clean, scalable project structure.

---

## 🔥 Key Features

### 🔐 Authentication

* User Registration
* Login & Logout
* Forgot Password
* Reset Password via Email (Token‑based)

### ✍️ Microblogging

* Create blogs with a **maximum of 15 words**
* Upload images with posts
* Blogs displayed in **LIFO order** (latest first)

### ❤️ Likes

* Like posts from other users
* Like counter updates on page refresh

### 👤 User Profiles

* Profile creation
* Edit profile (**logged‑in users only**)

### 🛡️ Security & Validation

* Password hashing
* CSRF protection
* Secure email tokens
* Proper validation & user‑friendly error messages

---

## 🧱 Project Structure

```text
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
```

---

## 🛠️ Tech Stack

| Layer     | Technology    |
| --------- | ------------- |
| Backend   | Flask         |
| Database  | PostgreSQL    |
| ORM       | SQLAlchemy    |
| Auth      | Flask‑Login   |
| Migration | Flask‑Migrate |
| Email     | Flask‑Mail    |
| Templates | Jinja2        |
| Frontend  | HTML, CSS     |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/meetfvtagline/twitter_app.git
cd twitter_app
```

---

### 2️⃣ Create & Activate Virtual Environment

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

---

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

⚠️ **Note:** `.env` is ignored by Git for security reasons.

---

## 🗄️ PostgreSQL Database Setup

### 1️⃣ Install PostgreSQL

Download from:
👉 [https://www.postgresql.org/download/](https://www.postgresql.org/download/)

**Default credentials used:**

* Username: `postgres`
* Password: `root`

---

### 2️⃣ Create Database

```sql
CREATE DATABASE twitter_db;
```

---

### 3️⃣ Run Database Migrations

```bash
flask db init        # Run once
flask db migrate -m "Initial migration"
flask db upgrade
```

---

## 📧 Email Configuration (Password Reset)

This project uses **Gmail SMTP** with **Google App Passwords**.

### 🔹 MAIL_USERNAME

Use your Gmail address:

```env
MAIL_USERNAME=meetfv.tagline@gmail.com
```

---

### 🔹 How to Create Google App Password

⚠️ **2‑Step Verification must be enabled**

**Steps:**

1. Go to 👉 [https://myaccount.google.com](https://myaccount.google.com)
2. Open **Security**
3. Enable **2‑Step Verification**
4. Go to **Security → App Passwords**
5. Select:

   * App → Mail
   * Device → Other
6. Generate password
7. Copy the **16‑character password**

```env
MAIL_PASSWORD=abcdefghijklmnop
```

✅ Use this **instead of your Gmail password**.

---

## ▶️ Running the Application

Make sure:

* Virtual environment is active
* PostgreSQL is running
* `.env` file exists

Run the app:

```bash
python run.py
```

Open in browser:
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 👤 User Flow

1. Open application URL
2. Register a new account
3. Login
4. Create short blogs (**15‑word limit**)
5. Upload images
6. Like other users’ posts
7. Edit profile
8. Reset password via email if needed

---

## ❗ Error Handling

Handled scenarios include:

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
* Secure email‑based password reset

---

## 📌 Future Enhancements

* Follow / Unfollow users
* AJAX‑based likes
* Comments system
* Pagination
* Deployment (Docker / AWS / Render)

---

## 👨‍💻 Author

**Meet FV Tagline**
GitHub 👉 [https://github.com/meetfvtagline](https://github.com/meetfvtagline)

---

⭐ *If you like this project, consider giving it a star on GitHub!*
