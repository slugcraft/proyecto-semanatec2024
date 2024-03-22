# proyecto-semanatec2024
# Repositorio del proyecto final de la semana tec

 Dante David Pérez Pérez - A01709226 - Memory Puzzle Game

 Risako Baba - Participante - A01757208 -PacMan

 Miguel Ángel Uribe Esquivel - A01277614 - Tic Tac Toe
 
# Memory Puzzle Game

This is a simple memory puzzle game implemented in Python using the Turtle graphics library. The game presents players with a grid of tiles, each containing a number. The objective is to match pairs of numbers by revealing tiles, exercising memory and concentration skills.

## Added Features

- Added a counter to keep track of the number of taps made: The way a added this feature was by adding a variable called `taps` and then I added a function called `update_taps` that would update the number of taps made every time a tile is clicked. I also added a turtle that would display the number of taps made on the screen.
- Added a final message to congratulate the player when all tiles are revealed: Just check if all the tiles are revealed then in the draw function I added a turtle that would display a message congratulating the player.


- Grid of tiles with numbers.
- Players reveal tiles by clicking on them.
- Matching pairs of numbers are revealed.
- Keeps track of the number of taps made.
- Ends the game when all tiles are revealed.
- Adherence to PEP 8 coding standards.

## Instructions

1. Click on a tile to reveal the number underneath.
2. Click on another tile to reveal its number.
3. If the numbers match, the tiles remain revealed.
4. If the numbers do not match, the tiles are hidden again.
5. Continue revealing tiles until all pairs are matched.
6. The game ends when all tiles are revealed.

### By Dante David Pérez Pérez - A01709226