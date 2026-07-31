# LEGO slot:0 autostart
# Title: Programming the Hub with SPIKE PRIME (3.0)
# Topic: Lesson: Light commands
# URL: https://www.cs2n.org/u/mp/badge_pages/2764
# Source: cs2n.org — Coding and Computational Thinking with LEGO SPIKE Prime (3.0)

from hub import light_matrix
import runloop

# Short: Shows a happy face image on the hub screen.

async def main():
    # This is our first light-program for the LEGO SPIKE Prime hub.
    # https://www.cs2n.org/u/mp/badge_pages/2764
    # It matches the CS2N lesson about Light Commands.
    # The hub has a light matrix, which is like a tiny screen.

    # When the program starts, show a happy face on the hub.
    # This is a built-in image that the hub already knows how to display.
    light_matrix.show_image(light_matrix.IMAGE_HAPPY)

    # Wait for 5 seconds so Alex can see the smile.
    # In the lesson, the light pattern is shown for 5 seconds.
    await runloop.sleep_ms(5000)

    # After the waiting time is done, clear the screen.
    # This helps the hub return to a blank state.
    light_matrix.clear()

# Start the program and run the main function.
runloop.run(main())
