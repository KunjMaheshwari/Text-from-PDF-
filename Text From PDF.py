import PyPDF2
a = PyPDF2.PdfFileReader('Programming.pdf')

str = ""
for i in range(1, 11):
    str += a.getPage(i).extraxtText()

with open('Progamming.txt', 'w') as f:
    f.write(str)
