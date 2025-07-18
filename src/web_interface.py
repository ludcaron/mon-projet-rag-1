from flask import Flask, render_template, request
from pdf_processing import extract_text_from_pdf

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file and file.filename.endswith('.pdf'):
        text = extract_text_from_pdf(file)
        return render_template('index.html', extracted_text=text)
    return 'Invalid file type', 400

if __name__ == '__main__':
    app.run(debug=True)