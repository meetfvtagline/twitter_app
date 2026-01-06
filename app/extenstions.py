'''
Docstring for app.extenstions

Needed Extenstion for Our Application like database,csrf,mail etc..
'''

from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail

db = SQLAlchemy()
csrf = CSRFProtect()
mail=Mail()     

