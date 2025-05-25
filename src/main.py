from flask import Flask, render_template
from pdf_processing import extract_text_from_pdf

app = Flask(__name__)

@app.route('/')
def index():
    # Process the sample PDF and extract text
    pdf_text = extract_text_from_pdf('data/sample.pdf')
    return render_template('index.html', pdf_text=pdf_text)

if __name__ == '__main__':
    app.run(debug=True)