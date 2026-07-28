# LEGO slot:0 autostart
# Title: Programming the Hub with SPIKE PRIME (3.0)
# Topic: Lesson: Light commands
# URL: https://www.cs2n.org/u/mp/badge_pages/2764
# Source: cs2n.org — Coding and Computational Thinking with LEGO SPIKE Prime (3.0)

from hub import light_matrix
import runloop

# Short: Writes a short text message on the hub screen.

async def main():
    # This is the "Write Pixel Message" idea from the lesson.
    # Instead of showing a happy face, we will show words on the hub screen.

    # Show the message "Hello" on the hub display.
    # The write() command lets the hub show letters and words.
    await light_matrix.write("Hello")

    # Wait for 1 second so Alex can read the message.
    await runloop.sleep_ms(1000)

    # Clear the screen after the message is shown.
    light_matrix.clear()

# Start the program and run the main function.
runloop.run(main())
