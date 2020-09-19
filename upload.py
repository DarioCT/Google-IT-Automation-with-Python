
#!/usr/bin/env python3

import glob
from PIL import Image

# Iterate files in supplier-data/images/
for i in glob.glob('supplier-data/images/*'):
    # if the file has an extension tiff open it, convert it to RGB, resize it and save as .jpeg
    if i[-4:] == 'tiff':
      img = Image.open(i)
      img = img.convert("RGB")
      img = img.resize((600, 400))
      img.save(i[:-4] + 'jpeg', 'JPEG')



import requests
import glob

# Upload the images using the Python Requests module

url = "http://localhost/upload/"

for i in glob.glob('supplier-data/images/*'):
  if i[-4:] == 'jpeg':
    with open(i, 'rb') as opened:
      r = requests.post(url, files={'file': opened})
