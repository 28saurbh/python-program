from PIL import Image

image1 = Image.open('img.jpg')
im1 = image1.convert("RGB")
im1.save('img.pdf')