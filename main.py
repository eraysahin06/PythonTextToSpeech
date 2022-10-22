import pyttsx3
import PyPDF2

story = open("Blog.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(story)

engine = pyttsx3.init()
voices = engine.getProperty('voices')

#voices[1] for a male reader voice.
engine.setProperty('voice', voices[0].id)

for page_no in range(0, pdfReader.numPages):
    page = pdfReader.getPage(page_no)
    text = page.extractText()
    engine.say(text)
    engine.runAndWait()