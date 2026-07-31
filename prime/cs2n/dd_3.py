# LEGO slot:0 autostart
# Title: Discrete Decisios with SPIKE PRIME (3.0)
# Mini-lesson: Operators
# https://www.cs2n.org/u/mp/badge_pages/2819
# Source: cs2n.org — Coding and Computational Thinking with LEGO SPIKE Prime (3.0)
import runloop
from hub import port, sound
import motor_pair
import distance_sensor
import color_sensor
import color

# Short: The robot beeps differently if something is close or if it sees red.

WHEEL_CIRCUMFERENCE = 17.6  # The distance around one wheel in centimeters

def get_degree_from_distance(x_cm):
    return int(x_cm / WHEEL_CIRCUMFERENCE * 360)

async def main():
    motor_pair.pair(motor_pair.PAIR_1, port.D, port.C)
    color_detected = color_sensor.color(port.F)
    distance = distance_sensor.distance(port.B)
    if distance < 150 or color_detected == color.RED:
        await sound.beep(440, 200, 100)
    else:
        await sound.beep(220, 500, 100)

runloop.run(main())