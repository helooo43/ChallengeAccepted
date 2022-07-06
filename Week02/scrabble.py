import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
words = []
s = {'eaionrtlsu': 1,
    'dg': 2,
    'bcmp': 3,
     'fhvwy': 4,
     'k': 5,
     'jx': 8,
    'qz': 10}
sums = {}
lts = []
wrds = []

for i in range(n):
    w = input()
    words.append(w)

letters = input()
for letter in letters:
    lts.append(letter)


for word in words:
    a = False
    for letter in word:

        if letter not in lts:
            a = True
            break
    if a:
        pass
    else:
        wrds.append(word)


wrds.reverse()
for word in wrds:
    a = 0
    rrr = []
    for wl in word:
        if wl in lts:
            if wl in rrr:
                break
            else:
                rrr.append(wl)
            for letters in s.keys():
                for letter in letters:
                    if letter == wl:
                        a += s.get(letters)
    sums[a] = word


c = max(sums.keys())
print(sums.get(c))
