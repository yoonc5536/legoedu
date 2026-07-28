# LEGO slot:0 autostart
# Title: Robot Movement with SPIKE PRIME (3.0)
# Topic: Mini challenge: sequential movements
# URL: https://www.cs2n.org/u/mp/badge_pages/3120
# Source: cs2n.org — Coding and Computational Thinking with LEGO SPIKE Prime (3.0)
import runloop
from hub import port
import motor_pair

# Short: Runs a short sequence of movements as a mini challenge.

# mini challenge: https://www.cs2n.org/u/mp/badge_pages/3120

# This program makes the LEGO robot move forward a short distance.
# It uses two wheels, one on port D and one on port C.

DISTANCE_TO_MOVE = 20.0  # How far we want the robot to go in centimeters
WHEEL_CIRCUMFERENCE = 17.6  # The distance around one wheel in centimeters

async def main():
    # Pair the two motors so they work together like a car's wheels.
    motor_pair.pair(motor_pair.PAIR_1, port.D, port.C)

    # Convert the target distance into wheel turns in degrees.
    # This helps the robot know how far to roll.
    distance_to_degree = int(DISTANCE_TO_MOVE / WHEEL_CIRCUMFERENCE * 360)

    for k in range(4):
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, distance_to_degree, 0, velocity=360)
        await runloop.sleep_ms(1000)  # Wait for 1 second before the next move

# Run the program
runloop.run(main())