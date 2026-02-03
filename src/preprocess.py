import re
import nltk
from nltk.corpus import stopwords


def _ensure_stopwords():
    try:
        stopwords.words("english")
    except LookupError:
        nltk.download("stopwords")


_ensure_stopwords()
STOP_WORDS = set(stopwords.words("english"))


def clean_text(text: str) -> str:
    text = (text or "").lower()
    text = re.sub(r"[^a-z\s]", " ", text)   # keep letters/spaces
    text = re.sub(r"\s+", " ", text).strip()  # normalize whitespace
    words = [w for w in text.split() if w not in STOP_WORDS]
    return " ".join(words)