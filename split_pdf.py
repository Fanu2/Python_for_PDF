from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_path, output_folder):
    pdf = PdfReader(input_path)
    for page_num in range(len(pdf.pages)):
        pdf_writer = PdfWriter()
        pdf_writer.add_page(pdf.pages[page_num])
        output_path = f"{output_folder}/page_{page_num + 1}.pdf"
        with open(output_path, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

if __name__ == "__main__":
    input_path = 'input.pdf'
    output_folder = 'output'
    split_pdf(input_path, output_folder)
