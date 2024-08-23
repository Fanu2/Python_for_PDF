import os

# Path to save the scripts
base_path = '/home/jasvir/PycharmProjects/PDF/'

# List of scripts with filenames and their content
scripts = {
    'merge_pdfs.py': '''\
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_path):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()

if __name__ == "__main__":
    pdf_list = ['file1.pdf', 'file2.pdf']
    output_path = 'merged.pdf'
    merge_pdfs(pdf_list, output_path)
''',

    'split_pdf.py': '''\
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
''',

    'extract_text_from_pdf.py': '''\
from PyPDF2 import PdfReader

def extract_text_from_pdf(input_path):
    pdf = PdfReader(input_path)
    text = ''
    for page in pdf.pages:
        text += page.extract_text()
    return text

if __name__ == "__main__":
    input_path = 'input.pdf'
    text = extract_text_from_pdf(input_path)
    print(text)
''',

    'add_watermark.py': '''\
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
''',

    'rotate_pdf_pages.py': '''\
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
''',

    'merge_pdfs_range.py': '''\
from PyPDF2 import PdfMerger

def merge_pdfs_with_range(pdf_list, page_ranges, output_path):
    merger = PdfMerger()
    for pdf, pages in zip(pdf_list, page_ranges):
        merger.append(pdf, pages=pages)
    merger.write(output_path)
    merger.close()

if __name__ == "__main__":
    pdf_list = ['file1.pdf', 'file2.pdf']
    page_ranges = [(0, 2), (1, 3)]  # Specify page ranges to merge from each PDF
    output_path = 'merged_with_range.pdf'
    merge_pdfs_with_range(pdf_list, page_ranges, output_path)
''',

    'create_pdf_with_text.py': '''\
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
''',

    'extract_pdf_metadata.py': '''\
from PyPDF2 import PdfReader

def extract_pdf_metadata(input_path):
    pdf = PdfReader(input_path)
    metadata = pdf.metadata
    return metadata

if __name__ == "__main__":
    input_path = 'input.pdf'
    metadata = extract_pdf_metadata(input_path)
    print(metadata)
''',

    'fill_pdf_form.py': '''\
from pdfrw import PdfReader, PdfWriter, PageMerge

def fill_pdf_form(template_path, output_path, data):
    template_pdf = PdfReader(template_path)
    output_pdf = PdfWriter()

    for page in template_pdf.pages:
        page_merge = PageMerge(page)
        page_merge.add(PageMerge().add(data, prepend=True))
        output_pdf.addpage(page)

    output_pdf.write(output_path)

if __name__ == "__main__":
    template_path = 'template.pdf'
    output_path = 'filled_form.pdf'
    data = {'field_name': 'value'}  # Example data
    fill_pdf_form(template_path, output_path, data)
''',

    'remove_pages_from_pdf.py': '''\
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
'''
}

# Ensure the directory exists
os.makedirs(base_path, exist_ok=True)

# Create and write each script file
for filename, content in scripts.items():
    file_path = os.path.join(base_path, filename)
    with open(file_path, 'w') as file:
        file.write(content)

print("Scripts have been created in", base_path)
