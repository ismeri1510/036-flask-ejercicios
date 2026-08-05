"""Primera aplicación Flask: muestra un saludo en la ruta principal."""
from flask import Flask #importamos la clase flsk

#creamos la app

app = Flask(__name__)

#esta ruta se ejecuta cuando entramos a la pag principal "/"

@app.route("/")
def inicio():
    """Muestra un mensaje de saludo en la página principal."""
    return "Hola, mundo soy Ismeri, esta es mi primer app con Flask jajaja."

#Ejecutamos la aplicacion solamente cuando abrimos el archivo directamente

if __name__=="__main__":
    app.run(debug=True)
