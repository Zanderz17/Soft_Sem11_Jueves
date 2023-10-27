from flask import Flask

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Define una ruta para la página de inicio
@app.route('/')
def hello_world():
    return 'Hola, Mundo!'

# Inicia la aplicación si se ejecuta este archivo
if __name__ == '__main__':
    app.run()
