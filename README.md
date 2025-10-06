# Real-Time Object Tracking by Python using OpenCV

## Project Overview
This is a **Real-time object tracking system** built using **Python** and **OpenCV**.  
This program detects a single color object in the camera feed and tracks its position in real-time.  
Based on the object’s location in the frame, it generates directional commands to control camera movement(LEFT, RIGHT, UP, DOWN), which gives basic movement control for robotics applications.

---

## Features
- **Real-time tracking** of a single color object using a webcam.  
- Adjustable **HSV trackbars** to fine-tune the color detection of object.  
- **Contour detection** used to identify object boundaries.  
- **Center smoothing** for smooth and stable movement detection.  
- **Directional commands** based on object’s position in the frame.  
- Displays object coordinates and movement commands in real-time.
- Press **d** to quit the program

---

## Custom Improvements
- **Center smoothing:** Averaging the last few detected positions of the object to reduce jitter and improve tracking stability.  
- **Directional movement logic:** Divides the camera frame into zones (LEFT, RIGHT, UP, DOWN) and outputs movement commands based on the smoothed center position.  
- **Real-time coordinate display:** Shows X and Y coordinates of the smoothed center on the video feed for visual feedback.  
- **Dynamic HSV tuning:** Trackbars allow adjusting lower and upper HSV thresholds while the program runs, making detection adaptable to different lighting conditions or objects.

*These additions make the project more than a basic OpenCV tutorial and demonstrate practical problem-solving for robotics applications.*

---

## How to Run

```bash
pip install opencv-python numpy
```

---

## Run Python script
```bash
python object_tracking.py
```
---

## Skills Learned
1. Python Programming
2. OpenCV
3. Video Processing
4. Contour Detection and HSV color filtering
5. Problem Solving

---

## Future Improvements
1. Multi-object tracking
2. Automatic HSV calibration
3. Real-time path tracking
4. Integration with a small robot

