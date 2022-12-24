print('For readimg Pdf file press 1')

print('for convert Text file to pdf File press 2')

print('convert Img format to Pdf format Press 3')

Press_Key = int(input())

if (Press_Key == 1):

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

    if (Press_Key == 2):

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

        print('PDf made SucessFully')

    if ( Press_Key == 3):

        import img2pdf
        from PIL import Image
        import os

        img_path = "C:\himanshu\clg project\img\h.jpg"


        pdf_path = "C:\himanshu\clg project\img\hss.pdf"

        image = Image.open(img_path)
        image.show()

        pdf_bytes = img2pdf.convert(image.filename)

        file = open(pdf_path, "wb")

        file.write(pdf_bytes)

        image.close()

        file.close()

        print("Successfully made pdf file")

    else:
        print('Invalid Input!')




