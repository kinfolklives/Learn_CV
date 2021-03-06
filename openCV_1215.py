from cv2 import cv2 as cv
import numpy as np
cv.imshow('shapes',getContours(cv.imread('datas/images/shapes_canny.png')))

def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv.resize(
                        imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv.resize(
                        imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv.cvtColor(
                        imgArray[x][y], cv.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        # hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv.resize(
                    imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv.resize(
                    imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv.cvtColor(imgArray[x], cv.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver
def getContours(img):
    contours, hierarchy = cv.findContours(
        img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    print('hierarchy : ', hierarchy)
    for cnt in contours:
        x,y,w,h = cv.boundingRect(cnt)
        print(x,y,w,h)
        epsilon = 0.02*cv.arcLength(cnt, True)
        approx = cv.approxPolyDP(cnt, epsilon, True)
        print(len(approx))
        cv.drawContours(img_color_approx, [approx], 0, (0,255,255), 2)
        cv.imshow("result approx", img_color_approx)
        
