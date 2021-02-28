#!/usr/bin/env python3

import os
from pathlib import Path
from PIL import Image

newsize = 600, 400
home = str(Path.home())

for file in os.listdir(home + '/supplier-data/images/'):
	im = Image.open(home + '/supplier-data/images/' + file).convert('RGB')
	im.resize((newsize)).save(home + '/supplier-data/images/' + file.split('.')[0] + '.jpeg', "JPEG")