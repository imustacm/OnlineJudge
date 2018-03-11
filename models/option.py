from core.db import db


class Option(db.Model):
    __tablename__ = 'option'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    key = db.Column(db.VARCHAR(128))
    value = db.Column(db.JSON)
