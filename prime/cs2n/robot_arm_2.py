# LEGO slot:0 autostart
# Title: Robot Movement with SPIKE PRIME (3.0)
# Topic: lesson - arm movement
# URL: https://www.cs2n.org/u/mp/badge_pages/2782
# Source: cs2n.org — Coding and Computational Thinking with LEGO SPIKE Prime (3.0)
import runloop
from hub import port
import motor_pair
import motor

# Short: Moves the arm and then makes the robot move a little.

# This program makes the LEGO robot move forward a short distance.
# It uses two wheels, one on port D and one on port C.
WHEEL_CIRCUMFERENCE = 17.6  # The distance around one wheel in centimeters

def get_degree_from_distance(x_cm):
    return int(x_cm / WHEEL_CIRCUMFERENCE * 360)

async def main():
    motor_pair.pair(motor_pair.PAIR_1, port.D, port.C)
    await motor.run_for_degrees(port.A, 80, 500)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, get_degree_from_distance(10), 0, velocity=360)

# Run the program
runloop.run(main())