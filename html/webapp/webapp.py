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
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(12, GPIO.OUT)

# servo = GPIO.PWM(12,50)
# servo.start(0)
i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 50

"""
APP.ROUTE
"""

class S(object):
    _instance = None

    # SERVO_MAX_DUTY=12
    # SERVO_MIN_DUTY=3
    # motor_angle=0
    servo1 = servo.Servo(pca.channel[1])
    servo2 = servo.Servo(pca.channel[2])
    servo3 = servo.Servo(pca.channel[3], min_pulse=100, max_pulse=2600)
    servo1.angle = 40
    servo2.angle = 120
    servo3.angle = 60
    time.sleep(0.05)
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

def move_left_right(x):
    angle3 = servo3.angle + x
    if angle3 < 90 and angle3 > 35:
        servo3.angle = angle3
        time.sleep(0.05)

def move_up_down(y):
    angle1 = servo1.angle + y
    angle2 = servo2.angle - y
    if angle1 < 120 and angle1 > 30:
        servo1.angle = angle1
    if angle2 < 125 and angle2 > 35:
        servo2.angle = angle2
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

