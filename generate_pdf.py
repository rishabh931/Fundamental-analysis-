from fpdf import FPDF
import os

def create_pdf_report(ticker, results, charts):
    filename = f"{ticker}_report.pdf"
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(190, 10, f"{ticker.upper()} - Minervini Analysis Report", ln=1, align='C')

    pdf.set_font("Arial", size=12)
    for key, value in results.items():
        pdf.cell(190, 10, f"{key}: {value}", ln=1)

    pdf.output(filename)
    return filename
