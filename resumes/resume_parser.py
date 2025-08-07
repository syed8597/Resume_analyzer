import fitz  # PyMuPDF
import re
import spacy
import importlib.util

# Check if model is available, if not, download and install
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")


from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
STOPWORDS = set(stopwords.words("english"))

STOPWORDS = set("""
i me my myself we our ours ourselves you you're you've you'll you'd your yours yourself yourselves he him his himself she she's her hers herself 
it it's its itself they them their theirs themselves what which who whom this that that'll these those am is are was were be been being have has had having do does did doing 
a an the and but if or because as until while of at by for with about against between into through during before after above below to from up down in out on off over under 
again further then once here there when where why how all any both each few more most other some such no nor not only own same so than too very s t can will just don should 
now d ll m o re ve y ain aren aren't couldn couldn't didn didn't doesn doesn't hadn hadn't hasn hasn't haven haven't isn isn't ma mightn mightn't mustn mustn't needn needn't 
shan shan't shouldn shouldn't wasn wasn't weren weren't won won't wouldn wouldn't
""".split())


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
