from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    mobile = db.Column(db.String(15), unique=True, nullable=False)  # Adjusted to store mobile as string
