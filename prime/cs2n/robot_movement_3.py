# LEGO slot:0 autostart
# Title: Robot Movement with SPIKE PRIME (3.0)
# Topic: Lesson: Turning in Place
# URL: https://www.cs2n.org/u/mp/badge_pages/2775
# Source: cs2n.org — Coding and Computational Thinking with LEGO SPIKE Prime (3.0)
import runloop
from hub import port
import motor_pair

# Short: Turns the robot in place according to the lesson.


# This program makes the LEGO robot move forward a short distance.
# It uses two wheels, one on port D and one on port C.

DISTANCE_TO_MOVE = 10.0  # How far we want the robot to go in centimeters
WHEEL_CIRCUMFERENCE = 17.6  # The distance around one wheel in centimeters

async def main():
    # Pair the two motors so they work together like a car's wheels.
    motor_pair.pair(motor_pair.PAIR_1, port.D, port.C)

    # 0.45 rotation
    # steering=100 (sharp right)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(0.45*360), 100)

# Run the program
runloop.run(main())