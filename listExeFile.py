# List all the execlusive files in a given dir (Python)

import os

path = '/home/data_analysis/tools/'

files = os.listdir(path)

for f in files:
  if f.lower().endswith('*.exe'):
	print(f)
   
