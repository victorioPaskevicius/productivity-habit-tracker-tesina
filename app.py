from flask import Flask,render_template,abort

app = Flask(__name__)

@app.route('/')
def inicio():
    return "<h1>Hello from flask</h1>"

@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f"Hola {nombre}"

@app.route('/edad/<int:edad>')
def edad(edad):
    return f'La edad es {edad}'

@app.route('/inicio/<nombre>')
def mostrar(nombre):
    return render_template('./index.html', nombre=nombre)

@app.route('/error')
def error():
    return abort(404)

@app.errorhandler(404)
def notfound(error):
    return render_template('./notfound.html',error=error),404