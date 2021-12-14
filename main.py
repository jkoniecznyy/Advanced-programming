import cv2
import matplotlib.pyplot as plt

def main():
    img = cv2.imread('Shrek.jpg')
    print(type(img))
    print(img)
    print(img.shape)
    cv2.imshow('image', img)
    cv2.imwaitKey(0)

    img_convert = cv2.cvtColor(img, cv2.COLOR_BGRR2GRAY)
    img.show(img_convert)
    plt.show()



if __name__ == 'main':
    main()
