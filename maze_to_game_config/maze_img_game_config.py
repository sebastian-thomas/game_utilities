#image to game config json

import json
from PIL import Image

# To generate a config file for a maze
# Each block is assumed to be 32*32 pixels

def rgb2hex(r,g,b):
	return '#%02x%02x%02x' % (r, g, b)

def main():
	blockSize = 32
	im = Image.open('a.png', 'r')
	pix = im.load()
	width, height = im.size
	colors = []
	points = []
	i = 0
	while 16 + i * blockSize < width :
		j = 0
		while 16 + j * blockSize < height:
			pixel = pix[16 + i*blockSize, 16 + j*blockSize]
			hexVal = rgb2hex(pixel[0], pixel[1], pixel[2])
			if hexVal not in colors:
				colors.append(hexVal)

			point = {}
			point['col'] = i
			point['row'] = j
			point['c'] = hexVal
			points.append(point)

			j = j + 1
		i = i + 1

	output = {}
	output['cols'] = (int) (width / blockSize)
	output['rows'] = (int) (height / blockSize)
	output['colors'] = colors
	output['points'] = points
	print(json.dumps(output, indent=4,sort_keys = False ))


if __name__ == "__main__":
	main()