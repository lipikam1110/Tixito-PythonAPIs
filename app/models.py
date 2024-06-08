from app import db
from sqlalchemy import CheckConstraint

class User(db.Model):
    __tablename__ = 'app_users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    mobile = db.Column(db.String(15), unique=True, nullable=False)
    whatsapp_notification_enabled = db.Column(db.Boolean, default=False, nullable=False)

    __table_args__ = (
        CheckConstraint("email LIKE '%@%.%'"),
    )
