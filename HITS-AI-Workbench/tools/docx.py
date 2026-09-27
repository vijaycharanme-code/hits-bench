from docx import Document

def extract_text(file_path: str) -> str:
    try:
        doc = Document(file_path)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
        return '\n'.join(fullText)
    except Exception as e:
        return f"Error extracting DOCX: {e}"
