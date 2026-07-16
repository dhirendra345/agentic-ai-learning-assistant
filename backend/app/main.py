import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from services.document_loader import DocumentLoader

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")
)

pdf_path = os.path.join(
    BASE_DIR,
    "data",
    "uploads",
    "sample.pdf"
)

print("PDF Path:", pdf_path)

pdf_text = DocumentLoader.read_pdf(pdf_path)

print(pdf_text[:1000])