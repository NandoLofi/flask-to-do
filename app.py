from flask import Flask, render_template
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = '/Users/fgalvan/Library/ApplicationSupport/Postgres/var-14/postgresql.conf'

db = SQLAlchemy(app)

class To_Do(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


@app.route('/')
def index():
    return render_template('base.html')

if __name__ == "__main__":
    app.run(debug=True)