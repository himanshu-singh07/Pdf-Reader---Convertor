import img2pdf
from PIL import Image
import os
import pyttsx3
import PyPDF2
from tkinter.filedialog import*

img_path = "C:\himanshu\clg project\img\h.jpg"


pdf_path = "C:\himanshu\clg project\img\hss.pdf"

image = Image.open(img_path)
image.show()

# converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(image.filename)

# opening or creating pdf file
file = open(pdf_path, "wb")

# writing pdf files with chunks
file.write(pdf_bytes)




# closing image file
image.close()

# closing pdf file
file.close()

# output
print("Successfully made pdf file")

pdf_img = askopenfilename()

