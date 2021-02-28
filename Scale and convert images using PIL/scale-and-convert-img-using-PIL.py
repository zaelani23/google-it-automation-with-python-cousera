#!/usr/bin/env python3

import os
from pathlib import Path
from PIL import Image

newsize = 128, 128
home = str(Path.home())

for file in os.listdir('images/'):
       im = Image.open(home + '/images/' + file).convert('RGB')
       im.rotate(270).resize((newsize)).save("/opt/icons/" + file, "JPEG")