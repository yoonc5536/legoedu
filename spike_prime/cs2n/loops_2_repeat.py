# LEGO slot:0 autostart
# Title: Loops with SPIKE prime (3.0)
# Topic: Lesson: Repeat loop
# URL: https://www.cs2n.org/u/mp/badge_pages/2808
# Source: cs2n.org — Coding and Computational Thinking with LEGO SPIKE Prime (3.0)
import runloop
from hub import port
import motor_pair

# Short: Moves forward and back several times (repeat loop).

# This program makes the LEGO robot move forward a short distance.
# It uses two wheels, one on port D and one on port C.

DISTANCE_TO_MOVE = 10.0  # How far we want the robot to go in centimeters
WHEEL_CIRCUMFERENCE = 17.6  # The distance around one wheel in centimeters

async def main():
    motor_pair.pair(motor_pair.PAIR_1, port.D, port.C)
    distance_to_degree = int(DISTANCE_TO_MOVE / WHEEL_CIRCUMFERENCE * 360)
    for _ in range(3):
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, distance_to_degree, 0, velocity=360)
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, -distance_to_degree, 0, velocity=360)

# Run the program
runloop.run(main())