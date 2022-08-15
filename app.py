from flask import Flask, render_template
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://fgalvan:test123@localhost/to_dodb'

db = SQLAlchemy(app)

class To_Do(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


@app.route('/')
def index():
    todo_list = To_Do.query.all()
    print(todo_list)
    return render_template('base.html', todo_list = todo_list)

if __name__ == "__main__":
    db.create_all()

    app.run(debug=True)