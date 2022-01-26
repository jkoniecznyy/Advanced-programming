import glob

from hog_person_detect import HogPersonDetect

if __name__ == "__main__":
    hog = HogPersonDetect()
    for path in glob.glob("images/*.jpg"):
        hog.person_detect(path)