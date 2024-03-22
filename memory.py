"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import shuffle
from turtle import (up, goto, down, color, begin_fill,
                    forward, left, end_fill, clear, update,
                    shape, stamp, write, ontimer, setup,
                    addshape, hideturtle, tracer, onscreenclick, done)

from freegames import path

import time

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
tap_count = 0


def square(x, y):
    """
    Draw white square with black outline at (x, y).
    Args:
        x: x-coordinate.
        y: y-coordinate.
    """
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """
    Convert (x, y) coordinates to tiles index.
    Args:
        x: x-coordinate.
        y: y-coordinate.
    Returns:
        int: tiles index.
    """
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """
    Convert tiles count to (x, y) coordinates.
    Args:
        count: tiles count.
    Returns:
        tuple: (x, y) coordinates.
    """
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """
    Update mark and hidden tiles based on tap.
    Args:
        x: x-coordinate.
        y: y-coordinate.
    """
    global tap_count
    tap_count += 1
    print("Number of taps: ", tap_count)
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """
    Draw image and tiles.
    """
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    up()
    goto(-200, 200)
    write("Number of taps: " + str(tap_count), font=('Arial', 30, 'normal'))

    if not any(hide):
        up()
        goto(-100, 0)
        write("All tiles revealed", font=('Arial', 30, 'normal'))
        print("All tiles revealed")
        print("Game Over")

        time.sleep(5)
        exit()

    update()
    ontimer(draw, 100)


# shuffle tiles and setup game
shuffle(tiles)

# setup game
setup(500, 500, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
