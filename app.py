from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/pc')
def pc():
    return render_template('pc.html')

@app.route('/console')
def console():
    return render_template('console.html')

@app.route('/trabalhe')
def produto1():
    return render_template('trabalhe.html')