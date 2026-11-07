"""
Resume Parser Module
====================
Handles PDF resume upload, validation, and text extraction using PyMuPDF.
"""

import fitz  # PyMuPDF
import os
from typing import Tuple


def validate_pdf(file_path: str) -> Tuple[bool, str]:
    """
    Validate that a file exists and is a valid PDF.

    Args:
        file_path: Path to the file to validate.

    Returns:
        Tuple of (is_valid, message).
    """
    if not os.path.exists(file_path):
        return False, "File not found."

    if not file_path.lower().endswith(".pdf"):
        return False, "Invalid file type. Only PDF files are accepted."

    try:
        doc = fitz.open(file_path)
        if doc.page_count == 0:
            doc.close()
            return False, "The PDF file has no pages."
        doc.close()
        return True, "Valid PDF file."
    except Exception as e:
        return False, f"Could not read PDF: {str(e)}"


def validate_uploaded_file(uploaded_file) -> Tuple[bool, str]:
    """
    Validate a Streamlit UploadedFile object.

    Args:
        uploaded_file: Streamlit UploadedFile object.

    Returns:
        Tuple of (is_valid, message).
    """
    if uploaded_file is None:
        return False, "No file uploaded."

    if not uploaded_file.name.lower().endswith(".pdf"):
        return False, "Invalid file type. Only PDF files are accepted."

    if uploaded_file.size == 0:
        return False, "The uploaded file is empty."

    # 10 MB limit
    if uploaded_file.size > 10 * 1024 * 1024:
        return False, "File size exceeds 10 MB limit."

    return True, "Valid PDF file."


def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract text from a PDF file using PyMuPDF.

    Args:
        file_path: Path to the PDF file.

    Returns:
        Extracted text as a string.

    Raises:
        ValueError: If the file is invalid or empty.
        FileNotFoundError: If the file does not exist.
    """
    is_valid, message = validate_pdf(file_path)
    if not is_valid:
        raise ValueError(message)

    text = ""
    try:
        doc = fitz.open(file_path)
        for page_num in range(doc.page_count):
            page = doc[page_num]
            text += page.get_text("text")
        doc.close()
    except Exception as e:
        raise ValueError(f"Error extracting text from PDF: {str(e)}")

    text = text.strip()
    if not text:
        raise ValueError("No readable text found in the PDF. The file may contain only images.")

    return text


def extract_text_from_bytes(file_bytes: bytes) -> str:
    """
    Extract text from PDF bytes (e.g., from a Streamlit UploadedFile).

    Args:
        file_bytes: Raw bytes of the PDF file.

    Returns:
        Extracted text as a string.

    Raises:
        ValueError: If no text can be extracted.
    """
    if not file_bytes:
        raise ValueError("Empty file content.")

    text = ""
    try:
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        if doc.page_count == 0:
            doc.close()
            raise ValueError("The PDF file has no pages.")

        for page_num in range(doc.page_count):
            page = doc[page_num]
            text += page.get_text("text")
        doc.close()
    except ValueError:
        raise
    except Exception as e:
        raise ValueError(f"Error extracting text from PDF: {str(e)}")

    text = text.strip()
    if not text:
        raise ValueError("No readable text found in the PDF. The file may contain only images.")

    return text
