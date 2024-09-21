from fpdf import FPDF
from PIL import Image

pdf = FPDF(orientation = "Portrait", format ="A4")
pdf.add_page()
pdf.image("shirtificate.png", x=10, y=60, w = 190, h = 200)
pdf.set_font("helvetica", "B", 40)
pdf.cell(0, 50, "CS50 Shirtificate", 0, 0, "C")
pdf.set_font("helvetica", "", 25)
pdf.set_text_color(255,255,255)
pdf.cell(-180, 250, "John Harvard took CS50", 0, 0, "C", fill=False)
pdf.output("shirtificate.pdf")
