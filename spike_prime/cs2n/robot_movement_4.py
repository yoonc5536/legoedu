# LEGO slot:0 autostart
# Title: Robot Movement with SPIKE PRIME (3.0)
# Topic: Mini challenge: turn around the craters
# URL: https://www.cs2n.org/u/mp/badge_pages/3121
# Source: cs2n.org — Coding and Computational Thinking with LEGO SPIKE Prime (3.0)
import runloop
from hub import port
import motor_pair

# Short: Mini challenge that practices turning and navigation.

# lesson: turnining in place: https://www.cs2n.org/u/mp/badge_pages/2775

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
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, get_degree_from_distance(15), 0, velocity=360)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(0.45*360), 100)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, get_degree_from_distance(30), 0, velocity=360)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(-0.45*360), 100)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, get_degree_from_distance(40), 0, velocity=360)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(-0.45*360), 100)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, get_degree_from_distance(30), 0, velocity=360)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(0.45*360), 100)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, get_degree_from_distance(30), 0, velocity=360)

# Run the program
runloop.run(main())