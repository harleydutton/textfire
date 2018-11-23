import curses
import random
import time
import numpy as np
width = 120
height = 30
speed = 60
gradient = [' ','.',':','-','=','+','*','#','%','@']
def main(stdscr):
    if curses.has_colors()==True:
        stdscr.addstr(0,0,'Has colors!')
        curses.start_color()
        curses.init_pair(1,curses.COLOR_BLACK,0)
        curses.init_pair(2,curses.COLOR_BLACK,0)
        curses.init_pair(3,curses.COLOR_RED,0)
        curses.init_pair(4,curses.COLOR_YELLOW,0)
        curses.init_pair(5,curses.COLOR_YELLOW,0)
        curses.init_pair(6,curses.COLOR_WHITE,0)
        for test in range(0,4):
            stdscr.addstr(test+1,0,'pair {}'.format(test),curses.color_pair(test))
        if curses.can_change_color()==True:
            stdscr.addstr(1,0,'Can change colors!')
            curses.init_color(0,0,0,0)
            curses.init_color(1,40,40,0)
            curses.init_color(2,100,100,0)
            curses.init_color(3,500,225,0)
            curses.init_color(4,600,300,0)
            curses.init_color(5,700,500,0)
            curses.init_color(6,900,800,0)
            curses.init_color(7,1000,1000,1000)
            for pair in range(1,8):
                curses.init_pair(pair,7-pair,0)
            for test in range(0,8):
                stdscr.addstr(2+test,0,'pair {}'.format(test),curses.color_pair(test))
            stdscr.refresh()
            stdscr.getkey()
            stdscr.clear()
    stdscr.nodelay(True)
    a = np.zeros((height,width))
    while True:
        # a = np.roll(a,-1,axis=0)
        for row in range(0,height-1):
            tmp = [None]*width
            for col in range(0,width):
                avg = a[row+1][col]*10
                if col > 0:
                    avg += a[row+1][col-1]
                    avg += a[row][col-1]
                if col < width-1:
                    avg += a[row+1][col+1]
                    avg += a[row][col+1]
                tmp[col]=avg/14.3
            a[row]=tmp
        for i in range(0,width):
            a[height-1][i]=random.random()
        for x in range(0,width):
            for y in range(0,height-1):#the bottom row is ugly so i hide it
                ch = gradient[int(len(gradient)*a[y][x])]
                if curses.can_change_color()==True:
                    stdscr.addstr(y,x,ch,curses.color_pair(7-int(8*a[y][x])))
                elif curses.has_colors()==True:
                    stdscr.addstr(y,x,ch,curses.color_pair(1+int(a[y][x]*6)))
                else:
                    stdscr.addstr(y,x,ch)
        stdscr.refresh()
        if stdscr.getch() == ord('q'):
            break
        time.sleep(1/speed)
curses.wrapper(main)
