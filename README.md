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

## 📊 Example Output

When testing multiple resumes against the same job description, the system ranks candidates based on relevance.

Example run:

--- RESUME MATCH RANKING ---

Alex Johnson.pdf | 31.5% -> Strong Match

Miguel_Pacheco_Outlier_Resume.pdf | 5.9% -> Low Match

--- WHY THESE MATCHED (Top 2) ---

#1: Alex Johnson.pdf | 31.5% -> Strong Match

- data
- machine
- learning
- analysis
- python

#2: Miguel_Pacheco_Outlier_Resume.pdf | 5.9% -> Low Match

- experience
- data
- learning
- machine

This demonstrates that resumes closely aligned with the job description score significantly higher than more generic resumes.