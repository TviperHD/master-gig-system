
from fpdf import FPDF

with open("Delivery/summary.txt", "r", encoding="utf-8") as file:
    text = file.read()

pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=12)

for line in text.split('\n'):
    pdf.multi_cell(0, 10, line)

pdf.output("Delivery/summary.pdf")
print("PDF created as Delivery/summary.pdf")
