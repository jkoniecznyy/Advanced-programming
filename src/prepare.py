import argparse
import numpy as np


from src.model import build_model

ARGS = None
NET = None
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))


def prepare_model():
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--prototxt",
                    help="path to Caffe 'deploy' prototxt file", default="MobileNetSSD_deploy.prototxt.txt")
    ap.add_argument("-m", "--model",
                    help="path to Caffe pre-trained model", default="MobileNetSSD_deploy.caffemodel")
    ap.add_argument("-c", "--confidence", type=float, default=0.2,
                    help="minimum probability to filter weak detections")
    global ARGS
    ARGS = vars(ap.parse_args())
    global NET
    NET = build_model(ARGS)
