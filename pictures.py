# this file, pictures.py, is just a file for taking photos from a linux machine
# it is include to demonstrate how to combine with dance.py and Robo.py to make
# stationary_rotation.py and hemisphere_movement.py
import cv2
import os
import time
from datetime import datetime

# Get the number of pictures to be taken from the user
num_pictures = int(input("Enter the number of pictures to be taken: "))

# Create a directory to save the pictures
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
directory = os.path.expanduser(f'~/Pictures/robot/{timestamp}')

if not os.path.exists(directory):
    os.makedirs(directory)

# Initialize the camera
# use the ./helper_scripts/find_cam.py to help find your cameras
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Take pictures every 2 seconds for the specified number of times
for i in range(num_pictures):
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to grab frame.")
        break

    filename = f"{directory}/{i + 1}.png"
    cv2.imwrite(filename, frame)
    print(f"Saved {filename}")

    time.sleep(2)

# Release the camera
cap.release()
print("Done.")

