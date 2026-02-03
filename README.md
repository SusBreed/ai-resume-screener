# AI Resume Screener (Python + NLP)

This project ranks PDF resumes against a job description using NLP.

## Features
- Reads a job description from `data/job_description.txt`
- Extracts text from PDF resumes in `data/resumes/`
- Cleans and normalizes text (stopwords removal, punctuation cleanup)
- Converts documents to TF-IDF vectors
- Ranks resumes using cosine similarity
- Explains the top match with contributing keywords

## Tech Stack
- Python
- pdfplumber (PDF text extraction)
- NLTK (stopwords)
- scikit-learn (TF-IDF + similarity)

## How to Run
1. Create and activate a virtual environment
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
