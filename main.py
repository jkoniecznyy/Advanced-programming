import cv2
import matplotlib.pyplot as plt
import pytesseract


def showShrek():
    img = cv2.imread('src/Shrek.jpg')
    print(type(img))
    print(img.shape)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    img_convert = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plt.imshow(img_convert)
    plt.show()


def tesseract():
    pytesseract.pytesseract.tesseract_cmd = (
        r"D:\\Programy\\Studia\\Tesseract\\tesseract.exe"
    )

    # img = cv2.imread('src/piwo.jpg')
    # img = cv2.imread('src/classroom.jpg')
    # img = cv2.imread('src/nfx.jpg')
    # img = cv2.imread('src/mes.jpg')
    img = cv2.imread('src/tatoo.jpg')
    result = pytesseract.image_to_string(img)
    print(result)


if __name__ == '__main__':
    # showShrek()
    tesseract()
