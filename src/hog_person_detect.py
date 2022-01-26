from datetime import datetime

import cv2
import imutils


class HogPersonDetect:
    def __init__(self):
        # Initialize the model
        self._model = cv2.HOGDescriptor()
        self._model.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        self._regions = None

    def person_detect(self, path: str):
        # Use proper function depending on the filename
        if path[-4:] == '.jpg':
            self._img_person_detect(path)
        elif path[-4:] == '.mp4':
            self._vid_person_detect(path)

    def _img_person_detect(self, image_path: str):
        # Read img from provided path and call _use_model_on_img()
        image = cv2.imread(image_path)
        self._use_model_on_img(image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def _vid_person_detect(self, vid_path: str):
        # Read video from provided path and call _use_model_on_img()
        # for every frame
        cv2.startWindowThread()
        if vid_path == 'your_camera.mp4':
            cap = cv2.VideoCapture(0)
        else:
            cap = cv2.VideoCapture(vid_path)

        while cap.isOpened():
            # Read the video stream
            ret, image = cap.read()
            if ret:
                self._use_model_on_img(image)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break

        cap.release()
        cv2.destroyAllWindows()

    def _use_model_on_img(self, image):
        # Prepare img
        image = imutils.resize(image, width=min(400, image.shape[1]))

        timestamp = datetime.now()

        # use the cv2.HOGDescriptor_getDefaultPeopleDetector to detect people on the img
        (regions, _) = self._model.detectMultiScale(image, winStride=(4, 4), padding=(4, 4), scale=1.05)

        time = float("{:.2f}".format((datetime.now() - timestamp).total_seconds()))

        # Mark people in the img
        counter = 0
        for (x, y, w, h) in regions:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            counter += 1

        # Put results on the image
        cv2.putText(image, f'People detected: {counter} in {time} s.',
                    (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

        # Show  img
        cv2.imshow("Image", image)
