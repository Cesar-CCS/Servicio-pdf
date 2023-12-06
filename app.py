import logging
from flask import Flask, Response
from database.database import db
from config import BasicConfig
from models.models import Product, Category
from helpers.functionscsv import generate_csv_categories, generate_csv_products
from helpers.pdf_generator import pdf_generate

app = Flask(__name__)

app = Flask(__name__)
app.config.from_object(BasicConfig)
db.init_app(app)


@app.route('/categories')
def csv_categories():
    return generate_csv_categories()


@app.route('/products')
def csv_products():
    return generate_csv_products()


@app.route("/products-pdf")
def products_pdf():
    columns = ["id", "name", "description", "price",]
    products = Product.query.all()
    w = 40
    return pdf_generate("Productos", columns, products, w,)


@app.route("/categories-pdf")
def categories_pdf():
    columns = ["id", "name", "description"]
    categories = Category.query.all()
    w = 60
    return pdf_generate("Categorias", columns, categories, w)


logging.basicConfig(level=logging.DEBUG, filename='data_layer.log')
