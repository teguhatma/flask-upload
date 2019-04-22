from app import db

__maxsize__ = 102400


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    first_name = db.Column(db.String(64), unique=True)
    last_name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    photos = db.Column(db.LargeBinary(__maxsize__), nullable=True)
    photos_filename = db.Column(db.String, nullable=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)