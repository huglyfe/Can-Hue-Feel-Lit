#Corey Campbell (28905111) Corey Collins (29175354) 4/4/2018
import numpy as np
import pyscreenshot as ImageGrab
from os import path


#Takes a list of integers that represent sections of the screen.
#Returns a list of 2 integer lists that represent the XY values for the average color of the section.
def screen_averages(sections):
	section_totals = [[0] * 3 for _ in range(len(sections))]
	section_xy = [[0] * 2 for _ in range(len(sections))]
	img = ImageGrab.grab()
	width, _ = img.size
	imageData = list(img.getdata())

	#Add up the RGB values for each pixel in each section.
	for pixel, (r, g, b) in enumerate(imageData):
		for section, (x1, x2, y1, y2) in enumerate(sections):
			#Check to see if the pixel is the bounds of the section.
			if (pixel % width) >= x1 and (pixel % width) < x2 and (pixel // width) >= y1 and (pixel // width) < y2:
				section_totals[section][0] += r
				section_totals[section][1] += g
				section_totals[section][2] += b

	for section, (x1, x2, y1, y2) in enumerate(sections):
		#Divide total RGB values by the number of pixels to get the average value per pixel.
		i = (x2 - x1) * (y2 - y1)
		red = section_totals[section][0] // i;
		green = section_totals[section][1] // i;
		blue = section_totals[section][2] // i;
		
		#Use the formula described in https://gist.github.com/popcorn245/30afa0f98eea1c2fd34d to get xy values.
		r = ((red + 0.055) / (1.055)) ** 2.4 if (red > 0.04045) else (red / 12.92)
		g = ((green + 0.055) / (1.055)) ** 2.4 if (green > 0.04045) else (green / 12.92)
		b = ((blue + 0.055) / (1.055)) ** 2.4 if (blue > 0.04045) else (blue / 12.92)

		X = r * 0.664511 + g * 0.154324 + b * 0.162028
		Y = r * 0.283881 + g * 0.668433 + b * 0.047685
		Z = r * 0.000088 + g * 0.072310 + b * 0.986039

		cx = X / (X + Y + Z)
		cy = Y / (X + Y + Z)

		section_xy[section][0] = cx
		section_xy[section][1] = cy

	return section_xy;

def main():
	print(screen_averages([[0,1,700,800]]))

if __name__ == "__main__":
    main()