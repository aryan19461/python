from pypdf import PdfMerger

merge = PdfMerger()
pdf_files = [
    "1.pdf", 
    "2.pdf", 
    "3.pdf"
    ]

for pdf in pdf_files:
    merge.append(pdf)

merge.write("python_merged.pdf")
merge.close()