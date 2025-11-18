# This file is intentionally left blank.from fpdf import FPDF
from fpdf import FPDF
def create_simple_pdf(text, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)
    pdf.output(filename)
create_simple_pdf("Hello, this is a PDF!", "output.pdf")