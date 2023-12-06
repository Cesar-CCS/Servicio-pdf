from flask import Flask, make_response
from pdf_generator import generar_pdf
from Venta import Venta
import base64

app = Flask(__name__)

# Lista de ventas (simulación de una base de datos)
ventas = []

# Agregar 5 ventas para la misma fecha (simulación)
for i in range(1, 6):
    venta = Venta(id_venta=i, fecha="2023-11-21", total_venta=100.0 * i, usuario=f"Usuario{i}")
    ventas.append(venta)

@app.route('/')
def index():
    return f'{ventas[0]}'

@app.route('/generar_pdf')
def generar_pdf_route():
    resp = generar_pdf(ventas)
    response = {"ok":True, "results":resp}
    return response

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)