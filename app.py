from flask import Flask, render_template


app = Flask(__name__)

livros = [
    {
        "id": 1,
        "titulo": "Python Fluente",
        "autor": "Luciano Ramalho",
        "ano": 2022,
        "disponivel": True,
    },
    {
        "id": 2,
        "titulo": "Flask Web Development",
        "autor": "Miguel Grinberg",
        "ano": 2018,
        "disponivel": False,
    },
    {
        "id": 3,
        "titulo": "Automatize Tarefas Maçantes com Python",
        "autor": "Al Sweigart",
        "ano": 2019,
        "disponivel": True,
    },
]


@app.route("/")
def inicio():
    return render_template("inicio.html")


if __name__ == "__main__":
    app.run(debug=True)