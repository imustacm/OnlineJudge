from core.db import db


class SignIn(db.Model):
    __tablename__ = 'sign_in'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    title = db.Column(db.VARCHAR(128))
    content = db.Column(db.TEXT)
    begin_time = db.Column(db.TIMESTAMP)
    end_time = db.Column(db.TIMESTAMP)
    multiple_ip_flag = db.Column(db.BOOLEAN)
    create_time = db.Column(db.TIMESTAMP)
    last_update_time = db.Column(db.TIMESTAMP)
    create_user = db.Column(db.INTEGER(db.INTEGER))
    visible = db.Column(db.BOOLEAN, nullable=False)


class SignInUser(db.Model):
    __tablename__ = 'sign_in_user'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    user_id = db.Column(db.INTEGER)
    sign_in_id = db.Column(db.INTEGER)
    create_time = db.Column(db.TIMESTAMP)
    ip = db.Column(db.VARCHAR(32))
    visible = db.Column(db.BOOLEAN)
