# Import the FPDF class and the argparse module
from fpdf import FPDF
import argparse
from PIL import Image


# Create an ArgumentParser object
parser = argparse.ArgumentParser()



# Parse the command line arguments
args = parser.parse_args()

# Create a new PDF object
pdf = FPDF('P', 'mm', (3840, 2160))

# creating a new image file with light blue color with A4 size dimensions using PIL
img = Image.new('RGB', (15000,15000), "#afeafe" )
img.save('pdf_background_color.png')


# Iterate over the number of pages
for i in range(10):

    pdf.add_page()
    pdf.image('pdf_background_color.png', x = 0, y = 0, type = '', link = '')

    # Set the font and size
    pdf.set_font('Arial', 'B', 16)
    # Add page numbering
    pdf.cell(0, 10, 'Page %d' % (i + 1))

# Save the PDF to a file
pdf.output('my_pdf.pdf', 'F')