"""
Editor : Kim Jihwan, Kim Taeung
"""
from flask import Flask, url_for,render_template, redirect
from markupsafe import escape

import RPi.GPIO as GPIO
from time import sleep

from board import SCL, SDA
import busio

from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
"""
Initial Setup
"""
app = Flask(__name__)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)   # LED control pin

i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 50
servo1 = servo.Servo(pca.channels[1])
servo2 = servo.Servo(pca.channels[2])
servo3 = servo.Servo(pca.channels[3], min_pulse=100, max_pulse=2600)
servo4 = servo.Servo(pca.channels[4])
servo5 = servo.Servo(pca.channels[5])
servo6 = servo.Servo(pca.channels[6])
servo7 = servo.Servo(pca.channels[7])
"""
initial angle
"""
servo1.angle = 40
servo2.angle = 120
servo3.angle = 60
servo4.angle = 90
servo5.angle = 90
servo6.angle = 120
servo7.angle = 50
time.sleep(0.05)

"""
APP.ROUTE
"""
class S(object):
    _instance = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


def move_left_right(x):
    angle3 = servo3.angle + x
    angle7 = servo7.angle + x
    if angle3 < 90 and angle3 > 35:
        servo3.angle = angle3
    if angle7 < 80 and angle7 > 25:
        servo7.angle = angle7
    time.sleep(0.05)


def move_up_down(y):
    angle1 = servo1.angle + y
    angle2 = servo2.angle - y
    if servo5.angle > 60:
        angle4 = servo4.angle
        angle5 = servo5.angle - y
        angle6 = servo6.angle - y
    else :
    #elif servo5.angle > 30:
        angle4 = servo4.angle
        angle5 = servo5.angle - 1.5 * y
        angle6 = servo6.angle - y
    #else :
    #    angle4 = servo4.angle + y
    #    angle5 = servo5.angle
    #    angle6 = servo6.angle
    
    if angle1 < 120 and angle1 > 30:
        servo1.angle = angle1
    if angle2 < 125 and angle2 > 35:
        servo2.angle = angle2
    if angle5 < 95 and angle5 > 5:
        servo5.angle = angle5
    if angle6 < 125 and angle6 > 55:
        servo6.angle = angle6
    time.sleep(0.05)
    
@app.route('/')
def render_webapp_page():
    return render_template('webapp.html')


@app.route('/move/<direction>', methods = ['POST'])
def move_to_dir(direction):
    if direction == 'up':
        return move_to_up()
    elif direction == 'down':
        return move_to_down()
    elif direction == 'right':
        return move_to_right()
    elif direction == 'left':
        return move_to_left()
    else:
        return

def move_to_up():
    print('up')
    move_up_down(2)
    return render_template('move.html')

def move_to_down():
    print('down')
    move_up_down(-2)
    return render_template('move.html')

def move_to_right():
    print('right')
    move_left_right(2)
    return render_template('move.html')

def move_to_left():
    print('left')
    move_left_right(-2)
    return render_template('move.html')

