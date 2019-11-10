import cv2

# load and display original image
image = cv2.imread(filename = "sources/icons-bg.jpg")
# cv2.namedWindow(winname = "original", flags = cv2.WINDOW_NORMAL)
# cv2.imshow(winname = "original", mat = image)
# cv2.waitKey(delay = 0)

# extract, display, and save sub-image
clip = image[514:818, 0:437, :]
# cv2.namedWindow(winname = "clip", flags = cv2.WINDOW_NORMAL)
# cv2.imshow(winname = "clip", mat = clip)
cv2.imwrite(filename = "clip.jpg", img = clip)
# cv2.waitKey(delay = 0)

