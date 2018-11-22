import curses
import random
import time
import numpy as np

#do everything as row,column and [row][column]
#the numpy array seems to be indexed backwards

width = 10
height = 25
speed = 5
# .:-=+*#%@
gradient = [' ','.',':','-','=','+','*','#','%','@']



def main(stdscr):
    stdscr.nodelay(True)
    a = np.zeros((height,width))
    while True:
        stdscr.clear()
        a = np.roll(a,-1,axis=0)
        #the roll call needs to be replaced with a blending call
        #i dont know if this is the same as the averaging call
        for i in range(0,width):
            a[height-1][i]=random.random()
            #this random bit needs to be replaced with a better palette
        for x in range(0,width):
            for y in range(0,height):
                ch = gradient[int(len(gradient)*a[y][x])]
                stdscr.addstr(y,x,ch)
                #needs the color added in here at some point
        stdscr.refresh()
        if stdscr.getch() == ord('q'):
            break
        time.sleep(1/speed)
curses.wrapper(main)
