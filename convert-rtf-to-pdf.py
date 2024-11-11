import pypandoc
from PyPDF2 import PdfReader, PdfWriter
from datetime import datetime

def convert_rtf_to_pdf_with_metadata(input_file, output_pdf, title, author):
    
    # Convert RTF or RTFD file to PDF using weasyprint as the PDF engine
    pypandoc.convert_file(input_file, 'pdf', outputfile=output_pdf, extra_args=['--pdf-engine=weasyprint'])
    
    # Read the PDF and add metadata
    reader = PdfReader(output_pdf)
    writer = PdfWriter()
    
    # Copy all pages to the writer
    for page in reader.pages:
        writer.add_page(page)
    
    # Set metadata
    writer.add_metadata({
        '/Title': title,
        '/Author': author,
        '/CreationDate': datetime.now().strftime("D:%Y%m%d%H%M%S")
    })
    
    # Write out the modified PDF with metadata
    with open(output_pdf, 'wb') as file:
        writer.write(file)
    
    print(f"PDF created and metadata added: {output_pdf}")

# Get user inputs
input_file = input("Enter the RTF or RTFD file path: ")
output_pdf = input("Enter the output PDF file path (e.g., output.pdf): ")
title = input("Enter the title: ")
author = input("Enter the author: ")

# Convert and add metadata
convert_rtf_to_pdf_with_metadata(input_file, output_pdf, title, author)
