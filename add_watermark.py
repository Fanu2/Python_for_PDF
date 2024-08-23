from PyPDF2 import PdfReader, PdfWriter

def add_watermark(input_pdf, watermark_pdf, output_pdf):
    pdf_reader = PdfReader(input_pdf)
    watermark_reader = PdfReader(watermark_pdf)
    pdf_writer = PdfWriter()
    watermark_page = watermark_reader.pages[0]

    for page in pdf_reader.pages:
        page.merge_page(watermark_page)
        pdf_writer.add_page(page)

    with open(output_pdf, 'wb') as output_file:
        pdf_writer.write(output_file)

if __name__ == "__main__":
    input_pdf = 'input.pdf'
    watermark_pdf = 'watermark.pdf'
    output_pdf = 'watermarked.pdf'
    add_watermark(input_pdf, watermark_pdf, output_pdf)
