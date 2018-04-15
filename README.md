# Anime Character Recognition

An OpenCV based system that uses a Haar Cascade Classifier to detect facial features of Japanese anime characters in a given image file.

## Dependencies

* Linux Distro

* Python 3.4+

* OpenCV 3.2.0+ (If using a binary, ensure GTK support is enabled.)

* googleimagesdownload (Install using `pip3 install googleimagesdownload`)

* saucenao (Install from [here](https://github.com/DaRealFreak/saucenao/))

## Training the classifier

1. Get positive images for the characters you want to train.

2. Get negative images for the classifier.

3. Create more positive samples by adding convolutions to the positive images and superposing them on the negative images.

4. Train the classifier using the in-built OpenCV commands.

## Running the script

1. Add images you want to test in the `test_set` folder.

2. Run `python3 detect.py test_set/<image-name>`. The script should detect the image and scrape similar images using Google Images and saucenao.

## Credits

This [article](https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/) was very informative in explaining the training process for the Haar Cascade classifier.