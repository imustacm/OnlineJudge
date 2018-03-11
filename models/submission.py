from core.db import db


class Submission(db.Model):
    __tablename__ = 'submission'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    problem_id = db.Column(db.INTEGER)
    contest_id = db.Column(db.INTEGER)
    user_id = db.Column(db.INTEGER)
    create_time = db.Column(db.TIMESTAMP)
    code = db.Column(db.TEXT)
    result = db.Column(db.INTEGER)
    info = db.Column(db.JSON)
    language = db.Column(db.VARCHAR(16))
    code_share = db.Column(db.BOOLEAN, nullable=False, default=False)
    statistic_info = db.Column(db.JSON)
    ip = db.Column(db.VARCHAR(32))
