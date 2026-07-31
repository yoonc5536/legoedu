# LEGO slot:0 autostart
# Title: Wait until & seconsors with SPIKE PRIME (3.0)
# Topic: Lesson: Wait for Green
# URL: https://www.cs2n.org/u/mp/badge_pages/2796
# Source: cs2n.org — Coding and Computational Thinking with LEGO SPIKE Prime (3.0)
import runloop
from hub import port, light_matrix
import distance_sensor
import motor_pair
import color_sensor
# Short: Waits for green before continuing.
import color

async def main():
    while True:
        color_detected = color_sensor.color(port.F)
        if color_detected is not None and color_detected == color.RED:
            break
    light_matrix.show_image(light_matrix.IMAGE_HAPPY)
    # Wait for 5 seconds so Alex can see the smile.
    # In the lesson, the light pattern is shown for 5 seconds.
    await runloop.sleep_ms(5000)

runloop.run(main())
