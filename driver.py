import pyxinput
import serial
from serial.serialutil import SerialException
import sys

SERIAL_PORT = "COM3"
SERIAL_BAUD = 115200
JOYSTICK_MAX_VALUE_X = 90.0
JOYSTICK_MAX_VALUE_Y = 90.0


def main():
    print("Connecting to serial on port {}...".format(SERIAL_PORT))
    try:
        s = serial.Serial(SERIAL_PORT, SERIAL_BAUD)
    except SerialException:
        print("ERROR: '{}' serial port not available".format(SERIAL_PORT))
        sys.exit(1)

    print("Creating fake XBOX 360 Controller...")
    v = pyxinput.vController()
    print("Ready!")

    x_overflow_warning_shown = False
    y_overflow_warning_shown = False

    while True:
        buf = s.read_until()
        elems = buf.split(b" ")

        buttons = elems[0]
        x = float(int(elems[1])) / JOYSTICK_MAX_VALUE_X
        y = float(int(elems[2])) / JOYSTICK_MAX_VALUE_Y
        if (x > 1.0 or x < -1.0) and not x_overflow_warning_shown:
            print(
                "WARNING: X value was larger than expected - increase JOYSTICK_MAX_VALUE_X!"
            )
            x_overflow_warning_shown = True
        if (y > 1.0 or y < -1.0) and not y_overflow_warning_shown:
            print(
                "WARNING: Y value was larger than expected - increase JOYSTICK_MAX_VALUE_Y!"
            )
            y_overflow_warning_shown = True

        # N64 A -> Xbox A / XInput Button 1
        v.set_value("BtnA", (1 if buttons[0] == 52 else 0))
        # N64 B -> Xbox B / XInput Button 2
        v.set_value("BtnB", (1 if buttons[1] == 52 else 0))
        # N64 Z -> Xbox Back / XInput Button 7
        v.set_value("BtnBack", (1 if buttons[2] == 52 else 0))
        # N64 Start -> Xbox Start / XInput Button 8
        v.set_value("BtnStart", (1 if buttons[3] == 52 else 0))

        # D-pad
        d_value = 0
        d_value |= 1 if buttons[4] == 52 else 0
        d_value |= 2 if buttons[5] == 52 else 0
        d_value |= 4 if buttons[6] == 52 else 0
        d_value |= 8 if buttons[7] == 52 else 0
        v.set_value("Dpad", d_value)

        # Skip 8 & 9

        # N64 L -> Xbox LB / XInput Button 5
        v.set_value("BtnShoulderL", (1 if buttons[10] == 52 else 0))
        # N64 R -> Xbox RB / XInput Button 6
        v.set_value("BtnShoulderR", (1 if buttons[11] == 52 else 0))

        # N64 C-up -> Xbox Left Stick Click / XInput Button 9
        v.set_value("BtnThumbL", (1 if buttons[12] == 52 else 0))
        # N64 C-down -> Xbox X / XInput Button 3
        v.set_value("BtnX", (1 if buttons[13] == 52 else 0))
        # N64 C-left -> Xbox Y / XInput Button 4
        v.set_value("BtnY", (1 if buttons[14] == 52 else 0))
        # N64 C-right -> Xbox Right Stick Click / XInput Button 10
        v.set_value("BtnThumbR", (1 if buttons[15] == 52 else 0))

        v.set_value("AxisLx", x)
        v.set_value("AxisLy", y)


if __name__ == "__main__":
    main()
