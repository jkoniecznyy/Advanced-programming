import cv2


def show_img(image):
    frame = cv2.resize(image, (540, 380), fx=0, fy=0,
                       interpolation=cv2.INTER_CUBIC)

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # using cv2.Gaussianblur() method to blur the video

    # (5, 5) is the kernel size for blurring.
    gaussianblur = cv2.GaussianBlur(frame, (5, 5), 0)
    cv2.imshow('gblur', gaussianblur)
