from flask import Flask, make_response
from pdf_generator import generar_pdf
from Venta import Venta

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
    pdf_output = generar_pdf(ventas)
    
    # Crear una respuesta para el cliente
    response = make_response(pdf_output)
    response.headers['Content-Disposition'] = 'inline'#f'attachment; filename={pdf_output}'
    response.headers['Content-type'] = 'application/pdf'

    return response

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)