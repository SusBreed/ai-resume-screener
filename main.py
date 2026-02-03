from src.parser import read_job_description, read_resumes
from src.preprocess import clean_text
from src.matcher import rank_resumes, top_match_keywords


def main():
    job_clean = clean_text(read_job_description())

    raw_resumes = read_resumes()
    if not raw_resumes:
        print("No resumes found. Add PDF files to: data/resumes/")
        return

    clean_resumes = {name: clean_text(text) for name, text in raw_resumes.items()}

    ranked = rank_resumes(job_clean, clean_resumes)

    raw_resumes = read_resumes()
    if not raw_resumes:
        print("No resumes found.")
        print("Add at least one PDF to: data/resumes/")
        print("Then run: python main.py")
    return

    print("\n--- RESUME MATCH RANKING ---\n")
    for i, (name, score) in enumerate(ranked, start=1):
        print(f"{i}. {name}  |  score: {score:.3f}")

    # Explain the top match
    top_name, top_score = ranked[0]
    print(f"\n--- WHY THIS MATCHED (#1): {top_name} ---")
    keywords = top_match_keywords(job_clean, clean_resumes[top_name], top_n=12)

    if not keywords:
        print("No overlapping keywords found.")
    else:
        for word, _strength in keywords:
            print(f"- {word}")


if __name__ == "__main__":
    main()


