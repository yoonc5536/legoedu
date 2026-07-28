# LEGO slot:0 autostart
# Title: Discrete Decisios with SPIKE PRIME (3.0)
# Topic: Lesson: Looped decisions
# URL: https://www.cs2n.org/u/mp/badge_pages/2821
# Source: cs2n.org — Coding and Computational Thinking with LEGO SPIKE Prime (3.0)
import runloop
from hub import port
import motor_pair
import distance_sensor

# Short: Keep moving and react when an obstacle comes close.

WHEEL_CIRCUMFERENCE = 17.6  # The distance around one wheel in centimeters

def get_degree_from_distance(x_cm):
    return int(x_cm / WHEEL_CIRCUMFERENCE * 360)

async def main():
    motor_pair.pair(motor_pair.PAIR_1, port.D, port.C)
    while True:
        distance = distance_sensor.distance(port.B)
        if distance < 200:
            await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(0.45*360), 100)
        else:
            await motor_pair.move_for_degrees(motor_pair.PAIR_1, get_degree_from_distance(30), 0, velocity=360)


runloop.run(main())