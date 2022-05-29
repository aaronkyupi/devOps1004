from PIL import Image

# Location of the image
img = Image.open("aaronk.png")

# mode of the image
print(img.mode)
img.show()
