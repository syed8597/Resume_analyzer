import fitz  # PyMuPDF
import re
import spacy
from nltk.corpus import stopwords

nlp = spacy.load("en_core_web_sm")
STOPWORDS = set(stopwords.words("english"))

# ✅ Extract raw text from uploaded PDF
def extract_text_from_pdf(file_path):
    text = ""
    doc = fitz.open(file_path)
    for page in doc:
        text += page.get_text()
    return text

# ✅ Extract skills from text using basic keyword matching
def extract_skills(text):
    skill_keywords = [
        "python", "django", "machine learning", "deep learning",
        "nlp", "pandas", "numpy", "data analysis", "html", "css", "git", "sql","data entery","teacher","react","vue","angular","excell","ms office","ms word"
    ]
    text = text.lower()
    found = [skill for skill in skill_keywords if skill in text]
    return list(set(found))

# ✅ Extract years of experience from resume (simple method)
def extract_experience(text):
    matches = re.findall(r'(\d+)\+?\s+years', text.lower())
    if matches:
        return max([int(m) for m in matches])
    return 0
