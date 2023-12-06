from fpdf import FPDF
import base64
import tempfile


def pdf_generate(name, columns, data, w):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)

    pdf.cell(0, 10, txt=f"Reporte de {name}", ln=True, align='C')
    pdf.ln(10)

    width_celda = w
    height_celda = 10

    for column in columns:
        pdf.cell(width_celda, height_celda, column, border=1)
    pdf.ln()

    for row in data:
        for column in columns:
            pdf.cell(width_celda, height_celda, str(
                getattr(row, column)), border=1)
        pdf.ln()

    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        pdf.output(temp_file.name)
    with open(temp_file.name, 'rb') as pdf_file:
        base64_pdf = base64.b64encode(pdf_file.read()).decode('utf-8')

    return base64_pdf
