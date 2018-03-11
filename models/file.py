from core.db import db


class File(db.Model):
    __tablename__ = 'file'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    title = db.Column(db.VARCHAR(128))
    content = db.Column(db.TEXT)
    file_img = db.Column(db.VARCHAR(128))
    file_type = db.Column(db.INTEGER)
    download_number = db.Column(db.INTEGER)
    view_number = db.Column(db.INTEGER)
    size = db.Column(db.VARCHAR(32))
    file_name_in = db.Column(db.VARCHAR(128))
    file_name_out = db.Column(db.VARCHAR(128))
    create_time = db.Column(db.TIMESTAMP)
    last_update_time = db.Column(db.TIMESTAMP)
    create_user = db.Column(db.INTEGER)
    visible = db.Column(db.BOOLEAN, nullable=False)


class FileType(db.Model):
    __tablename__ = 'file_type'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    title = db.Column(db.VARCHAR(128))
    create_time = db.Column(db.TIMESTAMP)
    last_update_time = db.Column(db.TIMESTAMP)
    create_user = db.Column(db.INTEGER)
    visible = db.Column(db.BOOLEAN, nullable=False)
