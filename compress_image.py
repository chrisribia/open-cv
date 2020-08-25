import PIL
from PIL import Image


mywidth = 2448
myheight = 2448

img = Image.open('scan0001.pdf')
img=img.resize((mywidth,myheight),PIL.Image.ANTIALIAS)
img.save('resize.jpg')


