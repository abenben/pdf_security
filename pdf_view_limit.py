import datetime
import PyPDF4


def set_pdf_view_limit(input_pdf_path, output_pdf_path, expiration_date):
    # 入力PDFを読み込む
    with open(input_pdf_path, "rb") as file:
        reader = PyPDF4.PdfFileReader(file)
        writer = PyPDF4.PdfFileWriter()

        # 全ページをコピーする
        for page_num in range(reader.getNumPages()):
            page = reader.getPage(page_num)
            writer.addPage(page)

        # メタデータに閲覧期限を設定
        metadata = {
            "/Creator": "pdf_view_limit_creator",
            "/Subject": f"Expiration Date: {expiration_date.isoformat()}",
        }
        writer.addMetadata(metadata)

        # 変更を加えたPDFを出力する
        with open(output_pdf_path, "wb") as output_file:
            writer.write(output_file)


def check_pdf_view_limit(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF4.PdfFileReader(file)

        # メタデータから閲覧期限を取得
        metadata = reader.getDocumentInfo()
        subject = metadata.get("/Subject")
        expiration_date_str = subject.split("Expiration Date: ")[1]
        expiration_date = datetime.datetime.fromisoformat(expiration_date_str)

        # 現在の日付と期限を比較
        if datetime.datetime.now() > expiration_date:
            print("This PDF has expired. Please contact the document owner for an updated version.")
            return False

    return True


if __name__ == "__main__":
    input_pdf_path = "./input/sample1.pdf"
    output_pdf_path = "./output/sample1_limit.pdf"
    expiration_date = datetime.datetime(2022, 3, 20)

    set_pdf_view_limit(input_pdf_path, output_pdf_path, expiration_date)

    if check_pdf_view_limit(output_pdf_path):
        print("You can still view this PDF.")
    else:
        print("This PDF has expired.")
