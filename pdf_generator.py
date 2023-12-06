from fpdf import FPDF
import base64
import tempfile

def generar_pdf(ventas):
    if not ventas:
        print("No hay ventas para generar el PDF.")
        return "No hay ventas para generar el PDF."

    # Tomar la fecha de la primera venta en la colección
    fecha = ventas[0].fecha

    # Crear un objeto PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Título del reporte
    pdf.cell(0, 10, txt=f"Reporte de Ventas {fecha}", ln=True, align='C')
    pdf.ln(10)  # Salto de línea

    # Encabezados de la tabla
    pdf.cell(40, 10, "ID Venta", 1)
    pdf.cell(80, 10, "Usuario", 1)
    pdf.cell(60, 10, "Total Venta", 1)
    pdf.ln()

    # Agregar contenido al PDF
    total_ventas_dia = 0  # Variable para almacenar la suma de las ventas
    for venta in ventas:
        pdf.cell(40, 10, str(venta.id_venta), 1)
        pdf.cell(80, 10, venta.usuario, 1)
        pdf.cell(60, 10, str(venta.total_venta), 1)
        pdf.ln()
        
        # Sumar el total de ventas
        total_ventas_dia += venta.total_venta

    # Fila adicional al final de la tabla
    pdf.cell(40, 10, "", 1)  # Celda vacía para la columna ID Venta
    pdf.cell(80, 10, "Total Ventas del Día:", 1)
    pdf.cell(60, 10, str(total_ventas_dia), 1)
    pdf.ln()

    # Guardar el PDF en un archivo
    # '''pdf_output = f"ventas_{fecha}.pdf"
    # pdf.output(pdf_output)

    # print(f"PDF generado exitosamente: {pdf_output}")'''

    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        pdf.output(temp_file.name)

    # Leer el contenido del archivo temporal
    with open(temp_file.name, 'rb') as pdf_file:
        # Codificar el contenido del PDF a Base64
        base64_pdf = base64.b64encode(pdf_file.read()).decode('utf-8')

    return base64_pdf