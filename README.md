# Roomba 650 Templates

This project has python3 code tested on the Roomba 650, including a python class
for bundling controls and state of the robot, as well as examples of how to
utilize Robo.py motion controls in other scripts, to integrate motion with other
computer actions.

## Requirements

- Linux/Ubuntu operating system
- Python 3.x
- OpenCV library
- Serial library

## Installation

1. Clone the repository:

```sh
git clone https://github.com/klei22/Roomba-650-Templates.git
```

2. (highly recommended) Create a virtual env:

```sh
python3 -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:

```sh
python3 -m pip install -r requirements.txt
```

## Usage

1. Connect the Roomba robot to the computer via USB.
2. Check the dev entry with `sudo dmesg -w` and change from /dev/ttyUSB0 in `Robo.py` if necessary
3. Run the desired Python script to perform the corresponding action:

- `dance.py`: Plays a sequence of dance moves with the Roomba robot.
- `hemisphere_movement.py`: Takes photos of an object from different angles while the Roomba robot moves.
- `pictures.py`: Takes photos from a Linux machine using the connected camera.
- `stationary_rotation.py`: Takes photos of the entire room by rotating the Roomba robot in place.

3. Follow the instructions provided by each script to interact with the Roomba robot and capture photos.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [Apache-2.0](LICENSE).
