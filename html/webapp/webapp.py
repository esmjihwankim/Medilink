"""
Editor : Kim Jihwan, Kim Taeung
"""
from flask import Flask, url_for,render_template, redirect
from markupsafe import escape

import RPi.GPIO as GPIO
from time import sleep

"""
Initial Setup
"""
app = Flask(__name__)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

servo = GPIO.PWM(12,50)
servo.start(0)

"""
APP.ROUTE
"""

class S(object):
    _instance = None

    SERVO_MAX_DUTY=12
    SERVO_MIN_DUTY=3
    motor_angle=0
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

def setServoPos(degree):
    if degree > 180:
        degree = 180
    elif degree < 0:
        degree = 0
    duty = S.SERVO_MIN_DUTY+(degree*(S.SERVO_MAX_DUTY-S.SERVO_MIN_DUTY)/180)
    servo.ChangeDutyCycle(duty)

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
    return render_template('move.html')

def move_to_down():
    print('down')
    return render_template('move.html')

def move_to_right():
    print('right')
    S.motor_angle+=10
    setServoPos(S.motor_angle)
    return render_template('move.html')

def move_to_left():
    print('left')
    S.motor_angle-=10
    setServoPos(S.motor_angle)
    return render_template('move.html')

