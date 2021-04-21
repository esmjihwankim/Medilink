from flask import Flask, url_for,render_template, redirect
from markupsafe import escape



app = Flask(__name__)

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
    #return render_template('webapp.html')

def move_to_down():
    print('down')
    return render_template('webapp.html')

def move_to_right():
    print('right')
    return render_template('webapp.html')

def move_to_left():
    print('left')
    return render_template('webapp.html')

