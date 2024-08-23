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
