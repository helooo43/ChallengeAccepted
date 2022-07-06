import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    b_m = 0
    b_h = 0
    mountain = []
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        if mountain_h > b_h:
            b_h = mountain_h
            b_m = i
    print(b_m)

        
        
