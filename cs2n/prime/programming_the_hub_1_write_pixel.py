from hub import light, light_matrix
import runloop

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
