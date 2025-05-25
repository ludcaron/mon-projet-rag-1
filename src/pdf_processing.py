from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    text = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text

def get_pdf_metadata(pdf_path):
    """Get metadata from a PDF file."""
    metadata = {}
    try:
        with open(pdf_path, "rb") as file:
            reader = PdfReader(file)
            metadata = reader.metadata
    except Exception as e:
        print(f"Error reading metadata from {pdf_path}: {e}")
    return metadata