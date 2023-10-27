from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# URLs de las dos instancias de la aplicación Flask
app1_url = "http://127.0.0.1:5000"  # Reemplaza con la URL de tu primera instancia
app2_url = "http://127.0.0.1:5001"  # Reemplaza con la URL de tu segunda instancia

@app.route('/call_apps', methods=['GET'])
def call_apps():
    try:
        # Datos a enviar en el cuerpo de la solicitud POST
        data = {
            "ItemId": "1",
            "Quantity": "3"
        }

        # Realiza solicitudes POST a ambas instancias en paralelo
        response1 = requests.post(f"{app1_url}/buy", params=data)
        response2 = requests.post(f"{app2_url}/buy", params=data)

        # Puedes personalizar cómo deseas manejar las respuestas aquí

        return jsonify({
            "app1_response": response1.text,
            "app2_response": response2.text
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5002)  # Puedes elegir otro puerto si es necesario
