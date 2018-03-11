from core.db import db

class Similarity(db.Model):
    __tablename__ = 'similarity'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    solution_id_new = db.Column(db.INTEGER)
    solution_id_old = db.Column(db.INTEGER)
    similarity_percent = db.Column(db.INTEGER)
