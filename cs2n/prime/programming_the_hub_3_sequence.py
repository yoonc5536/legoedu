import runloop
from hub import light_matrix

# This program makes a simple animation on the hub.
# It shows one column of lights at a time, like a moving bar.
# This matches the "Programming a Sequence" lesson.

# Build one pattern for the whole 5x5 light matrix.
# The number k tells us which column should be lit up.
# Each pattern has 25 values, one for each light.
def get_target_pattern(k):
    # Make a list with 25 items.
    # If the light is in the chosen column, turn it on with brightness 100.
    # Otherwise, leave it off with brightness 0.
    mat = [100 if i % 5 == k else 0 for i in range(25)]
    return mat

async def main():
    # Start from the rightmost column and move left.
    # The range(4, -1, -1) means: 4, 3, 2, 1, 0.
    for k in range(4, -1, -1):
        # Create the pattern for the current column.
        # Then show it on the hub screen.
        light_matrix.show(get_target_pattern(k))

        # Wait a short time so Alex can see the animation.
        await runloop.sleep_ms(500)

    # The program is done after all the columns have been shown.
    return

# Start the program.
runloop.run(main())

