# This file Robo.py is a python class for bundling robo control and robo state
import serial
import time
import threading
from math import cos, sin, radians


class RoombaController:
    def __init__(self):
        # Serial connection setup -- check which corresponds to the roomba
        # TODO: add scripts for creating a stable alias for Roomba 650 and automate setup to make this deterministic
        self.ser = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=1)

        # Initialize Roomba state
        self.position = [150, 150]
        self.direction = 90
        self.running = True
        self.stopped_due_to_bump = False

        # Start sensor reading thread
        self.sensor_thread = threading.Thread(target=self.read_sensors)
        self.sensor_thread.start()

    def start_roomba(self):
        self.ser.write(bytes([128]))  # Start
        time.sleep(0.1)
        self.ser.write(bytes([131]))  # Safe Mode
        time.sleep(0.1)

    def move_forward(self, seconds=None):
        self.send_move_command([137, 0, 100, 128, 0], seconds)

    def move_backward(self, seconds=None):
        self.send_move_command([137, 255, 156, 128, 0], seconds)

    def turn_left(self, seconds=None):
        self.send_move_command([137, 0, 100, 0, 1], seconds)

    def turn_right(self, seconds=None):
        self.send_move_command([137, 0, 100, 255, 255], seconds)

    def send_move_command(self, command, seconds):
        if seconds is None:
            self.ser.write(bytes(command))
            return

        self.ser.write(bytes(command))
        time.sleep(seconds)
        self.stop_roomba()

    def stop_roomba(self):
        self.ser.write(bytes([137, 0, 0, 0, 0]))  # Stop

    def read_sensors():
        global position
        global direction
        while running:
            # Requesting for Bumps and Wheel Drops.
            ser.write(bytes([142, 7]))
            time.sleep(0.015)
            bump_response = ser.read(1)
            if bump_response:
                bump_data = ord(bump_response)
                if bump_data & 0x03:
                    print("Bump detected!")
                    canvas.create_rectangle(
                        position[0] - 5,
                        position[1] - 5,
                        position[0] + 5,
                        position[1] + 5,
                        fill="red",
                    )
                    stop_robot()

            # Requesting Distance Sensor.
            ser.write(bytes([142, 19]))
            time.sleep(0.015)
            distance_response = ser.read(2)
            if len(distance_response) == 2:
                distance = int.from_bytes(
                    distance_response, byteorder="big", signed=True
                )
                # Calculate new position.
                position[0] += int(distance * cos(radians(direction)))
                position[1] -= int(distance * sin(radians(direction)))
                canvas.create_oval(
                    position[0] - 2,
                    position[1] - 2,
                    position[0] + 2,
                    position[1] + 2,
                    fill="blue",
                    outline="blue",
                )

            # Requesting Angle Sensor.
            ser.write(bytes([142, 20]))
            time.sleep(0.015)
            angle_response = ser.read(2)
            if len(angle_response) == 2:
                angle = int.from_bytes(angle_response, byteorder="big", signed=True)
                direction = (direction + angle) % 360

    def is_stopped_due_to_bump(self):
        return self.stopped_due_to_bump

    def resume_after_bump(self):
        self.stopped_due_to_bump = False
        self.start_roomba()

    def on_close():
        global running
        running = False  # Stop the sensor thread.
        sensor_thread.join()  # Wait for the sensor thread to finish.
        ser.close()  # Close the serial connection.
        root.destroy()


# Usage Example:
if __name__ == "__main__":
    controller = RoombaController()
    controller.start_roomba()
    controller.move_forward(seconds=1)
    controller.move_backward(seconds=1)
