import requests


img = requests.get("https://home.imgsmail.ru/resplash/107067/i/icons/d6a7eb9f75dc.svg")
img_file = open('path_to_image.svg', 'wb')
img_file.write(img.content)
img_file.close()
