import glob
# from src.hog_person_detect import person_detect
from src.video import show_vid
#
# if __name__ == "__main__":
#     for path in glob.glob("images/*.jpg"):
#         person_detect(path, 'jpg')
#
#     for path in glob.glob("movies/*.mp4"):
#         person_detect(path, 'mp4')

for path in glob.glob("movies/*.mp4"):
    print(path)
    show_vid(path, 'mp4')
