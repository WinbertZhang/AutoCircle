import math

r = 427
x = 960
y = 587

fileWrite = open('coordinates.txt', 'w')

for i in range(370):
    if i%6 == 0:
        fileWrite.write(str(x+r*math.sin(math.radians(i)) + 0.5) + ' ' + str(y+r*math.cos(math.radians(i))) + '\n')
fileWrite.close()