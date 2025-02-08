import os
from PyPDF2 import PdfReader
from docx import Document
from config import Config

class DocumentParser:
    @staticmethod
    def parse_pdf(file_path: str) -> str:
        """Extract text from a PDF File."""
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    
    @staticmethod
    def parse_docx(file_path: str) -> str:
        """Extract text from a DOCX file."""
        doc = Document(file_path)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text
    
    @staticmethod
    def parse_file(file_path: str) -> str:
        """Parse file based on its extension."""
        if file_path.endswith(".pdf"):
            return DocumentParser.parse_pdf(file_path)
        elif file_path.endswith(".docx"):
            return DocumentParser.parse_docx(file_path)
        else:
            raise ValueError("Unsupported file format. Only PDF and DOCX supported.")