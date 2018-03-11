from core.db import db


class Mail(db.Model):
    __tablename__ = 'mail'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    title = db.Column(db.VARCHAR(128))
    content = db.Column(db.TEXT)
    create_time = db.Column(db.TIMESTAMP)
    create_user = db.Column(db.INTEGER)


class MailUser(db.Model):
    __tablename__ = 'mail_user'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    mail_id = db.Column(db.INTEGER)
    to_user = db.Column(db.INTEGER)
    read_time = db.Column(db.TIMESTAMP)
    visible = db.Column(db.BOOLEAN, nullable=False, default=True)
