from flask import Flask, render_template, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.babel import Babel
from flask.ext.user import current_user, login_required, UserManager, UserMixin, SQLAlchemyAdapter
from wtforms.validators import ValidationError
import config
#from models.members import Members
#from models.servers import Servers

app = Flask(__name__)
app.config.from_object(config)

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


db.create_all()


db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter, password_validator=password_validator)
user_manager.init_app(app)


@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")


@app.route("/styret")
@app.route("/styret.html")
def showStyret():
    return render_template("styret.html")

@app.route("/admin")
@app.route("/admin.html")
def showAdmin():

    mock_data = [{"first_name": "Bjarne", "last_name":"Betjent"}, {"first_name":"Max", "last_name":"Mekker"}]
    return render_template("admin.html", members=mock_data)

@app.route("/servers")
def showServers():
    servers = Servers.query.all()
    return render_template("servers.html", servers=servers)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)