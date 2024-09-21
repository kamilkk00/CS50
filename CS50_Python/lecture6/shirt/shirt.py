from PIL import Image, ImageOps
import sys

try:
    file = sys.argv[2]
except IndexError:
    sys.exit ("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit ("Too many command-line arguments")
x = sys.argv[1]
y = sys.argv[2]
if (x[-4:]) == ".jpg" and (y[-4:]) != ".jpg" or (x[-4:]) != ".jpg" and (y[-4:]) == ".jpg":
    sys.exit ("Input and output have different extensions")
if (x[-4:]) != ".jpg" or (y[-4:]) != ".jpg":
    sys.exit ("Invalid output")


try:
    shirt = Image.open("shirt.png")
    with Image.open(x) as new_image:
        new_image = ImageOps.fit(new_image, shirt.size)
        new_image.paste(shirt, (0, 0), shirt)
        new_image.save(y)


except FileNotFoundError:
    sys.exit ("Input does not exist")
