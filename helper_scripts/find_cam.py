import cv2

max_tested = 10
for i in range(max_tested):
    cap = cv2.VideoCapture(i, cv2.CAP_ANY)  # Try to get the i-th device
    if cap.isOpened():
        print(f"Device index {i} is available")
        cap.release()
    else:
        print(f"Device index {i} is NOT available")

