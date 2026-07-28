# LEGO slot:0 autostart
# Title: Programming the Hub with SPIKE PRIME (3.0)
# Topic: Challenge: Advertising!
# URL: https://www.cs2n.org/u/mp/badge_pages/2768
# Source: cs2n.org — Coding and Computational Thinking with LEGO SPIKE Prime (3.0)
import runloop
from hub import light_matrix
# Short: Animates patterns to look like a simple advertisement.

# This program creates a simple animated advertisement on the hub.
# It uses a sequence of light patterns so the display looks like a billboard.
# This matches the Advertising! challenge from the lesson.

# Make a pattern with 25 lights.
# The value k chooses whether the lights in alternating positions are turned on.
def get_target_pattern(k):
    # Make a list with 25 items.
    # If the light is in the chosen alternating position, turn it on with brightness 100.
    # Otherwise, leave it off with brightness 0.
    mat = [100 if i % 2 == k else 0 for i in range(25)]
    return mat

# Create a blank pattern with all lights off.
blank_pattern = [0 for i in range(25)]

# Create a full pattern with all lights on.
full_pattern = [100 for i in range(25)]

async def main():
    # Build a list of patterns to show one after another.
    list_seq = []

    # Show a blinking alternating pattern several times.
    list_seq.append(get_target_pattern(0))
    list_seq.append(get_target_pattern(1))
    list_seq.append(get_target_pattern(0))
    list_seq.append(get_target_pattern(1))
    list_seq.append(get_target_pattern(0))
    list_seq.append(get_target_pattern(1))

    # Show a short pause with the screen turned off.
    list_seq.append(blank_pattern)

    # Make a single bright light in the middle.
    pattern_1by1 = blank_pattern.copy()
    pattern_1by1[2 * 5 + 2] = 100
    list_seq.append(pattern_1by1)

    # Make a 3x3 square of bright lights.
    pattern_3by3 = blank_pattern.copy()
    pattern_3by3[1 * 5 + 1:1 * 5 + 4] = [100, 100, 100]
    pattern_3by3[2 * 5 + 1:2 * 5 + 4] = [100, 100, 100]
    pattern_3by3[3 * 5 + 1:3 * 5 + 4] = [100, 100, 100]
    list_seq.append(pattern_3by3)

    # Show a full-screen bright pattern.
    list_seq.append(full_pattern)

    # Add a few more display moments to make the animation feel like an ad.
    list_seq.append(blank_pattern)
    list_seq.append(full_pattern)
    list_seq.append(pattern_3by3)
    list_seq.append(pattern_1by1)
    list_seq.append(blank_pattern)

    # Show each pattern for a short time.
    for pattern in list_seq:
        light_matrix.show(pattern)
        await runloop.sleep_ms(200)

# Start the program.
runloop.run(main())
