from flask import Flask, render_template

# Creamos la aplicación Flask
app = Flask(__name__)


# Ruta principal
@app.route("/")
def inicio():
    # Mostramos el archivo HTML
    return render_template("inicio.html")


# Ejecutamos la aplicación
if __name__ == "__main__":
    app.run(debug=True)