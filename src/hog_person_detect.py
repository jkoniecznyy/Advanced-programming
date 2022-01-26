from datetime import datetime
import imutils
import cv2 as cv


class HogPersonDetect:
    def __init__(self):
        # Initialize the model
        self._model = cv.HOGDescriptor()
        self._model.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())
        self._regions = None

    def _read_img(self, image_path: str):
        # Read and resize the img from path
        image = cv.imread(image_path)
        return imutils.resize(image, width=min(400, image.shape[1]))

    def _show_result(self, image, regions, time):
        # Mark people in the img
        counter = 0
        for (x, y, w, h) in regions:
            cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            counter += 1
        print(f'Model detected {counter} people in {time} s.')
        # Show given img
        cv.imshow('Image', image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def person_detect(self, image_path: str):
        image = self._read_img(image_path)

        timestamp = datetime.now()
        # use the cv.HOGDescriptor_getDefaultPeopleDetector to detect people on the img
        (regions, _) = self._model.detectMultiScale(image, winStride=(4, 4), padding=(4, 4), scale=1.05)

        time = float("{:.2f}".format((datetime.now() - timestamp).total_seconds()))

        self._show_result(image, regions, time)
