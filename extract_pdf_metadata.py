from PyPDF2 import PdfReader

def extract_pdf_metadata(input_path):
    pdf = PdfReader(input_path)
    metadata = pdf.metadata
    return metadata

if __name__ == "__main__":
    input_path = 'input.pdf'
    metadata = extract_pdf_metadata(input_path)
    print(metadata)
