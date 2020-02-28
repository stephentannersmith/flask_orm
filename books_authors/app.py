from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy #pylint: disable=import-error
from flask_migrate import Migrate #pylint: disable=import-error
from sqlalchemy.sql import func #pylint: disable=import-error

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

books_authors_table = db.Table('books_authors', 
db.Column('authors_id', db.ForeignKey('authors.id'), primary_key=True), 
db.Column('books_id', db.ForeignKey('books.id'), primary_key=True))

class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    desc = db.Column(db.Text)
    books_authors = db.relationship("Author", secondary=books_authors_table)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

class Author(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    notes = db.Column(db.Text)
    authors_books = db.relationship("Book", secondary=books_authors_table)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


@app.route("/")
def main():
    #grabs all info about books 
    book_results = Book.query.all()
    return render_template("index.html", book_results=book_results)

@app.route("/new_book", methods=["POST"])
def new_book():
    new_book = Book(title=request.form['title'], desc=request.form['desc'])
    print("Adding new book..")
    print(new_book)
    db.session.add(new_book)
    db.session.commit()
    return redirect("/")

@app.route("/book/<id>")
def book(id):
    book=Book.query.get(id)
    potential_authors = Author.query.all()
    return render_template("book.html", book=book, authors=potential_authors)

@app.route("/authors_books", methods=["POST"])
def add_author_book():
    author=Author.query.get(request.form['author_id'])
    book=Book.query.get(request.form['book_id'])
    print(author, book)
    author.authors_books.append(book)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

