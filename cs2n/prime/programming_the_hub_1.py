from hub import light, light_matrix
import runloop

async def main():
    # write your code here
    light_matrix.show_image(light_matrix.IMAGE_HAPPY)
    await runloop.sleep_ms(5000)
    light_matrix.clear()

runloop.run(main())
