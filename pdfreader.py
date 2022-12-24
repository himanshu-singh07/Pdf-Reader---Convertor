import PyPDF2
import pyttsx3
from tkinter.filedialog import*
# from PyPDF2 import PdfFileReader

book = askopenfilename()
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print('total pages is this pdf is :-\t',pages)

for num in range(0, pages):

    page = pdfreader.getPage(num)

    text = page.extractText()

    player = pyttsx3.init()
    
    player.say(text)

    player.runAndWait()
