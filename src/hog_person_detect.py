from datetime import datetime

import cv2
import imutils


class HogPersonDetect:
    def __init__(self):
        # Initialize the model
        self._model = cv2.HOGDescriptor()
        self._model.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        self._regions = None

    def _read_img(self, image_path: str):
        # Read and resize the img from path
        image = cv2.imread(image_path)
        return imutils.resize(image, width=min(400, image.shape[1]))

    def _show_result(self, image, regions, time):
        # Mark people in the img
        counter = 0
        for (x, y, w, h) in regions:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            counter += 1
        print(f'Model detected {counter} people in {time} s.')
        # Show given img
        cv2.imshow('Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def person_detect(self, path: str, type):
        if type == 'img':
            self._img_person_detect(path)
        else:
            self._vid_person_detect(path)

    def _img_person_detect(self, image_path: str):
        image = self._read_img(image_path)

        timestamp = datetime.now()
        # use the cv2.HOGDescriptor_getDefaultPeopleDetector to detect people on the img
        (regions, _) = self._model.detectMultiScale(image, winStride=(4, 4), padding=(4, 4), scale=1.05)

        time = float("{:.2f}".format((datetime.now() - timestamp).total_seconds()))

        self._show_result(image, regions, time)

    def _vid_person_detect(self, vid_path: str):
        cv2.startWindowThread()
        if vid_path == 'your_camera':
            cap = cv2.VideoCapture(0)
        else:
            cap = cv2.VideoCapture(vid_path)

        while cap.isOpened():
            # Read the video stream
            ret, image = cap.read()
            if ret:
                image = imutils.resize(image,
                                       width=min(400, image.shape[1]))

                # Detecting all the regions
                # in the Image that has a
                # pedestrians inside it
                (regions, _) = self._model.detectMultiScale(image,
                                                            winStride=(4, 4),
                                                            padding=(4, 4),
                                                            scale=1.05)

                # Drawing the regions in the
                # Image
                for (x, y, w, h) in regions:
                    cv2.rectangle(image, (x, y),
                                  (x + w, y + h),
                                  (0, 0, 255), 2)

                # Showing the output Image
                cv2.imshow("Image", image)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break

        cap.release()
        cv2.destroyAllWindows()
