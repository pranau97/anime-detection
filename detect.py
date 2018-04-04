'''Python script to perform image detection and reverse image lookup.'''

import os
import sys
import json
import logging
import cv2
from saucenao.saucenao import SauceNao

DB = {'3.xml': 'Hunter x Hunter',
      '2.xml': 'Hunter x Hunter',
      '5.xml': 'Death Note',
      '4.xml': 'Donald Duck Show',
      '1.xml': 'Rick and Morty'}

CHARACTER_DB = {'3.xml': 'Gon',
                '2.xml': 'Killua',
                '5.xml': 'L Death Note',
                '4.xml': 'Donald',
                '1.xml': 'Morty'}


def detect_characters(img_path):
    '''Reads the input image to do the following -
        * Detect an anime character from the trained database of characters.
        * Pass the image to cloud library to get visually similar images based on the content of the image.
        * Scrape more images based on the character detected.
    '''

    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    flag = 0
    for file in os.listdir('cascades'):
        cascade = cv2.CascadeClassifier('cascades/' + str(file))
        detect = cascade.detectMultiScale(gray, 1.3, 5, 0, (100, 100))

        for (x, y, w, h) in detect:
            print('Series: ' + DB[str(file)])
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            flag = 1

            api_data = json.load(open('api_key.json'))
            sauce = SauceNao("", databases=999, minimum_similarity=30, combine_api_types=False,
                             api_key=api_data['saucenao_key'],
                             exclude_categories='', move_to_categories=False, output_type=SauceNao.API_HTML_TYPE, start_file='',
                             log_level=logging.ERROR, title_minimum_similarity=30)

            data = {
                "Records": [{"keywords": CHARACTER_DB[str(file)], "limit": 20, "print_urls": False}]
            }

            print("Uploading image...")

            results = sauce.check_file(img_path)
            print("Evaluating image...\n")
            print(results)
            print("\n")
            print("Getting similar images...")

            with open('config.json', 'w') as outfile:
                json.dump(data, outfile)

            os.system("googleimagesdownload -cf config.json > /dev/null")

            print("Found 20 images similar in content to given image. Check the downloads folder for the downloaded images.")

        if flag == 1:
            break

    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 detect.py /path/to/input/image')
        sys.exit(0)
    detect_characters(sys.argv[1])
