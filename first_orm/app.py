from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy #pylint: disable=import-error
from flask_migrate import Migrate #pylint: disable=import-error
from sqlalchemy.sql import func #pylint: disable=import-error

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# the instance of the ORM
db = SQLAlchemy(app)

# a tool for allowing migrations/creation of tables
migrate = Migrate(app, db)

# the db.Model in parentheses tells SQLAlchemy that this class represents a table in our database
class User(db.Model):
    #__tablename__ = "users" optional
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    email = db.Column(db.String(45))
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=func.now()) # notice the extra import statement above
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

@app.route("/")
def index():
    results = User.query.all()
    return render_template('index.html', users=results)

@app.route("/create_user", methods=["POST"])
def create_user():
    new_user = User(first_name=request.form['first_name'], last_name=request.form['last_name'], email=request.form['email'], age=request.form['age'])
    print("Adding new user...")
    print("new_user")
    db.session.add(new_user)
    db.session.commit()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)