# LEGO slot:0 autostart
# Title: Wait until & seconsors with SPIKE PRIME (3.0)
# Topic: Lesson: Wait until near
# URL: https://www.cs2n.org/u/mp/badge_pages/2789
# Source: cs2n.org — Coding and Computational Thinking with LEGO SPIKE Prime (3.0)
import runloop
from hub import port, light_matrix
import distance_sensor

# Short: Waits until something is near, then shows a pattern.

TARGET_PATTERN = [100, 100, 100, 100, 100,
                  100, 0, 0, 0, 100,
                  100, 0, 0, 0, 100,
                  100, 0, 0, 0, 100,
                  100, 100, 100, 100, 100]

async def main():
    while True:
        distance = distance_sensor.distance(port.B)
        if distance is not None and distance < 150:
            break
    light_matrix.show(TARGET_PATTERN)
    await runloop.sleep_ms(2000)

runloop.run(main())