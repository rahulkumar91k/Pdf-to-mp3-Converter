import pyttsx3
import pdfplumber
import PyPDF2
file = 'D:/projects (all)/pdfto voicetest/PDF.pdf'
f=open(file,'rb')
pdfR = PyPDF2.PdfReader(f)
pages = len(pdfR.pages)
with pdfplumber.open(file) as pdf:
    for i in range (0,pages):
        page = pdf.pages[i]
        text=page.extract_text()
        print(text)
        s=pyttsx3.init()
        s.save_to_file(text,'D:/projects (all)/pdfto voicetest/rahul.mp3')
        s.runAndWait()
f.close()
