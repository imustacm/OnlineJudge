from core.db import db


class SpecialJudge(db.Model):
    __tablename__ = 'special_judge'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    problem_id = db.Column(db.INTEGER)
    language = db.Column(db.VARCHAR(16))
    code = db.Column(db.TEXT)
    version = db.Column(db.VARCHAR(16))
    compile_flag = db.Column(db.BOOLEAN, nullable=False, default=False)
    