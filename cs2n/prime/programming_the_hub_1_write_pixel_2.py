import runloop
from hub import light_matrix

# A list of 25 brightness values (5x5 grid)
# 100 = Bright, 0 = Off

TARGET_PATTERN = [
    0, 100, 100, 100, 0,
    100, 0, 0, 0, 100,
    100, 0, 50, 0, 100,
    100, 0, 0, 0, 100,
    0, 100, 100, 100, 0
]

async def main():
    # Pass the list directly into show()
    light_matrix.show(TARGET_PATTERN)
    await runloop.sleep_ms(14000)
    light_matrix.clear()

runloop.run(main())