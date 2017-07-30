import cv2
import numpy as np
import os

def convert_to_gray():
	for file_type in ['positives/morty']:
		for img in os.listdir(file_type):
			try:
				current_img_path = str(file_type) + '/' + str(img)
				i = cv2.imread(current_img_path, cv2.IMREAD_GRAYSCALE)
				resized = cv2.resize(i, (50,50))
				cv2.imwrite("pos/"+str(img), resized)

			except Exception as e:
				print(str(e))

print(os.getcwd())
convert_to_gray()
