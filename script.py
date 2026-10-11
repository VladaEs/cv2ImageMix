import cv2 
import numpy as np


image1 = cv2.imread("image1.jpg")
image2 = cv2.imread("image2.jpg")

assert image1 is not None, "Failed to load image1.jpg"
assert image2 is not None, "Failed to load image2.jpg"

mainImage = image1.copy()
h, w = image1.shape[:2]
h2, w2 = image2.shape[:2]
if h * w >= h2 * w2:
    mainImage = image1.copy()
    otherImage = image2.copy()
else:
    mainImage = image2.copy()
    otherImage = image1.copy()

main_h, main_w = mainImage.shape[:2]

other_resized = cv2.resize(otherImage, (main_w, main_h), interpolation=cv2.INTER_AREA)

main_g = mainImage.copy()
gpMain = [main_g]
for i in range(6):
    main_g = cv2.pyrDown(main_g)
    gpMain.append(main_g)

other_g = other_resized.copy()
gpOther = [other_g]
for i in range(6):
    other_g = cv2.pyrDown(other_g)
    gpOther.append(other_g)


levels = 6

lpMain = [gpMain[levels]]
for i in range(levels, 0, -1):
    GE = cv2.pyrUp(gpMain[i])
    GE = cv2.resize(GE, (gpMain[i - 1].shape[1], gpMain[i - 1].shape[0]))
    L = cv2.subtract(gpMain[i - 1], GE)
    lpMain.append(L)

lpOther = [gpOther[levels]]
for i in range(levels, 0, -1):
    GE = cv2.pyrUp(gpOther[i])
    GE = cv2.resize(GE, (gpOther[i - 1].shape[1], gpOther[i - 1].shape[0]))
    L = cv2.subtract(gpOther[i - 1], GE)
    lpOther.append(L)


LS = []
for l_main, l_other in zip(lpMain, lpOther):
    rows, cols, dpt = l_main.shape
    ls = np.hstack((l_main[:, :cols//2], l_other[:, cols//2:]))
    LS.append(ls)

ls_ = LS[0]
for i in range(1, len(LS)):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.resize(ls_, (LS[i].shape[1], LS[i].shape[0]))
    ls_ = cv2.add(ls_, LS[i])

real = np.hstack((mainImage[:, :main_w//2], other_resized[:, main_w//2:]))



cv2.imshow("Main image", mainImage)
cv2.imshow("Other resized to main", other_resized)
cv2.imshow("Blended image", ls_)
cv2.imshow("Real image", real)
cv2.imwrite("blended_image.jpg", ls_)
cv2.imwrite("real_image.jpg", real)




    




cv2.waitKey(0)
cv2.destroyAllWindows()