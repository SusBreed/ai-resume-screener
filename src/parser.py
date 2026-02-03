from pathlib import Path
import pdfplumber


def _project_root() -> Path:
    # project root = folder containing "src"
    return Path(__file__).resolve().parents[1]


def read_job_description() -> str:
    file_path = _project_root() / "data" / "job_description.txt"
    if not file_path.exists():
        raise FileNotFoundError(f"Job description file not found at: {file_path}")
    return file_path.read_text(encoding="utf-8").strip()


def read_resumes() -> dict[str, str]:
    folder_path = _project_root() / "data" / "resumes"
    if not folder_path.exists():
        return {}

    resume_texts: dict[str, str] = {}

    for file in folder_path.iterdir():
        if file.is_file() and file.suffix.lower() == ".pdf":
            with pdfplumber.open(file) as pdf:
                text = ""
                for page in pdf.pages:
                    text += page.extract_text() or ""
            resume_texts[file.name] = text.strip()

    return resume_texts

