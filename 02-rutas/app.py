"""Aplicación Flask con varias rutas."""

from flask import Flask


app = Flask(__name__)


@app.route("/")
def inicio():
    """Página principal."""
    return "Página principal."


@app.route("/contacto")
def contacto():
    """Información de contacto."""
    return "Página de contacto: imachorrog@miumg.edu.gt"


@app.route("/cursos")
def cursos():
    """Información sobre los cursos."""
    return "Cursos disponibles: HTML, CSS, Python y Flask."


if __name__ == "__main__":
    app.run(debug=True)
    