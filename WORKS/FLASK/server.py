from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def home():

    
    return "Hello, Flask!"

@app.route("/<name>")
def person(name):
    return f"<b>Hello, {escape(name)}!</b>"


if __name__=="__main__":
    app.run(debug=True)


