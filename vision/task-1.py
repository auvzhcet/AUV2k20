import numpy as np
import cv2

def get_centroid(contour):
    M = cv2.moments(contour)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    return [cx,cy]    

def drawCentroid(image, cx, cy):
    center = (int(cx),int(cy))
    cv2.circle(frame, center, 5, (0, 0, 255), -1)

    return image

def mask_image(image, lower, upper, colour):
    mask = cv2.inRange(image, lower, upper)
    mask = cv2.erode(mask, None, iterations=1)
    mask = cv2.dilate(mask, None, iterations=1)
    # cv2.imshow("{}".format(colour),mask)

    return mask

# HSV range for mask
lower_red = np.array([0, 100, 70], np.uint8)
upper_red = np.array([10, 255, 255], np.uint8)

lower_green = np.array([45, 60, 40], np.uint8)
upper_green = np.array([85, 255, 255], np.uint8)

# TODO: refine the ranges. handle the lighting condition.

cap = cv2.VideoCapture(0)
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream")


while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret == True:
        
        # blurred = cv2.GaussianBlur(frame, (11, 11), 0) # performs weighted gaussian averaging
        blurred = cv2.bilateralFilter(frame, 15, 75, 75)    # performs Gaussian blurring but makes sure edges are not blurred
        # TODO: change to gaussian blurring if slow.
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        
        mask_green = mask_image(hsv, lower_green, upper_green, "green")
        mask_red = mask_image(hsv, lower_red, upper_red, "Red")
        #combine the mask
        mask = cv2.bitwise_or(mask_green, mask_red)
        # cv2.imshow("final", mask)

        __, contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours) > 0:
            cnts = sorted(contours, key = cv2.contourArea, reverse = True)[:2]
            cent = list(map(get_centroid, cnts))
            # print(cent)
            cx,cy = (cent[0][0]+cent[1][0])/2, (cent[0][1]+cent[1][1])/2
            drawCentroid(frame, cx, cy)
            
            for cnt in cnts:
                # for contour approximation. uses douglass-peucker algorithm
                # epsilon = 0.1*cv2.arcLength(cnt,True)
                # approx = cv2.approxPolyDP(cnt,epsilon,True)
                # cv2.drawContours(frame, approx, -1, (0, 255, 0), 3)

                x,y,w,h = cv2.boundingRect(cnt)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                
                cv2.imshow("final", frame)
            
        # Press Q on keyboard to  exit
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
    
    # Break the loop
    else: 
        break

cap.release() 
cv2.destroyAllWindows()   