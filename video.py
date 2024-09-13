import numpy as np
import cv2

cap = cv2.VideoCapture('opencv_PS/video.mp4')
while True:
    ret, frame = cap.read()
    lower_green= np.array([40, 40, 40])
    upper_green= np.array([80, 255, 255])

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask= cv2.inRange(hsv,lower_green, upper_green)

# Perform Canny edge detection on the mask
    edges = cv2.Canny(mask, 50, 150)

# Dilate the edges to fill gaps
    kernel = np.ones((3, 3), np.uint8)
    edges = cv2.dilate(edges, kernel, iterations=10)
#we can see that as the number of iterations increase, distortion of object becomes less

# Use the edges to refine the mask
    mask[edges != 0] = 0
    mask_not = cv2.bitwise_not(mask)

    replace_color = (255,0,0)
    replacement_img = np.zeros_like(frame, dtype=np.uint8)
    replacement_img[:] = replace_color

    result = cv2.bitwise_and(frame, frame, mask=mask_not) + cv2.bitwise_and(replacement_img, replacement_img, mask=mask)
    cv2.imshow('frame',result)
    
    if cv2.waitKey(0)==ord('q'):
        break
      



cap.release()
 

cv2.destroyAllWindows()