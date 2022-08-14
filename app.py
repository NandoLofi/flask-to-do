from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello!"

@app.route('/about')
def about():
    return "About"

@app.route('/new')
def new():
    return "Create here"

@app.route('/delete'):
def delete():
    return "Delete"

if __name__ == "__main__":
    app.run(debug=True)