from flask import Flask
from flask import render_template
from flask import request
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/route_name', methods=['GET', 'POST'])
def method_name():
    pass
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']
        confirmpassword = request.form['confirmpassword']

    return render_template("registro.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
