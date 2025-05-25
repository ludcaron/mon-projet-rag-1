def extract_text_from_pdf(pdf_path):
    from PyPDF2 import PdfReader

    text = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    
    return text

def format_data(data):
    # Example function to format data for display
    return "\n".join(str(item) for item in data)

def validate_input(data):
    # Example function to validate input data
    return isinstance(data, str) and len(data) > 0