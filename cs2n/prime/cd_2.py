# LEGO slot:0 autostart
# Title: Continuous Decisions with SPIKE PRIME (3.0)
# Topic: Lesson: Obstacle detection
# URL: https://www.cs2n.org/u/mp/badge_pages/2828
# Source: cs2n.org — Coding and Computational Thinking with LEGO SPIKE Prime (3.0)
import runloop
from hub import port
import motor
import motor_pair
import distance_sensor

# Short: Move until a set position; stop if something gets too close.

async def main():
    motor_pair.pair(motor_pair.PAIR_1, port.D, port.C)

    while motor.relative_position(port.C) <= 2060: 
        distance = distance_sensor.distance(port.B)
        if distance is not None and distance < 200:
            motor_pair.stop(motor_pair.PAIR_1)
        else:
            motor_pair.move(motor_pair.PAIR_1, 0)

runloop.run(main())