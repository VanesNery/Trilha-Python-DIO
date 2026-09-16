from flask import Flask, request, url_for

app = Flask(__name__)


@app.route("/olamundo/<usuario>/<int:idade>/<float:altura>")
def hello_world(usuario, idade, altura):
    return {
        "usuario": usuario,
        "idade": idade,
        "altura": altura
    }


@app.route("/bemvindo")
def bem_vindo():
    return "<h1>Bem, vindo!</h1>"


@app.route("/projects/", methods=["GET", "POST"])
def projects():
    if request.method == "POST":
        return "<h1>Projects - POST</h1>"
    else:
        return "<h1>Projects - GET</h1>"


@app.route("/about")
def about():
    return "<h1>About</h1>"


with app.test_request_context():
    print(url_for('bem_vindo'))
    print(url_for('projects'))
    print(url_for('about', next='/'))
    print(url_for('hello_world', usuario='John Doe', idade=30, altura=1.75))