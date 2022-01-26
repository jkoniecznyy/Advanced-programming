from imutils.video import VideoStream, FileVideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2


def build_model(ARGS):
    # load our serialized model from disk
    print("[INFO] loading model...")
    return cv2.dnn.readNetFromCaffe(ARGS["prototxt"], ARGS["model"])
