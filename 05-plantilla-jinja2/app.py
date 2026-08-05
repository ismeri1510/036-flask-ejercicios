from flask import Flask, render_template

# Creamos la aplicación Flask
app = Flask(__name__)


# Ruta principal
@app.route("/")
def inicio():
    # Esta variable se enviará al archivo HTML
    nombre = "Ismeri"

    # Mostramos la plantilla y enviamos la variable nombre
    return render_template("inicio.html", nombre=nombre)


# Ejecutamos la aplicación
if __name__ == "__main__":
    app.run(debug=True)