# n64-to-xbox360-driver

This is designed to replace the second part of an Instructables guide to
using an Arduino with an N64 controller. The original guide is here:
https://www.instructables.com/id/Use-an-Arduino-with-an-N64-controller/

This driver is designed to read the data coming from the Arduino, and translate
it into a fake Xbox 360 controller on your PC through Xinput.

## Preparation and running

1. Follow that guide to flash the N64_Controller PDE file onto your Arduino.
Stop there instead of continuing to follow the instructions for setting up
the processing project.

2. Make sure you have 64-bit python installed on your machine.

3. Install pyserial and pyxinput via pip.

4. Make sure pyxinput works properly by cloning the repository at
https://github.com/bayangan1991/PYXInput and following the 'Prerequisites'
instructions there to install 'ScpVBus'.

5. Make sure SERIAL_PORT at the top of driver.py is set to the serial port
your Arduino is communicating on.

6. Run `python driver.py` and your N64 controller should successfully
appear as an XBox 360 controller!

## Button mappings

* N64 A -> Xbox A / XInput Button 1
* N64 B -> Xbox B / XInput Button 2
* N64 Z -> Xbox Back / XInput Button 7
* N64 Start -> Xbox Start / XInput Button 8
* N64 L -> Xbox LB / XInput Button 5
* N64 R -> Xbox RB / XInput Button 6
* N64 C-up -> Xbox Left Stick Click / XInput Button 9
* N64 C-down -> Xbox X / XInput Button 3
* N64 C-left -> Xbox Y / XInput Button 4
* N64 C-right -> Xbox Right Stick Click / XInput Button 10
* N64 D-pad -> Xbox D-pad
* N64 Joystick -> Xbox Left Joystick