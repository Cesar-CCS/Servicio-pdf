import io
import csv
import base64
from flask import Response
from models.models import Category, Product


def generate_csv_categories():
    categories = Category.query.all()
    categories_dict = []

    for category in categories:
        categories_dict.append(category.to_dict())

    csv_buffer = io.StringIO()
    csv_writer = csv.writer(csv_buffer)

    csv_writer.writerow(["id", "name", "description"])

    for item in categories_dict:
        csv_writer.writerow(
            [item["id"], item["name"], item["description"]])

    csv_content = csv_buffer.getvalue()

    csv_base64 = base64.b64encode(csv_content.encode()).decode()

    response = {
        "ok": True,
        "csv_base64": csv_base64
    }

    return response

    # archivo_csv = 'categories.csv'
    # encabezado_respuesta = {
    #     'Content-Disposition': f'attachment; filename={archivo_csv}',
    #     'Content-Type': 'text/csv'
    # }

    # with open(archivo_csv, 'w', newline='') as archivo:
    #     encabezado = categories_dict[0].keys()
    #     escritor_csv = csv.DictWriter(archivo, fieldnames=encabezado)
    #     escritor_csv.writeheader()

    #     for fila in categories_dict:
    #         escritor_csv.writerow(fila)

    # with open(archivo_csv, 'r') as archivo:
    #     contenido_csv = archivo.read()

    # respuesta = Response(
    #     contenido_csv, headers=encabezado_respuesta, content_type='text/csv')

    # return respuesta


def generate_csv_products():
    products = Product.query.all()
    products_dict = []
    for product in products:
        products_dict.append(product.to_dict())

    csv_buffer = io.StringIO()
    csv_writer = csv.writer(csv_buffer)

    csv_writer.writerow(["id", "name", "description", "price"])

    for item in products_dict:
        csv_writer.writerow(
            [item["id"], item["name"], item["description"], item["price"]])

    csv_content = csv_buffer.getvalue()

    csv_base64 = base64.b64encode(csv_content.encode()).decode()

    response = {
        "ok": True,
        "csv_base64": csv_base64
    }

    return response

    # encabezado_respuesta = {
    #     'Content-Disposition': f'attachment; filename={archivo_csv}',
    #     'Content-Type': 'text/csv'
    # }

    # with open(archivo_csv, 'w', newline='') as archivo:
    #     encabezado = products_dict[0].keys()
    #     escritor_csv = csv.DictWriter(archivo, fieldnames=encabezado)
    #     escritor_csv.writeheader()

    #     for fila in products_dict:
    #         escritor_csv.writerow(fila)

    # with open(archivo_csv, 'r') as archivo:
    #     contenido_csv = archivo.read()

    # respuesta = Response(
    #     contenido_csv, headers=encabezado_respuesta, content_type='text/csv')

    # return response
