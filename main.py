from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)


@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)