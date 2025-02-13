import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///rumorthink.db')
    SECRET_KEY = os.getenv('SECRET_KEY', 'rumorthink_secret')
