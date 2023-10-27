from flask import Flask, request, jsonify
from utils_db import *


# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Define una ruta para la página de inicio
@app.route('/')
def hello_world():
  return 'Hola, Mundo!'

# Ruta para el endpoint /query
@app.route('/query')
def query_item():
  # Obtener el parámetro "ItemID" de la URL
  item_id = request.args.get('ItemID')

  if item_id is not None:
    # Llamar a la función see_item y devolver el resultado como JSON
    item_info = see_item(item_id)
    return jsonify(item_info)
  else:
    return jsonify({"error": "Parámetro ItemID faltante en la URL"})


@app.route('/query', methods=['GET'])
def query_all_products():
  product_type = request.args.get('type')

  if product_type == 'ALL':
    all_products = get_all_products()
    return jsonify(all_products)
  else:
    return jsonify({"error": "Parámetro type debe ser 'ALL'"})

@app.route('/buy', methods=['POST'])
def buy_item():
  try:
    data = request.get_json()
    item_id = data.get('ItemId')
    quantity_to_buy = data.get('Quantity')

    if item_id is not None and quantity_to_buy is not None:
      result = buy_product(item_id, quantity_to_buy)
      return jsonify(result)
    else:
      return jsonify({"error": "Faltan parámetros en la solicitud"})
  except Exception as e:
    return jsonify({"error": "Ocurrió un error en la compra"})

# Inicia la aplicación si se ejecuta este archivo
if __name__ == '__main__':
  app.run()
