from PIL import Image
from sys import argv

for arg in argv[3:]:
	img = Image.open(str(arg))
	new_img = img.resize((int(argv[1]), int(argv[2])))
	new_img.save(str(arg), str(arg.split('.')[1]), optimize=True)	

