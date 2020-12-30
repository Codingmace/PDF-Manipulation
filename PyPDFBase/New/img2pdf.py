from PIL import Image

image1 = Image.open(r'path where the image is stored\file name.png')
im1 = image1.convert('RGB')
im1.save(r'path where the pdf will be stored\new file name.pdf')
