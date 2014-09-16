import pyb
from pyb import Pin
from staccel import STAccel
import math

accel = STAccel()

click_threshold = 1.5
right_threshold = 0.4
left_threshold = -right_threshold
up_threshold = 0.4
down_threshold = -up_threshold
reverse_threshold = -0.4

def isReversed(z):
    if z <= reverse_threshold:
        return True
    else:
        return False

def isClicked(z):
    if z > click_threshold:
        return True
    else:
        return False

def getDiff(x, y):
    x_diff = 0
    y_diff = 0

    if x > right_threshold:
        x_diff = -(x - right_threshold)
    elif x < left_threshold:
        x_diff = -(x - left_threshold)

    if y > up_threshold:
        y_diff = y - up_threshold
    elif y < down_threshold:
        y_diff = y - down_threshold

    return (x_diff, y_diff)

def getRevDiff(y):
    y_diff = 0

    if y > up_threshold:
        y_diff = -(y - up_threshold)
    elif y < down_threshold:
        y_diff = -(y - down_threshold)

    return y_diff

while True:
    x, y, z = accel.xyz()
    print((x, y, z))
    
    #print(x, y, z)
#    abs_accel = math.sqrt(x**2 + y**2 + z**2)
    if isClicked(z):
        print("click!")
        pyb.hid((1, 0, 0, 0))
    elif isReversed(z):
        y_diff = getRevDiff(y)
        pyb.hid((0, 0, 0, int(y_diff*10)))
    else:
        x_diff, y_diff = getDiff(x, y)

#       if x_diff or y_diff:
#            print((int(x_diff*20),int(y_diff*20)))
        pyb.hid((0, int(x_diff*20), int(y_diff*25), 0))


    pyb.delay(20)
