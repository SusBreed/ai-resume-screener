from src.parser import read_job_description, read_resumes
from src.preprocess import clean_text
from src.matcher import rank_resumes, top_match_keywords


def main():
    print("Program started")

    job_clean = clean_text(read_job_description())

    raw_resumes = read_resumes()
    print("Resumes detected:", list(raw_resumes.keys()))

    if not raw_resumes:
        print("No resumes found. Add PDF files to: data/resumes/")
        return

    clean_resumes = {name: clean_text(text) for name, text in raw_resumes.items()}

    # ✅ THIS WAS MISSING
    ranked = rank_resumes(job_clean, clean_resumes)

    if not ranked:
        print("No ranking produced.")
        return

    print("\n--- RESUME MATCH RANKING ---\n")

    def score_label(percent):
        if percent >= 25:
            return "Strong Match"
        elif percent >= 12:
            return "Medium Match"
        else:
            return "Low Match"

    for i, (name, score) in enumerate(ranked, start=1):
        percent = score * 100
        label = score_label(percent)
        print(f"{i}. {name}  |  {percent:.1f}%  -> {label}")

    top_k = min(3, len(ranked))
    print(f"\n--- WHY THESE MATCHED (Top {top_k}) ---")

    for idx in range(top_k):
        name, score = ranked[idx]
        percent = score * 100
        label = score_label(percent)

        print(f"\n#{idx+1}: {name}  |  {percent:.1f}% -> {label}")
        keywords = top_match_keywords(job_clean, clean_resumes[name], top_n=10)

        for word, _ in keywords:
            print(f"  - {word}")

if __name__ == "__main__":
    main()
