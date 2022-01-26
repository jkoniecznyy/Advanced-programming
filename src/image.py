from imutils.video import VideoStream, FileVideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2


from src.prepare import ARGS, CLASSES, COLORS, NET


def show_img(image):
    # grab the image from the threaded video stream and resize it
    # to have a maximum width of 400 pixels
    image = imutils.resize(image, width=400)
    # grab the image dimensions and convert it to a blob
    (h, w) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)),
                                 0.007843, (300, 300), 127.5)

    # pass the blob through the network and obtain the detections and
    # predictions
    NET.setInput(blob)
    detections = NET.forward()

    # loop over the detections
    for i in np.arange(0, detections.shape[2]):
        # extract the confidence (i.e., probability) associated with
        # the prediction
        confidence = detections[0, 0, i, 2]

        # filter out weak detections by ensuring the `confidence` is
        # greater than the minimum confidence
        if confidence > ARGS["confidence"]:
            # extract the index of the class label from the
            # `detections`, then compute the (x, y)-coordinates of
            # the bounding box for the object
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # draw the prediction on the image
            label = "{}: {:.2f}%".format(CLASSES[idx],
                                         confidence * 100)
            print(label)
            cv2.rectangle(image, (startX, startY), (endX, endY),
                          COLORS[idx], 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(image, label, (startX, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
