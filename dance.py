# This is dance.py a playful file for demoing robo-dance moves
import time
from Robo import RoombaController

# Initialize the RoombaController
controller = RoombaController()
controller.start_roomba()

# Repeat dance 2x
num_cycles = 2

# Repeat dance 2x
for i in range(num_cycles):

    # Move the robot for 0.2 seconds forward between photos
    # controller.send_move_command([137, 0, 100, 128, 0], seconds=0.2)  # Move Forward
    controller.move_forward(0.6)
    controller.move_backward(0.6)
    controller.turn_left(0.30)
    controller.turn_right(0.20)

    # Wait for the remaining 1.8 seconds to make a total delay of 2 seconds between photos
    time.sleep(0.6)

# Close the Roomba Controller
controller.on_close()

print("Done.")

