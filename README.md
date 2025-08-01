# 📚 Python for PDF

A collection of Python scripts to perform various PDF operations using popular libraries like `PyPDF2`, `reportlab`, or `fpdf`. This toolkit is ideal for automating everyday PDF-related tasks such as merging, splitting, extracting text, filling forms, and more.

## 📂 Features & Scripts

| Script Name                | Description                                                       |
| -------------------------- | ----------------------------------------------------------------- |
| `main.py`                  | Launcher or index script to test or call other modules.           |
| `create_pdf_with_text.py`  | Generate a PDF with custom text content.                          |
| `extract_pdf_metadata.py`  | Extract metadata such as author, title, subject, etc. from a PDF. |
| `extract_text_from_pdf.py` | Extract raw text from the contents of a PDF.                      |
| `fill_pdf_form.py`         | Fill out form fields in a fillable PDF.                           |
| `merge_pdfs.py`            | Merge multiple PDFs into a single file.                           |
| `merge_pdfs_range.py`      | Merge specific page ranges from multiple PDFs.                    |
| `remove_pages_from_pdf.py` | Delete specific pages from a PDF document.                        |
| `rotate_pdf_pages.py`      | Rotate individual or multiple pages within a PDF.                 |
| `split_pdf.py`             | Split a PDF into separate files per page or range.                |
| `_watermark.py`            | Add watermark text or images to existing PDF files.               |

## 💠 Requirements

Install the required Python packages:

```bash
pip install PyPDF2 reportlab
```

Other libraries you may consider (depending on scripts):

```bash
pip install fpdf pdfplumber pdfrw
```

## 🚀 Usage

Each script can be run independently from the command line. Example:

```bash
python merge_pdfs.py
```

Or customize and import specific modules into your own apps.

## 💡 Use Cases

* 📄 Combine multiple invoices into one PDF
* ✂️ Split chapters from an e-book
* 🔋 Auto-fill client forms
* 📟 Stamp reports with custom watermarks
* 🔍 Scrape text for data analysis

## 📌 Notes

* These are CLI-based utilities meant for developers and technical users.
* Input/output file paths may be hardcoded—update as needed.

## 📁 Directory Structure

```
Python_for_PDF/
│
├── _watermark.py
├── create_pdf_with_text.py
├── extract_pdf_metadata.py
├── extract_text_from_pdf.py
├── fill_pdf_form.py
├── main.py
├── merge_pdfs.py
├── merge_pdfs_range.py
├── remove_pages_from_pdf.py
├── rotate_pdf_pages.py
└── split_pdf.py
```

## 📜 License

MIT License

## ✨ Contributions

Pull requests are welcome! If you find a bug or have suggestions for improvement, feel free to open an issue.
