# Packages to include
''' pip install pdfcrowd, pip install pdfkit '''


import pdfkit 

# Locally saved HTML
pdfkit.from_file('my_test.html', my_'output.pdf')

# From Website
pdfkit.from_url('https://www.google.co.in/','my_testpdf.pdf')

# Store Text (HTML String) in PDF
pdfkit.from_string('my_testpdf ABC','testpdf.pdf')