# LEGO slot:0 autostart
# Title: Wait until & seconsors with SPIKE PRIME (3.0)
# Topic: Big idea: SPPPA
# URL: https://www.cs2n.org/u/mp/badge_pages/2790
# Source: cs2n.org — Coding and Computational Thinking with LEGO SPIKE Prime (3.0)
import runloop
from hub import port
import distance_sensor
import motor_pair

# Short: Demonstrates waiting and then acting (SPPPA idea).

async def main():
    motor_pair.pair(motor_pair.PAIR_1, port.D, port.C)
    while True:
        motor_pair.move(motor_pair.PAIR_1, 0)
        distance = distance_sensor.distance(port.B)
        if distance is not None and distance < 100:
            break
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(0.45*360), 100)

    while True:
        motor_pair.move(motor_pair.PAIR_1, 0)
        distance = distance_sensor.distance(port.B)
        if distance is not None and distance < 100:
            break
    motor_pair.stop(motor_pair.PAIR_1)


runloop.run(main())