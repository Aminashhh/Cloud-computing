
import pypdf
import os

files = [
    "Presentation.pdf",
    "hsbkp_2023_eng.pdf",
    "Sustainability-report-2024.pdf"
]

def extract_text(pdf_path, output_path):
    print(f"Processing {pdf_path}...")
    try:
        reader = pypdf.PdfReader(pdf_path)
        with open(output_path, 'w', encoding='utf-8') as f:
            for page_num, page in enumerate(reader.pages):
                f.write(f"--- Page {page_num + 1} ---\n")
                f.write(page.extract_text())
                f.write("\n\n")
        print(f"Saved to {output_path}")
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")

for file in files:
    output = "extracted_" + file.replace(".pdf", ".txt")
    extract_text(file, output)
