import urllib.request
import cv2
import numpy as np
import os

def store_raw_images():
    pic_num = 1
    
    if not os.path.exists('neg'):
        os.makedirs('neg')
        
    for i in ['negs/negatives/']:
        for f in os.listdir(i):
            try:
               img = cv2.imread(str(i)+'/'+str(f),cv2.IMREAD_GRAYSCALE)
               resized_image = cv2.resize(img, (100, 100))
               cv2.imwrite("neg/"+str(pic_num)+".jpg",resized_image)
               pic_num += 1
            
            except Exception as e:
               print(str(e))

def find_uglies():
    match = False
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('uglies'):
                try:
                    current_image_path = str(file_type)+'/'+str(img)
                    ugly = cv2.imread('uglies/'+str(ugly))
                    question = cv2.imread(current_image_path)
                    if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
                        print('That is one ugly pic! Deleting!')
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))

def create_pos_n_neg():
    for file_type in ['neg']:
        
        for img in os.listdir(file_type):
            if file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)

#store_raw_images()
create_pos_n_neg()
