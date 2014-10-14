from flask import Flask, render_template, url_for, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.babel import Babel
from flask.ext.user import current_user, login_required, UserManager, UserMixin, SQLAlchemyAdapter
from wtforms.validators import ValidationError
import config
from util import isOnline
import os

#from models.members import Members
#from models.servers import Servers
import random
app = Flask(__name__)
app.config.from_object(config)
if os.environ.get("FLASK_PRODUCTION_CONFIG"):
    app.config.from_envvar("FLASK_PRODUCTION_CONFIG")
db = SQLAlchemy(app)
babel = Babel(app)


def password_validator(form, field):
    password = field.data
    if len(password) < 4:
        raise ValidationError(_("Password must be at least 4 characters"))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean(), nullable=False, default=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)


class Servers(db.Model):
    sid = db.Column(db.Integer, primary_key=True, nullable=False)
    uid = db.Column(db.Integer, nullable=False)
    server_name = db.Column(db.String(20), nullable=False)
    ip_address = db.Column(db.String(15), nullable=False)


class Members(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(15), nullable=False)
    last_name = db.Column(db.String(15), nullable=False)
    position = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(15), nullable=True, default=None)
    mail = db.Column(db.String(30), nullable=False)
    payed = db.Column(db.Boolean, nullable=False, default=False)

db.create_all()


db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter, password_validator=password_validator)
user_manager.init_app(app)

"""
Static public pages
"""
@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")


@app.route("/styret")
@app.route("/styret.html")
def styret():
    board = Members.query.filter(Members.position != "member").all()
    random.shuffle(board)
    sorted_board = sorted(board, key=board_sorter)
    return render_template("styret.html", board_members=sorted_board)

def board_sorter(x):
    if x.position == "Leader":
        return 1
    if x.position == "Deputy":
        return 2
    elif x.position == "Economy":
        return 3
    elif x.position == "Secretary":
        return 4
    elif x.position == "Tech":
        return 5
    elif x.position == "Board member":
        return 6
    else:
        return 7

@app.route("/om")
@app.route("/om.html")
def om_oss():
    return render_template("om_oss.html")

@app.route("/kontakt")
@app.route("/kontakt.html")
def kontakt():
    return render_template("kontakt.html")

"""
Dashboard routes
"""

@app.route("/dashboard/overview.html")
@app.route("/admin")
def dashboard():
    members = Members.query.all()
    num_members = len(members)
    payers = len(Members.query.filter_by(payed=True).all())

    mock_data = [{"first_name": "Bjarne", "last_name":"Betjent"}, {"first_name":"Max", "last_name":"Mekker"}]
    return render_template("dashboard/overview.html", members=members, num_members=num_members, payers=payers)


@app.route("/dashboard/members.html")
def members():
    members = Members.query.all()
    return render_template("dashboard/members.html", members=members)

@app.route("/dashboard/servers.html")
def servers():
    servers = Servers.query.all()
    return render_template("dashboard/servers.html", servers=servers)


@app.route("/dashboard/export.html")
def export():
    return render_template("dashboard/export.html")


"""
Error and misc pages
"""

@app.errorhandler(404)
def page_not_found(e):
    #return render_template('404.html'), 404
    return "The route {} does not exist".format(request.url), 404

@app.route("/utils/isonline/<path:ip>")
def check_server(ip):


    if isOnline(ip):
        return jsonify(status="online", address=ip)
    else:
        return jsonify(status="offline", address=ip)
if __name__ == "__main__":


    app.run()
