# LEGO slot:0 autostart
# Title: Robot Movement with SPIKE PRIME (3.0)
# Topic: Lesson: Swing Turns
# URL: https://www.cs2n.org/u/mp/badge_pages/2777
# Source: cs2n.org — Coding and Computational Thinking with LEGO SPIKE Prime (3.0)
import runloop
from hub import port
import motor_pair

# Short: Demonstrates swing turns for steering the robot.

# lesson: swing turns https://www.cs2n.org/u/mp/badge_pages/2777
# This program makes the LEGO robot move forward a short distance.
# It uses two wheels, one on port D and one on port C.
WHEEL_CIRCUMFERENCE = 17.6  # The distance around one wheel in centimeters

def get_degree_from_distance(x_cm):
    return int(x_cm / WHEEL_CIRCUMFERENCE * 360)

async def main():
    # Pair the two motors so they work together like a car's wheels.
    motor_pair.pair(motor_pair.PAIR_1, port.D, port.C)

    # 0.45 rotation
    # steering=100 (sharp right)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(4.4*360), 20)
    # await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(1.5*360), 60)

# Run the program
runloop.run(main())