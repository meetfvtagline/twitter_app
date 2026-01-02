🐦 Flask Microblog (Twitter-Like App)A feature-rich microblogging application built with Flask and PostgreSQL. This project demonstrates core backend engineering principles, including secure authentication, database relationship modeling, and automated email workflows.🚀 Key Features🔐 Authentication & SecuritySecure Auth: User registration, login, and logout powered by Flask-Login.Password Safety: Industry-standard password hashing using Werkzeug.Recovery: Token-based password reset via email (Gmail SMTP).Protection: Integrated CSRF protection and input validation.✍️ Microblogging EngineLIFO Feed: Posts are displayed in "Latest-In, First-Out" order.Constraint Logic: Strict 15-word limit for posts to maintain microblogging brevity.Media Support: Ability to upload and display images with posts.Social Interaction: Like system with dynamic counter updates.👤 User ManagementProfiles: Personalized profile pages.Authorization: Secure "Edit Profile" functionality restricted to the account owner.🛠️ Tech StackLayerTechnologyBackendFlask (Python)DatabasePostgreSQLORMSQLAlchemyMigrationsFlask-MigrateAuthenticationFlask-LoginMailingFlask-MailTemplatingJinja2📂 Project StructurePlaintextTWITTER_APP/
├── app/
│   ├── models/        # Database models (SQLAlchemy)
│   ├── routes/        # Blueprints for Auth, Blogs, and Profiles
│   ├── static/        # CSS, JavaScript, and Uploaded Images
│   ├── templates/     # Jinja2 HTML templates
│   ├── __init__.py    # App factory pattern
│   ├── config.py      # Environment configurations
│   └── extensions.py  # Extension initialization (Mail, DB, Login)
├── migrations/        # Database version control (Flask-Migrate)
├── run.py             # Entry point
├── .env               # Environment variables (Hidden)
└── requirements.txt   # Project dependencies
⚙️ Installation & Setup1. Clone & NavigateBashgit clone https://github.com/meetfvtagline/twitter_app.git
cd twitter_app
2. Environment SetupCreate a virtual environment and install dependencies:Bash# Windows
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
3. Configure Environment VariablesCreate a .env file in the root directory:Ini, TOMLSECRET_KEY=your_secret_key_here
DATABASE_URL=postgresql://postgres:root@localhost:5432/twitter_db
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_google_app_password
4. Database InitializationEnsure PostgreSQL is running and you have created the twitter_db database, then run:Bashflask db init
flask db migrate -m "Initial migration"
flask db upgrade
📧 Email Configuration (Password Reset)This project uses Gmail SMTP. To enable this:Enable 2-Step Verification in your Google Account.Go to Security > App Passwords.Generate a new password for "Mail" and "Other (Custom Name)".Paste the 16-character code into your .env as MAIL_PASSWORD.📌 Future Roadmap[ ] Real-time: Implement AJAX for likes and comments (no page refresh).[ ] Social: Follow/Unfollow system and personalized feeds.[ ] UX: Add pagination for the home feed.[ ] Deployment: Dockerize the application for AWS/Render deployment.👨‍💻 AuthorMeet FV TaglineGitHub: @meetfvtagline
