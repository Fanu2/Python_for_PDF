from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf_with_text(output_path, text):
    c = canvas.Canvas(output_path, pagesize=letter)
    c.drawString(100, 750, text)
    c.save()

if __name__ == "__main__":
    output_path = 'text.pdf'
    text = 'Hello, this is a PDF with text!'
    create_pdf_with_text(output_path, text)
