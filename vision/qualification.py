import numpy as np
import cv2

cap = cv2.VideoCapture(0)
i = 0
while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame

    blackLower = np.array([0, 50, 0], np.uint8)
    blackUpper = np.array([20, 250, 255], np.uint8)

    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, blackLower, blackUpper)
    mask = cv2.erode(mask, None, iterations=1)
    mask = cv2.dilate(mask, None, iterations=1)
    cv2.imshow('frame', mask)

    contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
    cv2.imshow('mask', frame)
    cnt = max(contours, key=cv2.contourArea)
    cv2.drawContours(frame, cnt, -1, (0, 255, 0), 3)

    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()