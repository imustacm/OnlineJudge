from core.db import db


class CoveryImg(db.Model):
    __tablename__ = 'covery_img'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    img_name = db.Column(db.VARCHAR(128))
    hyperlink_flag = db.Column(db.BOOLEAN, nullable=False, default=False)
    article_flag = db.Column(db.BOOLEAN, nullable=False, default=False)
    hyperlink = db.Column(db.VARCHAR(128))
    visible = db.Column(db.BOOLEAN, nullable=False, default=True)
