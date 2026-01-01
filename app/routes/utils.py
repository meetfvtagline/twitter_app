from itsdangerous import URLSafeTimedSerializer
from flask import current_app

def generate_reset_token(email):
    s = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
    return s.dumps(email, salt="password-reset")

def verify_reset_token(token, expires=1800):  # 30 min
    s = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
    try:
        email = s.loads(token, salt="password-reset", max_age=expires)
    except:
        return None
    return email
