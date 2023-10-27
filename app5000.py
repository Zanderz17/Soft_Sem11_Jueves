from flask import Flask, request, jsonify
from utils_db import *


# Crea una instancia de la aplicación Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hola, Mundo!'

# Ruta para el endpoint /query
@app.route('/query')
def query_item():
  item_id = request.args.get('ItemID')
  product_type = request.args.get('type')
  if item_id is not None:
    item_info = see_item(item_id)
    return jsonify(item_info)
  if product_type == 'ALL':
    all_products = get_all_products()
    return jsonify(all_products)
  else:
    return jsonify({"error": "Parámetro ItemID faltante en la URL"})


@app.route('/buy', methods=['POST'])
def buy_item():
  try:
    item_id = request.args.get('ItemId')
    quantity_to_buy = request.args.get('Quantity')
    print(item_id)
    
    if item_id is not None and quantity_to_buy is not None:
      result = buy_product(item_id, quantity_to_buy)
      return jsonify(result)
    else:
      return jsonify({"error": "Faltan parámetros en la solicitud"})
  except Exception as e:
    print(e)
    return jsonify({"error": "Ocurrió un error en la compra"})
  

# Inicia la aplicación si se ejecuta este archivo
if __name__ == '__main__':
  app.run(port=5000)
