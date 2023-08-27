from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)  # the order of the parameters is red, green, blue
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(x1=10, y1=21, x2=200, y2=21)

    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=12)
    pdf.set_text_color(180, 180, 180)  # the order of the parameters is red, green, blue
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1)

    for pages in range(row["Pages"] - 1):
        pdf.add_page()

        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=12)
        pdf.set_text_color(180, 180, 180)  # the order of the parameters is red, green, blue
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1)

pdf.output("output.pdf")
