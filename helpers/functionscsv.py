import csv
from flask import Response
from models.models import Category, Product


def generate_csv_categories():
    categories = Category.query.all()
    categories_dict = []

    for category in categories:
        categories_dict.append(category.to_dict())

    archivo_csv = 'categories.csv'
    encabezado_respuesta = {
        'Content-Disposition': f'attachment; filename={archivo_csv}',
        'Content-Type': 'text/csv'
    }

    with open(archivo_csv, 'w', newline='') as archivo:
        encabezado = categories_dict[0].keys()
        escritor_csv = csv.DictWriter(archivo, fieldnames=encabezado)
        escritor_csv.writeheader()

        for fila in categories_dict:
            escritor_csv.writerow(fila)

    with open(archivo_csv, 'r') as archivo:
        contenido_csv = archivo.read()

    respuesta = Response(
        contenido_csv, headers=encabezado_respuesta, content_type='text/csv')

    return respuesta


def generate_csv_products():
    products = Product.query.all()
    products_dict = []
    for product in products:
        products_dict.append(product.to_dict())

    archivo_csv = 'products.csv'
    encabezado_respuesta = {
        'Content-Disposition': f'attachment; filename={archivo_csv}',
        'Content-Type': 'text/csv'
    }

    with open(archivo_csv, 'w', newline='') as archivo:
        encabezado = products_dict[0].keys()
        escritor_csv = csv.DictWriter(archivo, fieldnames=encabezado)
        escritor_csv.writeheader()

        for fila in products_dict:
            escritor_csv.writerow(fila)

    with open(archivo_csv, 'r') as archivo:
        contenido_csv = archivo.read()

    respuesta = Response(
        contenido_csv, headers=encabezado_respuesta, content_type='text/csv')

    return respuesta
