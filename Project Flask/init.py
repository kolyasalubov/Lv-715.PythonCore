from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import secret_key, sql_alchemy_data_base_uri

app = Flask(__name__)
app.secret_key = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = sql_alchemy_data_base_uri

db = SQLAlchemy(app)
manager = LoginManager(app)

with app.app_context():
    db.create_all()
