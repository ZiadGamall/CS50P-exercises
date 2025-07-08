from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("Arial", size=20)
pdf.cell(70, 10, "CS50 Shirtificate", 0, align="C")
pdf.add_page()
pdf.output("shirtificate.pdf")