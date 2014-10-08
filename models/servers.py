from main import db


class Servers(db.Model):
    __bind_key__ = "td"
    __tablename__ = "servers"
    sid = db.Column(db.Integer, primary_key=True, nullable=False)
    uid = db.Column(db.Integer, nullable=False)
    server_name = db.Column(db.String(20), nullable=False)
    ip_address = db.Column(db.String(15), nullable=False)
