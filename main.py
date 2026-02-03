from src.parser import read_job_description, read_resumes
from src.preprocess import clean_text
from src.matcher import rank_resumes, top_match_keywords


def main():
    job_clean = clean_text(read_job_description())
    raw_resumes = read_resumes()
    clean_resumes = {name: clean_text(text) for name, text in raw_resumes.items()}

    ranked = rank_resumes(job_clean, clean_resumes)

    print("\n--- RESUME MATCH RANKING ---\n")
    if not ranked:
        print("No resumes ranked. Add PDF resumes to data/resumes.")
        return

    for i, (name, score) in enumerate(ranked, start=1):
        print(f"{i}. {name}  |  score: {score:.3f}")

    # Explain the top resume (rank #1)
    top_name, top_score = ranked[0]
    print(f"\n--- WHY THIS MATCHED (#1): {top_name} ---")
    keywords = top_match_keywords(job_clean, clean_resumes[top_name], top_n=12)

    if not keywords:
        print("No overlapping keywords found (or resume text is empty).")
    else:
        for word, strength in keywords:
            print(f"- {word}")


if __name__ == "__main__":
    main()
