import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
iy = initial_ty
ix = initial_tx
gy = light_y
gx = light_x
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    if  initial_tx > light_x  and initial_ty > light_y:
        print('NW')
        iy -= 1
        ix -= 1
    elif iy < gy and ix < gx:
        print("SE")
        iy += 1
        ix += 1

    elif iy > gy and ix < gx:
        print("NE")
        iy -= 1
        ix += 1

    elif iy < gy and ix > gx:
        print("SW")
        iy += 1
        ix -= 1

    elif light_x > initial_tx:
        print('E')
        ix += 1

    elif light_x < initial_tx:
        print('W')
        ix -= 1

    elif initial_ty > light_y:
        print("N")
        iy -= 1

    else:
        print("S")
        iy += 1

    #so ive been stuck here for an hour cus this fucking game doesnt tell you that the postion stays the same and u must manually change it AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
