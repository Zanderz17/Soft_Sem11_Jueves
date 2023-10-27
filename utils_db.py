import psycopg2
from dotenv import load_dotenv
import os
import json


load_dotenv()
cwd = os.getcwd()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def see_item(id):
  try:
    connection = psycopg2.connect(
      host=DB_HOST,
      port=DB_PORT,
      database=DB_NAME,
      user=DB_USER,
      password=DB_PASSWORD
    )
    cursor = connection.cursor()

    cursor.execute("SELECT Name, Quantity FROM ShoppingCart WHERE ItemID = %s", (id,))
    result = cursor.fetchone()

    if result is not None:
      data = {
        "name": result[0],
        "quantity": result[1]
      }
      return json.dumps(data)
    else:
      return json.dumps({"error": "Producto no encontrado"})

  except Exception as e:
    print(f"Error: {e}")
    return json.dumps({"error": "Ocurrió un error"})
  finally:
    if connection:
      connection.close()


def buy_product(id, quantity_to_buy):
  try:
    connection = psycopg2.connect(
      host=DB_HOST,
      port=DB_PORT,
      database=DB_NAME,
      user=DB_USER,
      password=DB_PASSWORD
    )
    cursor = connection.cursor()

    # Obtener información del producto
    cursor.execute("SELECT Name, Quantity FROM ShoppingCart WHERE ItemID = %s", (id,))
    product_info = cursor.fetchone()

    if product_info is None:
      return json.dumps({"error": "Producto no encontrado"})

    product_name, current_quantity = product_info

    if current_quantity < quantity_to_buy:
      return json.dumps({"error": "Cantidad insuficiente en stock"})

    # Restar la cantidad comprada del stock
    new_quantity = current_quantity - quantity_to_buy
    cursor.execute("UPDATE ShoppingCart SET Quantity = %s WHERE ItemID = %s", (new_quantity, id))

    connection.commit()
    
    return json.dumps({"message": "Compra exitosa"})

  except Exception as e:
    print(f"Error: {e}")
    return json.dumps({"error": "Ocurrió un error en la compra"})
  finally:
    if connection:
      connection.close()

def get_all_products():
  try:
    connection = psycopg2.connect(
      host=DB_HOST,
      port=DB_PORT,
      database=DB_NAME,
      user=DB_USER,
      password=DB_PASSWORD
    )
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM ShoppingCart")
    result = cursor.fetchall()

    products = []
    for row in result:
      product = {
        "ItemID": row[0],
        "Name": row[1],
        "Quantity": row[2]
      }
      products.append(product)

    return json.dumps(products)

  except Exception as e:
    print(f"Error: {e}")
    return json.dumps({"error": "Ocurrió un error al obtener los productos"})
  finally:
    if connection:
      connection.close()