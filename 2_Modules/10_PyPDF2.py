#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# In this tutorial we will be working with PyPDF2 module module
# ===================================================================================================
# ______________________ PyPDF2 module ______________________
# --pypdf extracts the information as a string
# --first page in pypdf is the 0 page
# --you can not directly edit the pdf
# --instead you need to open the pdf, extract content, fix things, and create new prd using that content
# --you can not insert pages in the middle, you can only add page at the end
# ===================================================================================================

# opening and reading pdf file
import PyPDF2
pdf_object = open('./1_working_files/meetingminutes.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_object)
print('Number of pages: ', pdf_reader.numPages)
page0 = pdf_reader.getPage(0)
print(page0.extractText())

# opening and reading encrypted pdf file
pdf_reader = PyPDF2.PdfFileReader(open('./1_working_files/encrypted.pdf', 'rb'))
print(pdf_reader.isEncrypted)
pdf_reader.decrypt('rosebud')
page0 = pdf_reader.getPage(1)

# let's use pypdf to copy pages from one pdf to the other
pdf_file1 = open('./1_working_files/meetingminutes.pdf', 'rb')
pdf_file2 = open('./1_working_files/meetingminutes2.pdf', 'rb')
pdf_obj1 = PyPDF2.PdfFileReader(pdf_file1)
pdf_obj2 = PyPDF2.PdfFileReader(pdf_file2)
combined_pdf = PyPDF2.PdfFileWriter()

for i in range(0, pdf_obj1.numPages):
    combined_pdf.addPage(pdf_obj1.getPage(i))

for i in range(0, pdf_obj2.numPages):
    combined_pdf.addPage(pdf_obj2.getPage(i))

output_file = open('./1_working_files/combinedpdf.pdf', 'wb')
combined_pdf.write(output_file)
output_file.close()
pdf_file1.close()
pdf_file2.close()

# let's rotate the pages in the pdf combined pdf
pdf_file1 = open('./1_working_files/combinedpdf.pdf', 'rb')
pdf_obj = PyPDF2.PdfFileReader(pdf_file1)
rotated_pdf = PyPDF2.PdfFileWriter()

for i in range(0, pdf_obj.numPages):
    page = pdf_obj.getPage(i)
    page.rotateClockwise(90)
    rotated_pdf.addPage(page)

with open('./1_working_files/combinedpdf_rotated.pdf', 'wb') as object_:
    rotated_pdf.write(object_)

# you can also overlay pages with PyPDF2
pdf_file = open('./1_working_files/meetingminutes.pdf', 'rb')
pdf_watermark = open('./1_working_files/watermark.pdf', 'rb')
pdf_obj = PyPDF2.PdfFileReader(pdf_file)
wm_obj = PyPDF2.PdfFileReader(pdf_watermark)
writer = PyPDF2.PdfFileWriter()

page = pdf_obj.getPage(0)
page_wm = wm_obj.getPage(0)
page.mergePage(page_wm)

writer.addPage(page)
with open('./1_working_files/watermarked.pdf', 'wb') as object_:
    writer.write(object_)

# encrypting pdfs
# before writing writer to the file, use writer.encrypt('key')
# then write to the file as normal


