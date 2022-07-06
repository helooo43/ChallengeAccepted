import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
p = []
res = []
r = 1
for i in range(n):
    pi = int(input())
    p.append(pi)

p.sort()
for s in p:
    k = p[r] - s
    res.append(k)
    if r < len(p) - 1:
        r += 1
res.sort()
print(res[1])


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

