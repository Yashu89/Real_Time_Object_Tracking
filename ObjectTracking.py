import cv2 as cv
import numpy as np

def nothing(b):
    pass

cv.namedWindow("HSV Trackbars", cv.WINDOW_NORMAL)
cv.resizeWindow("HSV Trackbars", 500, 230)
cv.createTrackbar("H Lower", "HSV Trackbars", 0, 179, nothing)
cv.createTrackbar("S Lower", "HSV Trackbars", 0, 255, nothing)
cv.createTrackbar("V Lower", "HSV Trackbars", 0, 255, nothing)
cv.createTrackbar("H Upper", "HSV Trackbars", 179, 179, nothing)
cv.createTrackbar("S Upper", "HSV Trackbars", 255, 255, nothing)
cv.createTrackbar("V Upper", "HSV Trackbars", 255, 255, nothing)


vid = cv.VideoCapture(0)

center_points = []

while True:
    ret, frame = vid.read()
    if not ret:
        break

    frame = cv.flip(frame, 1)
    frame = cv.GaussianBlur(frame, (7, 7), 0)

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    hL = cv.getTrackbarPos("H Lower", "HSV Trackbars")
    sL = cv.getTrackbarPos("S Lower", "HSV Trackbars")
    vL = cv.getTrackbarPos("V Lower", "HSV Trackbars")
    hU = cv.getTrackbarPos("H Upper", "HSV Trackbars")
    sU = cv.getTrackbarPos("S Upper", "HSV Trackbars")
    vU = cv.getTrackbarPos("V Upper", "HSV Trackbars")

    lower_Color = np.array([hL, sL, vL])
    upper_Color = np.array([hU, sU, vU])

    mask = cv.inRange(hsv, lower_Color, upper_Color)

    mask = cv.erode(mask, None, iterations=2)
    mask = cv.dilate(mask, None, iterations=2)

    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    if contours:

        c = max(contours, key=cv.contourArea)

        if cv.contourArea(c) > 500:
            x, y, w, h = cv.boundingRect(c)
            cx, cy = x + w // 2, y + h // 2

            center_points.append((cx, cy))
            if len(center_points) > 5:
                center_points.pop(0)
            smoothedX = int(np.mean([p[0] for p in center_points]))
            smoothedY = int(np.mean([p[1] for p in center_points]))

            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv.circle(frame, (smoothedX, smoothedY), 5, (0, 0, 255), -1)

            if smoothedY > frame.shape[0]//2:
                cv.putText(frame, f"X:{smoothedX} Y:{smoothedY}", (x, y - 10),
                        cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            else:
                cv.putText(frame, f"X:{smoothedX} Y:{smoothedY}", (x, y + h + 20),
                        cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)    


            if smoothedX < frame.shape[1] // 3:
                command_h = "LEFT"
            elif smoothedX > 2 * frame.shape[1] // 3:
                command_h = "RIGHT"
            else:
                command_h = "FORWARD"

            if smoothedY < frame.shape[0] // 3:
                command_v = "UP"
            elif smoothedY > 2 * frame.shape[0] // 3:
                command_v = "DOWN"
            else:
                command_v = ""

            command = f"{command_h} {command_v}".strip()
        else:
            command = "Very small Object"
    else:
        command = "Object not detected"

    cv.putText(frame, "Move Camera by the Command", (10, 25),
                cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 1)
    
    cv.putText(frame, f"Command: {command}", (10, 50),
                cv.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 0), 1)

    cv.imshow("Object Tracking", frame)
    cv.imshow("Mask", mask)  

    if cv.waitKey(1) & 0xFF == ord('d'):
        break

vid.release()
cv.destroyAllWindows()
