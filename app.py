from flask import Flask,render_template,abort

app = Flask(__name__)

@app.route('/')
def inicio():
    return "<h1>Hello from flask</h1>"
