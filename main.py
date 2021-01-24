# Wave Height
# -----------
# Using OpenCV, we detect a certain color range and trace a path around it in order
# to calculate the maximum vertical distance within the path from the baseline.
#
# By Mohammad Tomaraei (https://tomaraei.com)
#
# Press the 0 key to see the next image.

import numpy as np
import cv2 as cv


def measure(image_filename):
    # Load the image
    reference = cv.imread(image_filename)

    # Convert BGR to HSV
    hsv = cv.cvtColor(reference, cv.COLOR_BGR2HSV)

    # Define the color range
    lower_limit = np.array([20, 100, 50])
    upper_limit = np.array([70, 255, 255])

    # Threshold the HSV image to get only green colors
    mask = cv.inRange(hsv, lower_limit, upper_limit)

    # Show the detected path
    res = cv.bitwise_and(reference, reference, mask=mask)

    # Find the non-zero pixels to draw a rectangle around the mask
    non_zero = cv.findNonZero(mask)

    # Draw the rectangular box
    x, y, w, h = cv.boundingRect(non_zero)
    cv.rectangle(res, (x,y), (x+w, y+h), (255, 0, 0))

    # Indicate the height
    cv.putText(res, 'Height of rectangle: %d' % h, (60, 300), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv.imshow('res', res)
    cv.waitKey(0)

measure('reference.png')
measure('wave-1.png')
measure('wave-2.png')