import cv2
import numpy as np

# Set the frame height and width for the video capture
frameheight = 640
framewidth = 480

# Open a video capture object (0 corresponds to the default camera)
cap = cv2.VideoCapture(0)

# Set the height, width, and brightness of the video capture
cap.set(3, frameheight)  # height of the frame
cap.set(4, framewidth)   # width of the frame
cap.set(10, 150)         # brightness of the video

# Define a test color range in HSV format (Hue, Saturation, Value)
testColor = [20, 100, 100, 30, 255, 255]

# Define a color for drawing on the frame (BGR format)
drawColor = [0, 255, 255]  # Yellow color

# List to store detected points
points = []

# Function to find color in the image and update the points list
def findColor(img, testColor, drawColor):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    newPoints = []

    # Define lower and upper bounds for the color range
    lower = np.array(testColor[0:3])
    upper = np.array(testColor[3:6])

    # Create a mask for the specified color range
    mask = cv2.inRange(imgHSV, lower, upper)

    # Get the coordinates of the detected color and draw a circle on the frame
    x, y = getContours(mask)
    cv2.circle(frameResult, (x, y), 10, drawColor, cv2.FILLED)

    # If valid coordinates are found, add them to the newPoints list
    if x != 0 and y != 0:
        newPoints.append([x, y])

    return newPoints

# Function to find contours in the image and return the center coordinates
def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0

    # Loop through the contours and find the bounding rectangle
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)

    # Return the center coordinates of the bounding rectangle
    return x + w // 2, y

# Function to draw circles on the frame based on the detected points
def drawCanvas(points):
    for p in points:
        cv2.circle(frameResult, (p[0], p[1]), 10, drawColor, cv2.FILLED)

# Main loop for capturing video frames and processing
while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # Create a copy of the frame for drawing
    frameResult = frame.copy()

    # Find the color in the frame and update the points list
    newPoints = findColor(frame, testColor, drawColor)

    # If new points are detected, add them to the points list
    if len(newPoints) != 0:
        for ne in newPoints:
            points.append(ne)

    # If points are available, draw circles on the frame
    if len(points) != 0:
        drawCanvas(points)

    # Display the resulting frame
    cv2.imshow("test", frameResult)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

# Release the video capture object
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
