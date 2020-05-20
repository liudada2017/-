import os
import glob
import cv2


if __name__ == '__main__':
    imgDir = './XXX'

    imgList = []
    for root, dirs, files in os.walk(imgDir):
        for file in files:
            if os.path.splitext(file)[1] == '.png':
                imgList.append(os.path.join(root, file))

    for imgPath in imgList:
        img = cv2.imread(imgPath)
        imgPath = imgPath.replace('png', 'jpg')
        cv2.imwrite(imgPath, img)
