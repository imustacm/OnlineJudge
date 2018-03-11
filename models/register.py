from core.db import db


class Register(db.Model):
    __tablename__ = 'register'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    register_type_id = db.Column(db.INTEGER)
    name = db.Column(db.VARCHAR(128))
    gender = db.Column(db.BOOLEAN)
    student_number = db.Column(db.VARCHAR(32))
    telephone = db.Column(db.VARCHAR(32))
    qq = db.Column(db.VARCHAR(32))
    create_time = db.Column(db.TIMESTAMP)
    ip = db.Column(db.VARCHAR(32))


class RegisterType(db.Model):
    __tablename__ = 'register_type'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    name = db.Column(db.VARCHAR(128))
    create_time = db.Column(db.TIMESTAMP)
    last_update_time = db.Column(db.TIMESTAMP)
    create_user = db.Column(db.INTEGER)
    running_flag = db.Column(db.BOOLEAN, nullable=False, default=False)
    visible = db.Column(db.BOOLEAN, nullable=False, default=True)


