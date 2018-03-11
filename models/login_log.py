from core.db import db


class LoginLog(db.Model):
    __tablename__ = 'login_log'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    user_id = db.Column(db.INTEGER)
    create_time = db.Column(db.TIMESTAMP)
    ip = db.Column(db.VARCHAR(32))
    success_flag = db.Column(db.BOOLEAN)
