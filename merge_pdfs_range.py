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
