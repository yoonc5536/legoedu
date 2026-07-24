# LEGO slot:0 autostart
import runloop
from hub import port
import motor_pair

# This program makes the LEGO robot move forward a short distance.
# It uses two wheels, one on port D and one on port C.

DISTANCE_TO_MOVE = 10.0  # How far we want the robot to go in centimeters
WHEEL_CIRCUMFERENCE = 17.6  # The distance around one wheel in centimeters

async def main():
    # Pair the two motors so they work together like a car's wheels.
    motor_pair.pair(motor_pair.PAIR_1, port.D, port.C)

    # Wait for 2 seconds so the robot is ready before moving.
    await runloop.sleep_ms(2000)

    # Convert the target distance into wheel turns in degrees.
    # This helps the robot know how far to roll.
    distance_to_degree = int(DISTANCE_TO_MOVE / WHEEL_CIRCUMFERENCE * 360)

    # Move the robot forward by that many degrees.
    # The 0 means the robot should move straight.
    # The velocity of 360 makes it move at a steady speed.
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, distance_to_degree, 0, velocity=360)

# Run the program
runloop.run(main())