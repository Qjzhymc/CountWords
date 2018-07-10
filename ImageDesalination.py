from PIL import Image
im=Image.open('C:/Users/22467/Downloads/westbrook.jpg')
pix=im.load()
width=im.size[0]
height=im.size[1]
im2=Image.new("RGB",(width,height))
for x in range(width):
	for y in range(height):
		r,g,b=pix[x,y]
		r,g,b=r//2,g//2,b//2
		im2.putpixel((x,y),(r,g,b))
im.show()

im2.show()
im2.save('C:/Users/22467/Downloads/westbrook2.jpg')