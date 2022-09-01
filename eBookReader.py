import pyttsx3
import PyPDF2
eBook = open('dee.pdf', 'de')
pdfReader = PyPDF2.PdfFileReader(eBook)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(68, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
