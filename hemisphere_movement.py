# hemisphere_movement.py takes photos of an object from different angles
import cv2
import os
import time
from datetime import datetime
from Robo import RoombaController  # Ensure that this import is correct

# Initialize the RoombaController
controller = RoombaController()
controller.start_roomba()

# Get the number of pictures to be taken from the user
num_pictures = 20

# Create a directory to save the pictures
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
directory = os.path.expanduser(f'~/Pictures/robot/{timestamp}')

if not os.path.exists(directory):
    os.makedirs(directory)

# Initialize the camera
cap = cv2.VideoCapture(2)

if not cap.isOpened():
    print("Error: Could not open camera.")
    controller.close()
    exit()

# Take pictures every 2 seconds for the specified number of times
for i in range(num_pictures):
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to grab frame.")
        break

    # filename = f"{directory}/{i + 1}.png"
    filename = f"{directory}/{str(i + 1).zfill(len(str(num_pictures)))}.png"
    cv2.imwrite(filename, frame)
    print(f"Saved {filename}")

    # Move the robot for 0.2 seconds forward between photos
    # controller.send_move_command([137, 0, 100, 128, 0], seconds=0.2)  # Move Forward
    controller.move_forward(0.6)
    controller.turn_left(0.05)

    # Wait for the remaining 1.8 seconds to make a total delay of 2 seconds between photos
    time.sleep(0.6)

# Release the camera
cap.release()

# Close the Roomba Controller
controller.close()

print("Done.")

