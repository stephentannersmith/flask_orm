from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy #pylint: disable=import-error
from flask_migrate import Migrate #pylint: disable=import-error
from sqlalchemy.sql import func #pylint: disable=import-error

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dojos_ninjas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Dojo(db.Model):
	__tablename__ = "dojos"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))
	city = db.Column(db.String(255))
	state = db.Column(db.String(255))
	created_at = db.Column(db.DateTime, server_default=func.now())
	updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

class Ninja(db.Model):
	__tablename__ = "ninjas"
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(255))
	last_name = db.Column(db.String(255))
	dojos_id = db.Column(db.Integer, db.ForeignKey("dojos.id", ondelete="cascade"), nullable=False)
	dojo = db.relationship("Dojo", foreign_keys=[dojos_id], backref="ninjas")
	created_at = db.Column(db.DateTime, server_default=func.now())
	updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
	
	def full_name(self):
		return f"{self.first_name} {self.last_name}"

@app.route("/")
def main():
	# grabs all dojos
	dojo_results = Dojo.query.all()
	return render_template("main.html", dojos=dojo_results)

@app.route("/add_dojo", methods=["POST"])
def add_dojo():
	new_dojo = Dojo(name=request.form['name'], city=request.form['city'], state=request.form['state'])
	print("Adding new dojo...")
	print(new_dojo)
	db.session.add(new_dojo)
	db.session.commit()

	return redirect("/")

@app.route("/add_ninja", methods=["POST"])
def add_ninja():
	new_ninja = Ninja(first_name=request.form['first_name'], last_name=request.form['last_name'], dojo=Dojo.query.get(request.form['id']))

	print("Adding new ninja...")
	print(new_ninja)
	db.session.add(new_ninja)
	db.session.commit()
	return redirect("/")

if __name__ == "__main__":
	app.run(debug=True)