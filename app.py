from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Kariya Loku scene da! Donige birthday lagai kiyl scene thiyagnn epa !!!"
