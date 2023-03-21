import PyPDF4

with open('./input/sample1.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF4.PdfFileReader(pdf_file)

    pdf_writer = PyPDF4.PdfFileWriter()

    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page)

    owner_pwd = 'password'
    user_pwd = 'password'
    key_length = 128
    use_128bit = True

    pdf_writer.encrypt(user_pwd, owner_pwd, use_128bit, key_length)

    with open('./output/sample1.pdf', 'wb') as output_pdf:
        pdf_writer.write(output_pdf)