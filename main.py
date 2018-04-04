#Corey Campbell (28905111) Corey Collins (29175354) 4/4/2018
import numpy as np
import pyscreenshot as ImageGrab

#Takes a list of integers that represent sections of the screen.
#Returns a list of 3 integer lists that represent the RGB values for the average color of the section.
def screenAverages(sections):
	section_averages = [ [0] * 3 for _ in range(len(sections))]
	img = ImageGrab.grab()
	width, _ = img.size
	imageData = list(img.getdata())

	#Add up the RGB values for each pixel in each section.
	for pixel, (r, g, b) in enumerate(imageData):
		for section, (x1, x2, y1, y2) in enumerate(sections):
			#Check to see if the pixel is the bounds of the section.
			if (pixel % width) >= x1 and (pixel % width) < x2 and (pixel // width) >= y1 and (pixel // width) < y2:
				section_averages[section][0] += r
				section_averages[section][1] += g
				section_averages[section][2] += b

	#Divide total RGB values by the number of pixels to get the average value per pixel.
	for section, (x1, x2, y1, y2) in enumerate(sections):
		i = (x2 - x1) * (y2 - y1)
		section_averages[section][0] //= i
		section_averages[section][1] //= i
		section_averages[section][2] //= i

	return section_averages;


def main():
	screenAverages([[0,1,700,800]])


if __name__ == "__main__":
    main()