from PyPDF2 import PdfReader, PdfWriter

def remove_pages_from_pdf(input_path, output_path, pages_to_remove):
    pdf_reader = PdfReader(input_path)
    pdf_writer = PdfWriter()

    for page_num in range(len(pdf_reader.pages)):
        if page_num not in pages_to_remove:
            pdf_writer.add_page(pdf_reader.pages[page_num])

    with open(output_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

if __name__ == "__main__":
    input_path = 'input.pdf'
    output_path = 'without_pages.pdf'
    pages_to_remove = [0, 2]  # Remove the first and third pages
    remove_pages_from_pdf(input_path, output_path, pages_to_remove)
