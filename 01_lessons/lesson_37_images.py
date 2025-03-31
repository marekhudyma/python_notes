# pip install pillow

from PIL import Image
img = Image.open('/10_resources/lena.jpg')
type(img)
# img.show()
print(img.size)
print(img.filename)
print(img.format_description)

# img.crop((10, 10, 100, 100)).show()
# img.rotate(90).resize((100, 100)).show()

img.putalpha(100)
img.show()