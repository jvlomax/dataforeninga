from flask import Flask, render_template, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.babel import Babel
from flask.ext.user import current_user, login_required, UserManager, UserMixin, SQLAlchemyAdapter
from wtforms.validators import ValidationError
import config

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

db.create_all()

db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter, password_validator=password_validator)
user_manager.init_app(app)


@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")


@app.route("/admin")
@app.route("/admin.html")
@login_required
def admin():
    return render_template("admin.html")


if __name__ == "__main__":
    app.run(debug=True)