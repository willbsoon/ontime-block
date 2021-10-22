#!/usr/bin/env python
# coding: utf-8

import os
import sys
import time
import curses
import pyautogui
from datetime import datetime
import curses
import curses
 
def main(stdscr):
    # Color Pair
#     curses.use_default_colors()

#    curses.start_color()  # 이걸 해줘야 함
    
    if curses.has_colors():
        for i in range(1, 100):
            curses.init_pair(i, curses.COLOR_WHITE, curses.COLOR_BLACK) # 팔레트 저장. 글씨 색, 배경 색
            stdscr.addstr("COLOR %d! " % i, curses.color_pair(i)) # 팔레트 색에 따라 컬러 바뀜
            stdscr.addstr("BOLD! ", curses.color_pair(i) | curses.A_BOLD)
            stdscr.addstr("STANDOUT! ", curses.color_pair(i) | curses.A_STANDOUT)
#             stdscr.addstr("UNDERLINE! ", curses.color_pair(i) | curses.A_UNDERLINE)
            stdscr.addstr("BLINK! ", curses.color_pair(i) | curses.A_BLINK)
#             stdscr.addstr("DIM! ", curses.color_pair(i) | curses.A_DIM)
#             stdscr.addstr("REVERSE! ", curses.color_pair(i) | curses.A_REVERSE)
    stdscr.refresh()
    stdscr.getch()
 
    while True:
        try:
            k = stdscr.getkey()
            if k == "\n": break
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    curses.wrapper(main)