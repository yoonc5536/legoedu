from hub import light, light_matrix
import runloop

async def main():
    # write your code here
    await light_matrix.write("Hello")
    await runloop.sleep_ms(1000)
    light_matrix.clear()

runloop.run(main())
