from flask import Flask, request

# Creamos la aplicación Flask
app = Flask(__name__)


# Esta ruta acepta los métodos GET y POST
@app.route("/", methods=["GET", "POST"])
def formulario():
    # Si el usuario envía el formulario, se usa el método POST
    if request.method == "POST":
        # Obtenemos el dato escrito en el campo llamado "nombre"
        nombre = request.form["nombre"]

        # Mostramos un mensaje personalizado
        return f"Hola, {nombre}. Gracias por enviar el formulario."

    # Si la página se abre normalmente, se usa el método GET
    return """
    <h1>Formulario sencillo</h1>

    <form method="POST">
        <label>Escribe tu nombre:</label>
        <input type="text" name="nombre" required>
        <button type="submit">Enviar</button>
    </form>
    """


# Ejecutamos la aplicación
if __name__ == "__main__":
    app.run(debug=True)