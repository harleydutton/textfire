import curses
import random
import time
import numpy as np

#do everything as row,column and [row][column]
#the numpy array seems to be indexed backwards

width = 120
height = 30
speed = 5
# .:-=+*#%@
gradient = [' ','.',':','-','=','+','*','#','%','@']
#for colors it looks like we have black, red, yellow, and white.
#i can try and define some more colors in curses
#i want a series of nice oranges between white and black as my 8 colors.


def main(stdscr):
    if curses.has_colors()==True:
        stdscr.addstr(0,0,'Has colors!')
        if curses.can_change_color()==True:
            stdscr.addstr(1,0,'Can change colors!')
            curses.start_color()
            for color in range(1,7):
                curses.init_color(color, 
                        int(1000/6*color), 
                        int(500/6*color), 
                        int(200/6*color))
                #fix this color palatte at some point
            curses.init_color(0,0,0,0)
            curses.init_color(7,1000,1000,1000)
            for pair in range(1,8):
                curses.init_pair(pair,7-pair,0)
            for test in range(0,8):
                stdscr.addstr(2+test,0,'pair {}: '.format(test),curses.color_pair(test))
                stdscr.addstr(2+test,6,'######',curses.color_pair(test))
            stdscr.refresh()
            stdscr.getkey()
            stdscr.clear()
    stdscr.nodelay(True)
    a = np.zeros((height,width))

    while True:
        # a = np.roll(a,-1,axis=0)
        for row in range(0,height-1,1):
            tmp = [None]*width
            for col in range(0,width):
                tmp[col] = a[row][col]
                count = 1
                if col > 0:
                    tmp[col]+=a[row][col-1]
                    count+=1
                if col < width-1:
                    tmp[col]+=a[row][col+1]
                    count+=1
                if row > 0:
                    tmp[col]+=a[row-1][col]
                    count+=1
                    if col > 0:
                        tmp[col]+=a[row-1][col-1]
                        count+=1
                    if col < width-1:
                        tmp[col]+=a[row-1][col+1]
                        count+=1
                if row < height-1:
                    tmp[col]+=a[row+1][col]
                    count+=1
                    if col > 0:
                        tmp[col]+=a[row+1][col-1]
                        count+=1
                    if col < width-1:
                        tmp[col]+=a[row+1][col+1]
                        count+=1
                tmp[col]=tmp[col]/count
            a[row+1]=tmp


        #the roll call needs to be replaced with a blending call
        #i dont know if this is the same as the averaging call
        for i in range(0,width):
            a[height-1][i]=random.random()/2+.5
            #this random bit needs to be replaced with a better palette
        for x in range(0,width):
            for y in range(0,height):
                ch = gradient[int(len(gradient)*a[y][x])]
                if curses.can_change_color()==True:
                    stdscr.addstr(y,x,ch,curses.color_pair(7-int(8*a[y][x])))
                # elif curses.has_colors()==True:
                #     stdscr.addstr(y,x,ch,curses.color_pair(int(a[y][x]*4)))
                #needs to have the color pairs initialized above
                else:
                    stdscr.addstr(y,x,ch)
                #needs the color added in here at some point


        stdscr.refresh()
        if stdscr.getch() == ord('q'):
            break
        time.sleep(1/speed)
curses.wrapper(main)
