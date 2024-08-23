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
