"""Aplicación Flask que recibe un parámetro desde la URL."""

from flask import Flask


app = Flask(__name__)

@app.route("/")
def inicio(): #pag principal con las instrucciones
    return "Escribe en la URL: /estudiante/tu_nombre"


@app.route("/estudiante/<nombre>") #define la ruta
def estudiante(nombre):
    return f"Hola, {nombre}. Bienvenid@ al curso de Desarrollo Web."


if __name__ == "__main__":
    app.run(debug=True)