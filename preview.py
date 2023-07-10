import os
import json
# enable ansi escape codes on windows
os.system("")

with open("colors.json") as f:
	colors = json.load(f)

for flavor_name, flavor_colors in colors.items():
	print("%s:" % flavor_name)
	
	for color_name, color_code in flavor_colors.items():
		red   = int(color_code[1:3], 16)
		green = int(color_code[3:5], 16)
		blue  = int(color_code[5:7], 16)
		
		if (0.2126 * red
		  + 0.7152 * green
		  + 0.0722 * blue) > 128:
			print("\t%s: \x1b[48;2;%d;%d;%dm\x1b[30m%s\x1b[0m"
			      % (color_name, red, green, blue, color_code))
		else:
			print("\t%s: \x1b[48;2;%d;%d;%dm\x1b[97m%s\x1b[0m"
			      % (color_name, red, green, blue, color_code))
	
	print()
