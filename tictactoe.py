"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""
# IMPORT THE FUNCTIONS THAT ARE NECESARY FROM TURTLE TO RUN THE PROGRAM

from turtle import update, up, goto, down, circle, color
from turtle import setup, hideturtle, tracer, onscreenclick, done

from freegames import line

# KEEPS THE COORDINATES OF THE POSITIONS THAT HAVE A SIMBOL ON THE BOARD

boxes = []


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    color("red")
    # / CENTER THE X
    line(x+33, y+33, x + 100, y + 100)
    # \ CENTER THE X
    line(x+33, y + 100, x + 100, y+33)

# RETURNS BOOL IF (x, y) COORDINATES HAVE ALREADY A SIMBOL INSIDE


def ocupacion(x, y):
    return ((x, y) in boxes)


def drawo(x, y):
    """Draw O player."""
    color("blue")
    up()
    # CENTERS THE CIRCLE
    goto(x + 67, y + 27)
    down()
    # REDUCE THE SIZE OF THE CIRCLE
    circle(40)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    # IF THE COORDINATES DOESN´T HAVE A SIMBOLE YET

    if (not (ocupacion(x, y))):

        # REGISTERS THE NEW SIMBOL
        boxes.append((x, y))
        draw = players[player]
        draw(x, y)
        update()
        state['player'] = not player
    else:
        print("Casilla ocupada\n")

    update()


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
