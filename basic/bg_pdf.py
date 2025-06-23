"""
pip install PyPDF2

import PyPDF2
f=open('example.pdf','rb')  # read binary like image
pdf_reader=PyPDF.PdfFileReader(f)
pdf_reader.numPages
#5

page_one=pdf_reader.getPage(0)
page_one_text=page_one.extractTest()
page_one_text
# all the page data are displayed

f.close


#write to pdf page
# no update but appending to new page

f=open('example.pdf')
pdf_reader=PyPDF2.PdfFileReader(f)
first_page=pdf_reader.getPage(0)

pdf_write=PyPDF2.PdfFileWrite()
pdf_write.addPage(first_page)
pdf_output=open('new.pdf','wd')
pdf_writer.write(pdf_output)
f.close()
pdf_output.close()


## Get all data of pdf in text

f=open('example.pdf','rb')
pdf_text[]
pdf_reader=PyPDF2.PdfFileReader(f)

for num in range(v.numPages):
    page=pdf_read.getPage(num)
    pdf_text.append(page.extractTest())

"""