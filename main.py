import glob

from hog_person_detect import HogPersonDetect

if __name__ == "__main__":
    hog = HogPersonDetect()
    for path in glob.glob("src/images/*.jpg"):
        hog.person_detect(path, 'img')

    for path in glob.glob("src/videos/*.mp4"):
        hog.person_detect(path, 'vid')

    hog.person_detect('your_camera', 'vid')
