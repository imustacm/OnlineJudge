from core.db import db


class Permission(db.Model):
    __tablename__ = 'permission'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    title = db.Column(db.VARCHAR(128))
    content = db.Column(db.TEXT)


class PermissionUser(db.Model):
    __tablename__ = 'permission_user'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    permission_id = db.Column(db.INTEGER)
    user_id = db.Column(db.INTEGER)
    create_time = db.Column(db.TIMESTAMP)
    create_user = db.INTEGER(db.INTEGER)
    visible = db.Column(db.BOOLEAN, nullable=False, default=True)
