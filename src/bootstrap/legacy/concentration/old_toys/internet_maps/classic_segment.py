import cv2
import pytesseract
from multiprocessing import Pool, freeze_support
import traceback
# nvm.
# TimeoutError?
# use graph query to do this.
# randomly select three?


def parallel(x, v, z):
    with Pool(processes=x) as pool:
        return pool.map(v, z)


def getText(f):  # shit.
    config = ("-c tessedit_do_invert=0 --oem 3 --psm 6")  # LSTM is awful.
    # get it a try.
    # must likely we shall use a language detector before use?
    return pytesseract.image_to_string(f, lang="eng", config=config, nice=0)
# def saveMe(a,b):
#     cv2.imwrite("dreamer/"+str(a)+".png",b)
# this is a simple method. we can adjust the values with ease.
# we can have different values with filter.
# x,y,w,h
# do we need conversions here?
# this cannot detect the line direction -> fourier transform -> linear analysis.
# if __name__ == "__main__":
    # freeze_support()
    # do this in __main__


def getRead(image):
    # image = cv2.imread(sx)
    # change this config.
    # turn it into some b&w.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sh, sw = gray.shape[:2]
    gray = cv2.bitwise_not(gray)
    blur = cv2.GaussianBlur(gray, (3, 1), 0)  # odd different.
    thresh = cv2.adaptiveThreshold(
        blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 30)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 2))
    dilate = cv2.dilate(thresh, kernel, iterations=4)
    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    ar = []
    ROI_number = 0  # i must slice it around.
#   # shall we use multithreading?
#   cv2.imshow("gray",gray)
#   cv2.waitKey(0)
#   cv2.imshow("blur",blur)
#   cv2.waitKey(0)
#   cv2.imshow("thresh",thresh)
#   cv2.waitKey(0)
#   cv2.imshow("dilate",dilate)
#   cv2.waitKey(0)
# #   cv2.imshow(" ",gray)
#   cv2.waitKey(0)
#   cv2.imshow(" ",gray)
#   cv2.waitKey(0)
    # use multilanguage mode.
    # too fucking long.
    # what the heck?
    for c in cnts:
        area = cv2.contourArea(c)
        x, y, w, h = cv2.boundingRect(c)
        # fucking hell.
        try:
            y0_, y1_ = y-4, y+8+h
            if y0_ < 0:
                y0_ = 0
            if y1_ > sh:
                y1_ = sh
            f = gray[y0_:y1_, x:x+w]  # the way to crop the image.
            _thresh = 127
            # increase contrast?
            # how comes?
            # f0=cv2.adaptiveThreshold(f,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,3,1)*0.03
            f = cv2.threshold(f, _thresh, 255, cv2.THRESH_BINARY)[1]
            # f=f+(f0*0.05)
            h1, w1 = f.shape[:2]
            f = cv2.resize(f, (w1*2, h1*2), 2, 2)
            # fx,fy=f.shape
            # finally some shit?
            # # f=cv2.bitwise_not(f)
            # cv2.imshow("dilate",f)
            # cv2.waitKey(0)
            # we are gonna check this twice.
            ar.append([f, [x, y, w, h], area])
        except:
            e = traceback.format_exc()
            print(e)
            pass
    asr, axr = list(reversed(sorted(ar, key=(lambda x: x[2]))))[:5], []
    for ra, rx in enumerate(parallel(5, getText, list(map((lambda x: x[0]), asr)))):
        text = rx
        axr.append([text, asr[ra][1]])
    return axr
    # store some python objects?
    # do the recording.
    #     cv2.rectangle(image, (x, y - 4), (x + w, 8 + y + h), (36, 255, 12), 3)
    #     cv2.putText(image,text,(int(x+w/2),int(y+h/2)),cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
    # af=0
    # positional data? nvm.
    # for a0, b0 in ar:
    #     saveMe(af,a0)
    #     af+=1
    # cv2.imshow('thresh', thresh)
    # cv2.imshow('dilate', dilate)
    # cv2.imshow('image', image)
    # cv2.waitKey()
# this shit is production ready.
# better use char segments.
