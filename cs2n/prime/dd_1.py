# LEGO slot:0 autostart
# Title: Discrete Decisios with SPIKE PRIME (3.0)
# Topic: Lesson: Turn if not clear
# URL: https://www.cs2n.org/u/mp/badge_pages/2816
# Source: cs2n.org — Coding and Computational Thinking with LEGO SPIKE Prime (3.0)
import runloop
from hub import port
import motor_pair
import distance_sensor

# Short: If something is very close, the robot will turn a little bit.

async def main():
    motor_pair.pair(motor_pair.PAIR_1, port.D, port.C)
    distance = distance_sensor.distance(port.B)
    if distance is not None and distance < 200:
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(0.45*360), 100)

runloop.run(main())