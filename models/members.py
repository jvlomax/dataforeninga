from main import db


class Members(db.Model):
    __bind_key__ = "td"
    __tablename__ = "members"
    uid = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(15), nullable=False)
    last_name = db.Column(db.String(15), nullable=False)
    position = db.Column(db.String(20), nullable=False, default="member")
    phone = db.Column(db.String(15), nullable=True)
    mail = db.Column(db.String(30), nullable=False)