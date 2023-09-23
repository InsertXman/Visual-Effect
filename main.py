from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import *

desk=GetDC(0)
x=GetSystemMetrics(0)
y=GetSystemMetrics(1)

def effect(sleep,time):
    for i in range (0,time):
        PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), PATINVERT)
        Sleep(sleep)

#the function is written like this effect(sleep time,time)
#example:
#effect(10,100)