#!/usr/bin/env python3

# Import the necessary libraries
import time
import math
from ev3dev2.motor import *
from ev3dev2.sound import Sound
from ev3dev2.button import Button
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sensor.virtual import *

# Create the sensors and motors objects
motorA = LargeMotor(OUTPUT_A)
motorB = LargeMotor(OUTPUT_B)
left_motor = motorA
right_motor = motorB
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)

spkr = Sound()
btn = Button()
radio = Radio()
obtr = ObjectTracker()

color_sensor = ColorSensor(INPUT_1)
ultrasonic_sensor = UltrasonicSensor(INPUT_2)
gyro_sensor = GyroSensor(INPUT_3)
gps_sensor = GPSSensor(INPUT_4)
pen = Pen(INPUT_5)

motorC = LargeMotor(OUTPUT_C) # Magnet

# Here is where your code starts

def Turn(degrees):
    global direction, distance, directionError
    pv = gyro_sensor.angle
    sp = degrees + pv
    for count in range(300):
        pv = gyro_sensor.angle
        error = sp - pv
        error = min(max(error, -100), 100)
        tank_drive.on(error, (-1 * error))
    tank_drive.off(brake=True)

def drive():
    tank_drive.on(25, 25)

while True:
    if ultrasonic_sensor.distance_centimeters <= 25:
        Turn(90)
    else:
        drive()
