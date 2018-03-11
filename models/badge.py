from core.db import db


class Badge(db.Model):
    __tablename__ = 'badge'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    title = db.Column(db.VARCHAR(128))
    content = db.Column(db.TEXT)
    badge_img = db.Column(db.VARCHAR(128))
    badge_type = db.Column(db.INTEGER)
    create_time = db.Column(db.TIMESTAMP)
    last_update_time = db.Column(db.TIMESTAMP)
    create_user = db.INTEGER(db.INTEGER)
    visible = db.Column(db.BOOLEAN, nullable=False)


class BadgeType(db.Model):
    __tablename__ = 'badge_type'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    title = db.Column(db.VARCHAR(128))
    get_flag = db.Column(db.BOOLEAN)
    create_time = db.Column(db.TIMESTAMP)
    last_update_time = db.Column(db.TIMESTAMP)
    create_user = db.INTEGER(db.INTEGER)
    visible = db.Column(db.BOOLEAN, nullable=False)


class BadgeUser(db.Model):
    __tablename__ = 'badge_user'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    user_id = db.Column(db.INTEGER)
    badge_id = db.Column(db.INTEGER)
    create_time = db.Column(db.INTEGER)
    create_user = db.Column(db.INTEGER)
    visible = db.Column(db.BOOLEAN)
