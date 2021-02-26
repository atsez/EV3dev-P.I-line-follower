#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires EV3 MicroPython v2.0 or higher.


# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
color_sensor_1 = ColorSensor(Port.S1)
color_sensor_2 = ColorSensor(Port.S2)

# modes : 1(only with one sensor) 2(with two sensors)

robot = DriveBase(left_motor ,right_motor ,wheel_diameter=88 ,axle_track=180)

def line_folower(mode ,distance ,speed ,coefficient) :

    if mode == 1 :

        right_motor.reset_angle(0)
        left_motor.reset_angle(0)
        wait(200)

        reflect_X = 8.5
        speed_X = speed 
        distance_X = distance
        cof = coefficient

        while right_motor.angle() >= distance_X :

            reflect_1 = color_sensor_1.reflection()
            reflect_2 = reflect_X
            turn_rate = (reflect_1-reflect_2) * cof

            robot.drive(speed_X, turn_rate)



    elif mode == 2 :

        right_motor.reset_angle(0)
        left_motor.reset_angle(0)
        wait(200)

        speed_X = speed 
        distance_X = distance
        cof = coefficient

        while right_motor.angle() >= distance_X :

            reflect_1 = color_sensor_1.reflection()
            reflect_2 = color_sensor_2.reflection()
            turn_rate = (reflect_1-reflect_2)

            robot.drive(speed_X, turn_rate)
        

line_folower(2,900,40,0.45)