import base64
import hashlib

from core.db import db


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    username = db.Column(db.VARCHAR(32))
    password_hash = db.Column(db.VARCHAR(128))
    head_image = db.Column(db.VARCHAR(128))
    real_name = db.Column(db.VARCHAR(32))
    email = db.Column(db.VARCHAR(128))
    create_time = db.Column(db.TIMESTAMP)
    ip = db.Column(db.VARCHAR(32))
    problem_page = db.Column(db.INTEGER, default=1)
    submit_language = db.Column(db.INTEGER, default=0)
    submit_number = db.Column(db.INTEGER, default=0)
    accepted_number = db.Column(db.INTEGER, default=0)
    gender = db.Column(db.BOOLEAN)
    school = db.Column(db.VARCHAR(64))
    telephone = db.Column(db.VARCHAR(32))
    mood = db.Column(db.VARCHAR(256))
    major = db.Column(db.VARCHAR(32))
    grade = db.Column(db.INTEGER)
    clazz = db.Column(db.INTEGER)
    qq = db.Column(db.VARCHAR(32))
    student_number = db.Column(db.VARCHAR(32))
    blog = db.Column(db.VARCHAR(256))
    github = db.Column(db.VARCHAR(256))
    reset_password_token = db.Column(db.VARCHAR(32))
    reset_password_time = db.Column(db.TIMESTAMP)
    session_keys = db.Column(db.JSON)
    visible = db.Column(db.BOOLEAN, nullable=False, default=True)

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        md5 = hashlib.md5(password.encode()).hexdigest()
        self.password_hash = base64.b64encode(md5.encode()).decode()

    def verify_password(self, password):
        md5 = hashlib.md5(password.encode()).hexdigest().encode()
        password = base64.b64encode(md5).decode()
        if password == self.password_hash:
            return True
        return False


class UserGroup(db.Model):
    __tablename__ = 'user_group'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    title = db.Column(db.VARCHAR(128))
    visible = db.Column(db.BOOLEAN, nullable=False, default=True)


class UserToGroup(db.Model):
    __tablename__ = 'user_to_group'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    user_id = db.Column(db.INTEGER)
    user_group_id = db.Column(db.INTEGER)
    visible = db.Column(db.BOOLEAN, nullable=False, default=True)
