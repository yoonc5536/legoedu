# LEGO slot:0 autostart
# Title: Wait until & seconsors with SPIKE PRIME (3.0)
# Topic: Lesson: Move until near
# URL: https://www.cs2n.org/u/mp/badge_pages/2792
# Source: cs2n.org — Coding and Computational Thinking with LEGO SPIKE Prime (3.0)
import runloop
from hub import port, light_matrix
import distance_sensor
import motor_pair
import color_sensor
# Short: Moves until it detects the red color, then stops.
import color

async def main():
    motor_pair.pair(motor_pair.PAIR_1, port.D, port.C)
    while True:
        motor_pair.move(motor_pair.PAIR_1, 0)
        color_detected = color_sensor.color(port.F)
        if color_detected is not None and color_detected == color.RED:
            break
    motor_pair.stop(motor_pair.PAIR_1)

runloop.run(main())
