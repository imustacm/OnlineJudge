from core.db import db


class ForumSection(db.Model):
    __tablename__ = 'forum_section'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    title = db.Column(db.VARCHAR(128))
    content = db.Column(db.TEXT)
    create_time = db.Column(db.TIMESTAMP)
    last_update_time = db.Column(db.TIMESTAMP)
    create_user = db.Column(db.INTEGER)
    subject_number = db.Column(db.INTEGER, default=0)
    note_number = db.Column(db.INTEGER, default=0)
    visible = db.Column(db.BOOLEAN, nullable=False, default=True)


class ForumSubject(db.Model):
    __tablename__ = 'forum_subject'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    title = db.Column(db.VARCHAR(128))
    section_id = db.Column(db.INTEGER)
    create_time = db.Column(db.TIMESTAMP)
    create_user = db.Column(db.INTEGER)
    good_flag = db.Column(db.BOOLEAN, nullable=False, default=False)
    up_flag = db.Column(db.BOOLEAN, nullable=False, default=False)
    view_number = db.Column(db.INTEGER, default=0)
    admire_number = db.Column(db.INTEGER, default=0)
    reply_number = db.Column(db.INTEGER, default=0)
    visible = db.Column(db.BOOLEAN, nullable=False, default=True)


class ForumNote(db.Model):
    __tablename__ = 'forum_note'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    subject_id = db.Column(db.INTEGER)
    section_id = db.Column(db.INTEGER)
    content = db.Column(db.TEXT)
    floor_number = db.Column(db.INTEGER)
    create_time = db.Column(db.TIMESTAMP)
    create_user = db.Column(db.INTEGER)
    visible = db.Column(db.BOOLEAN, nullable=False, default=True)

