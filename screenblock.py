#!/usr/bin/env python
# coding: utf-8

import os
import sys
import time
import curses
import pyautogui
from datetime import datetime


CNT = 1
TIME_INTERVAL = 500
try:
    TIME_INTERVAL = int(input('기준 시간을 입력하세요(초 단위). ==> ') )   # second
    if TIME_INTERVAL >= 1200:
        raise Exception('최대시간은 1000초 입니다.')
except ValueError:
    sys.exit('숫자 외 다른 문자를 입력하셨습니다. 종료합니다.')
except Exception as e:
    sys.exit(e.__str__() +' 종료합니다.')

PASS = 'pass'
BLOCK = 'block'

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
timer=0

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

def printStr(screenWidth, screenHeight, currentMouseX, currentMouseY, blockType):
    stdscr.addstr(0,0,'=========================================================================                                               ')
    stdscr.addstr(1,0,'=  ====  ====  =========  =======================================   ==  =                                               ')
    stdscr.addstr(2,0,'=  ====  ====  =========  ======================================  =  =  =                                               ')
    stdscr.addstr(3,0,'=  ====  ====  =========  ======================================  ==   ==                                               ')
    stdscr.addstr(4,0,'=  ====  ====  ===   ===  ===   ====   ===  =  = ====   =================                                               ')
    stdscr.addstr(5,0,'=   ==    ==  ===  =  ==  ==  =  ==     ==        ==  =  ================                                               ')
    stdscr.addstr(6,0,'==  ==    ==  ===     ==  ==  =====  =  ==  =  =  ==     ================                                               ')
    stdscr.addstr(7,0,'==  ==    ==  ===  =====  ==  =====  =  ==  =  =  ==  ===================                                               ')
    stdscr.addstr(8,0,'===    ==    ====  =  ==  ==  =  ==  =  ==  =  =  ==  =  ================                                               ')
    stdscr.addstr(9,0,'====  ====  ======   ===  ===   ====   ===  =  =  ===   =================                                               ')
    stdscr.addstr(10,0,'=========================================================================                                               ')
    stdscr.addstr(11,0,'========================================================================================================================')
    stdscr.addstr(12,0,'===    ====  =======  ==        ==    ==  =====  ==        ============      ====  ==========    ======     ===  ====  =')
    stdscr.addstr(13,0,'==  ==  ===   ======  =====  ======  ===   ===   ==  ==================  ===  ===  =========  ==  ====  ===  ==  ===  ==')
    stdscr.addstr(14,0,'=  ====  ==    =====  =====  ======  ===  =   =  ==  ==================  ====  ==  ========  ====  ==  ========  ==  ===')
    stdscr.addstr(15,0,'=  ====  ==  ==  ===  =====  ======  ===  == ==  ==  ==================  ===  ===  ========  ====  ==  ========  =  ====')
    stdscr.addstr(16,0,'=  ====  ==  ===  ==  =====  ======  ===  =====  ==      ====        ==      ====  ========  ====  ==  ========     ====')
    stdscr.addstr(17,0,'=  ====  ==  ====  =  =====  ======  ===  =====  ==  ==================  ===  ===  ========  ====  ==  ========  ==  ===')
    stdscr.addstr(18,0,'=  ====  ==  =====    =====  ======  ===  =====  ==  ==================  ====  ==  ========  ====  ==  ========  ===  ==')
    stdscr.addstr(19,0,'==  ==  ===  ======   =====  ======  ===  =====  ==  ==================  ===  ===  =========  ==  ====  ===  ==  ====  =')
    stdscr.addstr(20,0,'===    ====  =======  =====  =====    ==  =====  ==        ============      ====        ====    ======     ===  ====  =')
    stdscr.addstr(21,0,'========================================================================================================================')

    stdscr.addstr(22,0,'ON-TIME block 실 행 ~~! ( 기 준 시 간  : {} sec )'.format(TIME_INTERVAL))
    stdscr.addstr(23,0,'전 체 사 이 즈 : {:>4}, {:>4} / 현 재  위 치 : {:>4}, {:>4} '
              .format(screenWidth, screenHeight, currentMouseX, currentMouseY))
    
    stdscr.addstr(24,0,'기 준  시 간 에  따 라  마 우 스  위 치  변 화 를  체 크 해 서  기 준 시 간 동 안  변 화 가  없 으 면  하 단 부 를  클 릭 해 서  온 타 임  작 동 을  무 력 화  합 니 다. ')
    if blockType ==  PASS:
        stdscr.addstr(26,0,' '*100)
        stdscr.addstr(26,0,'현 재 위 치 : {:>4}, {:>4} // pass! '.format(currentMouseX, currentMouseY))
    elif blockType ==  BLOCK:
        stdscr.addstr(26,0,' '*100)
        stdscr.addstr(26,0,'[{}] {:0>4} 번 째  동 작 /// ({:>4},{:>4}) 위 치  클 릭 '
                          .format(datetime.now(), CNT, int(screenWidth*4/5), screenHeight))
    stdscr.addstr(27,0,'경 과 시 간 : {:>2}min {:>2}sec /// {}sec '.format(int(timer/60), timer%60, timer))
    stdscr.addstr(28,0,'중 단 을   원 하 시 면   창 을   종 료 하 세 요 ')
    stdscr.refresh()
    

try:
    while True :
        blockType=''
        time.sleep(1)
        timer +=1
        if(timer % TIME_INTERVAL == 0):
            if (currentMouseX, currentMouseY) != pyautogui.position():
                blockType = PASS
            else:
                blockType = BLOCK
                
                #키보드로 0.3초동안 '/' 글자를 입력
                pyautogui.click(screenWidth*4/5, screenHeight)
                pyautogui.typewrite("/", interval=0.3)

                CNT += 1
            currentMouseX, currentMouseY = pyautogui.position()
        printStr(screenWidth, screenHeight, currentMouseX, currentMouseY, blockType)

finally:
    curses.echo()
    curses.nocbreak()
    curses.endwin()   