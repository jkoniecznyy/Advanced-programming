from imutils.video import VideoStream, FileVideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2
import os

from src.prepare import ARGS, CLASSES, COLORS, NET
from src.image import show_img


def show_vid(path):
    # initialize the video stream and the FPS counter
    print("[INFO] starting video stream...")
    print(os.getcwd())
    vs = FileVideoStream(path).start()
    fps = FPS().start()
    # loop over the frames from the video stream
    while True:

        frame = vs.read()
        show_img(frame)
        # show the output frame
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

        # update the FPS counter
        fps.update()

    # stop the timer and display FPS information
    fps.stop()
    print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    # do a bit of cleanup
    cv2.destroyAllWindows()
    vs.stop()
