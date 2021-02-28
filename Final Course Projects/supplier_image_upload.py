#!/usr/bin/env python3

import requests
import os
from pathlib import Path
import pathlib

url = "http://localhost/upload/"
home = str(Path.home())
files = os.listdir(home + '/supplier-data/images/')

for file in files:
	if pathlib.Path(file).suffix == '.jpeg':
		with open(home + '/supplier-data/images/' + file, 'rb') as opened:
			r = requests.post(url, files={'file': opened})
			print(r.status_code)
