import sys
import os

pdf_path = "/Users/ali/Documents/git/the most ai shit youve ever seen/research/sources/Does AI Foster imposter feelings_ The impact of task design on students’ use of AI _ Education and Information Technologies _ Springer Nature Link.pdf"
output_path = "/Users/ali/Documents/git/the most ai shit youve ever seen/research/extracted/extracted_text.txt"

print(f"Checking libraries to extract text from: {pdf_path}")

try:
    import pypdf
    print("Using pypdf")
    reader = pypdf.PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n\n"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Success! Extracted text written to extracted_text.txt")
    sys.exit(0)
except ImportError:
    pass

try:
    import PyPDF2
    print("Using PyPDF2")
    reader = PyPDF2.PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n\n"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Success! Extracted text written to extracted_text.txt")
    sys.exit(0)
except ImportError:
    pass

try:
    import pdfplumber
    print("Using pdfplumber")
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n\n"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Success! Extracted text written to extracted_text.txt")
    sys.exit(0)
except ImportError:
    pass

print("No PDF extraction libraries found (tried pypdf, PyPDF2, pdfplumber). Trying pdftotext tool...")
res = os.system(f'pdftotext "{pdf_path}" "{output_path}"')
if res == 0:
    print("Success using pdftotext command!")
    sys.exit(0)

print("Failed to find any PDF extraction tool. Please install pypdf via pip.")
sys.exit(1)
