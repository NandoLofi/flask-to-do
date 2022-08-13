from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello!"

@app.route('/about')
def about():
    return "About"

if __name__ == "__main__":
    app.run(debug=True)