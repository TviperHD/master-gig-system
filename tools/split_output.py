
import os

os.makedirs("Delivery", exist_ok=True)

with open("ai_output.txt", "r", encoding="utf-8") as f:
    content = f.read()

sections = {
    "Section 1:": "section1.txt",
    "Section 2:": "section2.txt",
    "Section 3:": "section3.txt",
    "Section 4:": "section4.txt",
}

for title, filename in sections.items():
    if title in content:
        section_data = content.split(title)[1].split("Section")[0].strip()
        with open(f"Delivery/{filename}", "w", encoding="utf-8") as f:
            f.write(section_data)
