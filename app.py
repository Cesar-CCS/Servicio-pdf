import logging
from flask import Flask, Response, jsonify
from database.database import db
from config import BasicConfig
from models.models import Product, Category
from helpers.functionscsv import generate_csv_categories, generate_csv_products
from helpers.pdf_generator import pdf_generate
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app=app)
app.config.from_object(BasicConfig)
db.init_app(app)


@cross_origin
@app.route('/categories')
def csv_categories():
    return generate_csv_categories()


@cross_origin
@app.route('/products')
def csv_products():
    return generate_csv_products()


@cross_origin
@app.route("/products-pdf")
def products_pdf():
    try:
        columns = ["id", "name", "description", "price",]
        products = Product.query.all()
        w = 40
        results = pdf_generate("Productos", columns, products, w,)
        response = jsonify({"ok": True, "results":  results})
        response.headers['Content-Type'] = 'application/json'
        return response
    except Exception as e:
        return jsonify({"ok": False, "error": e})


@cross_origin
@app.route("/categories-pdf")
def categories_pdf():
    try:
        columns = ["id", "name", "description"]
        categories = Category.query.all()
        w = 60
        results = pdf_generate("Categorias", columns, categories, w)
        response = jsonify({"ok": True, "results": results})
        response.headers['Content-Type'] = 'application/json'
        return response
    except Exception as e:
        return jsonify({"ok": False, "error": e})


logging.basicConfig(level=logging.DEBUG, filename='data_layer.log')
