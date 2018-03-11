from core.db import db


class Contest(db.Model):
    __tablename__ = 'contest'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    title = db.Column(db.VARCHAR(128))
    content = db.Column(db.TEXT)
    close_rank_flag = db.Column(db.BOOLEAN, nullable=False, default=True)
    close_rank_time = db.Column(db.INTEGER)
    contest_flag = db.Column(db.BOOLEAN, nullable=False, default=False)
    permission_type = db.Column(db.INTEGER)
    password = db.Column(db.VARCHAR(32))
    user_group_id = db.Column(db.INTEGER)
    start_time = db.Column(db.TIMESTAMP)
    end_time = db.Column(db.TIMESTAMP)
    create_time = db.Column(db.TIMESTAMP)
    last_update_time = db.Column(db.TIMESTAMP)
    create_user = db.Column(db.INTEGER)
    allow_mail = db.Column(db.BOOLEAN, nullable=False, default=True)
    visible = db.Column(db.BOOLEAN, nullable=False, default=True)


class ContestNotice(db.Model):
    __tablename__ = 'contest_notice'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    title = db.Column(db.VARCHAR(128))
    content = db.Column(db.TEXT)
    contest_id = db.Column(db.INTEGER)
    create_time = db.Column(db.TIMESTAMP)
    create_user = db.Column(db.INTEGER)
    visible = db.Column(db.BOOLEAN, nullable=False, default=True)


class ContestProblem(db.Model):
    __tablename__ = 'contest_problem'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    contest_id = db.Column(db.INTEGER)
    problem_id = db.Column(db.INTEGER)
    number = db.Column(db.INTEGER)
