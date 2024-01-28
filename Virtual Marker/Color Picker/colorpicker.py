import cv2
import numpy as np

# Set the frame width and height for the video capture
frameWidth = 200
frameHeight = 200

# Open a video capture object (0 corresponds to the default camera)
cap = cv2.VideoCapture(0)

# Set the width and height of the video capture
cap.set(3, frameWidth)
cap.set(4, frameHeight)

# Function to be used as a placeholder for the empty trackbar callback
def empty(a):
    pass

# Create a window for trackbars and set their initial positions
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

# Main loop for adjusting color range using trackbars
while True:
    # Read a frame from the video capture
    success, img = cap.read()

    # Convert the frame to HSV color space
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Get the current positions of the trackbars
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    sat_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    sat_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    val_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    val_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    # Create lower and upper bounds for the color range
    lower = np.array([h_min, sat_min, val_min])
    upper = np.array([h_max, sat_max, val_max])

    # Create a mask based on the color range
    mask = cv2.inRange(imgHSV, lower, upper)

    # Apply the mask to the original image to highlight the selected color range
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    # Convert the mask to a 3-channel image for stacking
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    # Stack the original image, mask, and the result side by side for display
    hstack = np.hstack([img, mask, imgResult])

    # Display the stacked image in a window named 'Picker'
    cv2.imshow('Picker', hstack)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
