# LEGO slot:0 autostart
# Title: Robot Movement with SPIKE PRIME (3.0)
# Topic: lesson - arm movement
# URL: https://www.cs2n.org/u/mp/badge_pages/2782
# Source: cs2n.org — Coding and Computational Thinking with LEGO SPIKE Prime (3.0)
import runloop
from hub import port
# import motor_pair
import motor

# Short: Moves the robot arm up and then down.
# This program makes the LEGO robot move forward a short distance.
# It uses two wheels, one on port D and one on port C.

async def main():
    await motor.run_for_degrees(port.A, 80, 500)
    await motor.run_for_degrees(port.A, -80, 500)

# Run the program
runloop.run(main())