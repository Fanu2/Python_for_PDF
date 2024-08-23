from PyPDF2 import PdfReader, PdfWriter

def rotate_pdf_pages(input_path, output_path, rotation_degree):
    pdf_reader = PdfReader(input_path)
    pdf_writer = PdfWriter()

    for page in pdf_reader.pages:
        page.rotate_clockwise(rotation_degree)
        pdf_writer.add_page(page)

    with open(output_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

if __name__ == "__main__":
    input_path = 'input.pdf'
    output_path = 'rotated.pdf'
    rotation_degree = 90
    rotate_pdf_pages(input_path, output_path, rotation_degree)
