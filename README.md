# Virtual Marker Using OpenCV

This Python script utilizes the OpenCV library to perform color tracking using a webcam. It captures video frames, detects a specified color range in the frames, and draws circles on the detected points.

## Getting Started

### Prerequisites
- Python
- OpenCV library (`pip install opencv-python`)

### Running the Script
1. Clone the repository:
   ```bash
   git clone https://github.com/Krishanu-007/Virtual-Marker.git
   cd Virtual-Marker
2. Run the script:
   ```bash
   python Virtual Paint.py
3. Press 'q' to exit the application.
## Code Structure

### Libraries Used
- `cv2`: OpenCV library for computer vision tasks
- `numpy`: Numerical operations library

### Script Overview
1. **Set Frame Parameters:**
   - Set the frame height, width, and brightness for video capture.

2. **Open Video Capture Object:**
   - Open a video capture object (using the default camera).

3. **Set Video Capture Properties:**
   - Set properties for video capture (height, width, brightness).

4. **Define Color Range and Drawing Color:**
   - Define a color range in HSV format (Hue, Saturation, Value).
   - Define a color for drawing on the frame (BGR format).

5. **Initialize Point Lists:**
   - Create lists to store detected points.

6. **Implement Functions:**
   - `findColor(img, testColor, drawColor)`: Find specified color in the image and update the points list.
   - `getContours(img)`: Find contours in the image and return center coordinates.
   - `drawCanvas(points)`: Draw circles on the frame based on detected points.

7. **Main Loop:**
   - Read frames from video capture.
   - Find color in the frame and update points.
   - Draw circles on the frame based on the detected points.
   - Display the resulting frame.
   - Press 'q' to exit the loop.

8. **Release Resources:**
   - Release the video capture object.

9. **Close OpenCV Windows:**
   - Close all OpenCV windows.
## Contributing

I am open for all types of contributions! If you have suggestions, enhancements, or bug fixes, feel free to contribute.
Being a newbie below are the list of some of the issues I came accross and don't know how to solve, feel free to contribute:

### Situations that need some improvement:
- Currently the program just detects the yellow color(I didn't have any other color marker at the time of testing).
- The HSV values form the colorpicker.py aren't relating with that of the real code.
- Currently the code is drawing in mirror image form.
