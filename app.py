from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///rumorthink.db')
db = SQLAlchemy(app)

# Modelo de Usuarios
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    avatar_url = db.Column(db.String(255), default='https://rumorthink.com/default-avatar.png')
    tokens = db.Column(db.Integer, default=0)

# Modelo de Pensamientos
class Thought(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    votes = db.Column(db.Integer, default=0)

@app.route('/')
def home():
    return jsonify({'message': 'Bienvenido a RumorThink API'})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
