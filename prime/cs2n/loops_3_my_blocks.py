# LEGO slot:0 autostart
# Title: Loops with SPIKE prime (3.0)
# Topic: Mini-Lesson: My Blocks with Parameters
# URL: https://www.cs2n.org/u/mp/badge_pages/2809
# Source: cs2n.org — Coding and Computational Thinking with LEGO SPIKE Prime (3.0)
import runloop
from hub import port, light_matrix
import motor_pair

# Short: Shows how to make and reuse small blocks (functions) with parameters.

# This program makes the LEGO robot move forward a short distance.
# It uses two wheels, one on port D and one on port C.

WHEEL_CIRCUMFERENCE = 17.6  # The distance around one wheel in centimeters
full_pattern = [100 for i in range(25)]

async def square(length_of_sides):
    for _ in range(4):
        distance_to_degree = int(length_of_sides / WHEEL_CIRCUMFERENCE * 360)
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, distance_to_degree, 0, velocity=360)
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(0.45*360), 100)


async def main():    
    motor_pair.pair(motor_pair.PAIR_1, port.D, port.C)
    await square(30)
    light_matrix.show(full_pattern)
    await square(60)

# Run the program
runloop.run(main())