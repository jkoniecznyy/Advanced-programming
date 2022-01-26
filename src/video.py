import cv2
from src.image import show_img


def show_vid(path, x):
    # Creating a VideoCapture object to read the video
    cap = cv2.VideoCapture(path)

    # Loop until the end of the video
    while (cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        show_img(frame)

        # define q as the exit button
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # release the video capture object
    cap.release()

    # Closes all the windows currently opened.
    cv2.destroyAllWindows()
