from app import db #En bref : on importe depuis le package (app), pas directement depuis __init__.

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.Boolean, default=False, nullable=False)  # False = user, True = admin

    def __repr__(self):
        role_name = "Admin" if self.role else "User"
        return f"<User {self.username} ({role_name})>"
