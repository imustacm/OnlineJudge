from core.db import db
from utils.model_to_dict import to_dict_tools


class Problem(db.Model):
    __tablename__ = 'problem'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    title = db.Column(db.VARCHAR(128))
    description = db.Column(db.TEXT)
    input = db.Column(db.TEXT)
    output = db.Column(db.TEXT)
    sample = db.Column(db.JSON)
    test_case_id = db.Column(db.VARCHAR(64))
    test_case_score = db.Column(db.JSON)
    hint = db.Column(db.TEXT)
    languages = db.Column(db.JSON)
    time_limit = db.Column(db.INTEGER)
    memory_limit = db.Column(db.INTEGER)
    difficulty = db.Column(db.INTEGER)
    source = db.Column(db.VARCHAR(128))
    spj_flag = db.Column(db.BOOLEAN, nullable=False, default=False)
    submit_number = db.Column(db.INTEGER)
    accepted_number = db.Column(db.INTEGER)
    create_time = db.Column(db.TIMESTAMP)
    last_update_time = db.Column(db.TIMESTAMP)
    create_user = db.Column(db.INTEGER)
    visible = db.Column(db.BOOLEAN, nullable=False, default=True)

    def __repr__(self):
        return '<School %r>' % self.name

    def to_dict(self):
        dict_info = to_dict_tools(self)
        return dict_info


class ProblemTag(db.Model):
    __tablename__ = 'problem_tag'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    name = db.Column(db.VARCHAR(128))
    visible = db.Column(db.BOOLEAN, nullable=False, default=True)


class ProblemToTag(db.Model):
    __tablename__ = 'problem_to_tag'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    problem_id = db.Column(db.INTEGER)
    problem_tag_id = db.Column(db.INTEGER)
