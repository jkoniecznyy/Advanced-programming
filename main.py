#
# if __name__ == "__main__":
#     for path in glob.glob("images/*.jpg"):
#         person_detect(path, 'jpg')
#
#     for path in glob.glob("movies/*.mp4"):
#     	  print(path)
#         show_vid(path, 'mp4')

# USAGE
#
# python main.py --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel

import argparse
import time

from imutils.video import VideoStream, FileVideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2

from src.prepare import prepare_model
from src.video import show_vid


prepare_model()
show_vid("D:/Siema/Studia/Mgr 1 Semestr/Zaawansowane programowanie/Repo/Advanced-programming/movies/sign.mp4")
