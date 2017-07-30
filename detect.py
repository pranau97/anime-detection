import numpy as np
import cv2
import sys
import os

if len(sys.argv) != 2:
	print('Usage: detect <input-file>')
	sys.exit(0)

img = cv2.imread(sys.argv[1])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cascade_dir = 'cascades'

db = {'3.xml':'Hunter x Hunter', '2.xml': 'Hunter x Hunter', '5.xml': 'Death Note', '4.xml': 'Donald Duck Show', '1.xml': 'Rick and Morty'}

flag = 0
for file in os.listdir(cascade_dir):
	cascade = cv2.CascadeClassifier(cascade_dir+'/'+str(file))
	detect = cascade.detectMultiScale(gray, 1.3, 5, 0, (100,100))

	for (x,y,w,h) in detect:
		print('Series: '+db[str(file)])
		cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
		flag = 1
	if flag == 1:
		break

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
