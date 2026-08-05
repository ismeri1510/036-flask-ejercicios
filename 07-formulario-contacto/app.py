from flask import Flask, render_template, request

# Creamos la aplicación Flask
app = Flask(__name__)


# Esta ruta acepta GET y POST
@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    # Si el usuario envía el formulario
    if request.method == "POST":
        # Obtenemos los datos escritos
        nombre = request.form["nombre"]
        mensaje = request.form["mensaje"]

        # Mostramos la página de agradecimiento
        return render_template(
            "gracias.html",
            nombre=nombre,
            mensaje=mensaje
        )

    # Si la ruta se abre normalmente, mostramos el formulario
    return render_template("contacto.html")


# Ejecutamos la aplicación
if __name__ == "__main__":
    app.run(debug=True)