import PyPDF2
import pyttsx3
from tkinter.filedialog import*


from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

pdf.set_font("Arial", size = 15)

file = open("a+.txt","r")

for x in file:
	pdf.cell(200, 10, txt = x, ln = 1, align = 'C')

pdf.output("a++.pdf")


file.close()




