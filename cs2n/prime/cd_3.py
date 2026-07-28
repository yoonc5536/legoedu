# LEGO slot:0 autostart
# Title: Continuous Decisions with SPIKE PRIME (3.0)
# Topic: Lesson: Line Tracking
# URL: https://www.cs2n.org/u/mp/badge_pages/2830
# Source: cs2n.org — Coding and Computational Thinking with LEGO SPIKE Prime (3.0)
import runloop
from hub import port
import motor
import motor_pair
import distance_sensor
import color_sensor
import color

# Short: Use the color sensor to turn; this helps follow a line or edge.

async def main():
    motor_pair.pair(motor_pair.PAIR_1, port.D, port.C)
    while True:
        if color_sensor.color(port.F) == color.BLUE:
            motor_pair.move(motor_pair.PAIR_1, -20)
        else:
            motor_pair.move(motor_pair.PAIR_1, 20)


runloop.run(main())