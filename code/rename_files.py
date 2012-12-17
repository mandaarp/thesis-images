PREFIX = "pedestrian-back-"

import glob
import os

g = glob.glob("*.jpg")

for i in range(len(g)):
	os.rename(g[i], PREFIX + str(i+1) + ".jpg")



