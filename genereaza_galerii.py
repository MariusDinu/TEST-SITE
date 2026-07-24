from pathlib import Path

ROOT = Path("proiecte")      # folderul cu pozele
OUTPUT = "galerii.txt"

EXT = {".jpg", ".jpeg", ".png", ".webp", ".gif"}

with open(OUTPUT, "w", encoding="utf-8") as out:

    for folder in sorted(ROOT.rglob("*")):
        if not folder.is_dir():
            continue

        rel = folder.relative_to(ROOT).as_posix()

        # pentru folderul radacina nu scriem sectiune
        if rel == ".":
            continue

        out.write(f"[{rel}]\n")

        imagini = sorted(
            [f for f in folder.iterdir()
             if f.is_file() and f.suffix.lower() in EXT],
            key=lambda x: x.name.lower()
        )

        for img in imagini:
            out.write(img.as_posix() + "\n")

        out.write("\n")

print("galerii.txt generat.")