# LEGO slot:0 autostart
# Title: Programming the Hub with SPIKE PRIME (3.0)
# Topic: Lesson: Light commands
# URL: https://www.cs2n.org/u/mp/badge_pages/2764
# Source: cs2n.org — Coding and Computational Thinking with LEGO SPIKE Prime (3.0)
# Start imports
import runloop
from hub import light_matrix

# Short: Shows a simple 5x5 light pattern on the hub screen.

# This is the last quiz challenge from the lesson.
# We are making a pattern on the 5x5 light matrix of the hub.
# The hub screen is made of 25 tiny light dots.

# A list of 25 brightness values (5x5 grid)
# Each number controls one light dot.
# 100 = bright light, 50 = dim light, 0 = light off
# The values are written row by row, from left to right.

TARGET_PATTERN = [
    0, 100, 100, 100, 0,   # Top row: a little point on each side
    100, 0, 0, 0, 100,      # Second row: open space inside the shape
    100, 0, 50, 0, 100,     # Third row: a dim center point
    100, 0, 0, 0, 100,      # Fourth row: same shape as the row above
    0, 100, 100, 100, 0    # Bottom row: the shape closes nicely
]

async def main():
    # Send the pattern to the hub so it can show the lights.
    light_matrix.show(TARGET_PATTERN)

    # Wait for 14 seconds so Alex can see the pattern on the screen.
    await runloop.sleep_ms(14000)

    # Clear the screen when the time is up.
    light_matrix.clear()

# Start the program and run the main function.
runloop.run(main())