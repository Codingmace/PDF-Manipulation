import os
import img2pdf
with open("output.pdf", "wb") as f:
    f.write(img2pdf.convert([i for i in os.listdir('.') if i.endswith(".jpg")]))
# Files must be in the current working directory tho.
