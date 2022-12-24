import img2pdf
from PIL import Image
import os
import pyttsx3
import PyPDF2
from tkinter.filedialog import*

img_path = askopenfilename()


pdf_path = "C:\himanshu\clg project\img\hss.pdf"

image = Image.open(img_path)
image.show()

# converting into chunks using img2pdf