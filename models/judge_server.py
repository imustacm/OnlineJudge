from core.db import db


class JudgeServer(db.Model):
    __tablename__ = 'judge_server'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    hostname = db.Column(db.VARCHAR(128))
    ip = db.Column(db.VARCHAR(32))
    judger_version = db.Column(db.VARCHAR(32))
    cpu_core = db.Column(db.INTEGER)
    memory_usage = db.Column(db.FLOAT)
    cpu_usage = db.Column(db.FLOAT)
    last_heartbeat = db.Column(db.TIMESTAMP)
    create_time = db.Column(db.TIMESTAMP)
    task_number = db.Column(db.INTEGER)
    service_url = db.Column(db.VARCHAR(256))
    visible = db.Column(db.BOOLEAN, nullable=False, default=True)

