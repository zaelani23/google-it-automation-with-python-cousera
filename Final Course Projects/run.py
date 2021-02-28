#! /usr/bin/env python3

import os
import requests
from pathlib import Path
import pathlib

home = str(Path.home())
file_dir = os.path.join(home, 'supplier-data/descriptions/')
files = os.listdir(file_dir)

for file in files:
        file_path = os.path.join(file_dir, file)
        with open(file_path) as desc:
        	read_desc = desc.read()
        	desc_split = read_desc.splitlines()
        	name = desc_split[0]
        	weight = int(desc_split[1].split()[0])
        	description = desc_split[2]
        	image_name = file.replace('txt', 'jpeg')
        	descriptions = {'name': name, 'weight': weight, 'description': description, 
        					'image_name': image_name}
        send_desc = requests.post('http://localhost/fruits/', json = descriptions)
        print(send_desc.status_code)