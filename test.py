
from collections import deque
import os
import time
import random
from threading import Thread
import random
import numpy as np
from datetime import datetime




RESET_F = '\033[m'
cyan_f = '\033[36m'
green_f = '\033[32m'
red_f = '\033[31m'
white_f = '\033[37m'
reset_f = '\033[m'
underline_f = '\033[4m'


class Canvas():
    def __init__(self, offset_r, offset_c, rows=10, cols=20,  framerate=20, color=241):
        os.system('cls')
        self.rows = rows
        self.cols = cols
        self.offset_r = offset_r
        self.offset_c = offset_c
        self.upt_interval = 1/framerate
        self.color = color
        self.build_array()

    def start(self, seconds):
        last_updt = time.time()
        time_sart = time.time()
        while time.time() <= time_sart + seconds:
            if time.time() >= last_updt + self.upt_interval:
                last_updt = time.time()
                self.update()

    def update(self):
        self.draw_frame()
        self.draw_array()
        self.draw_clock(0, 20)
        self.update_array()

    def draw_frame(self):
        print(self.set_cursor(self.offset_r-1, self.offset_c-1) +
              '┌' + ((1+self.cols)*'─') + '┐')
        print(self.set_cursor(self.offset_r+self.rows,
              self.offset_c-1)+'└' + ((1+self.cols)*'─') + '┘')
        for row in range(self.rows):
            print(self.set_cursor(row + self.offset_r, self.offset_c-1) + '│')
            print(self.set_cursor(row + self.offset_r,
                  self.offset_c+1+self.cols) + '│')

    def draw_array(self):
        r = 0
        for row in self.array:
            c = 0
            for char in row:
                print(self.set_cursor(self.offset_r+r, self.offset_c+c), end='')
                print(self.random_color(c % 3) + char, RESET_F, end='')
                c += 1
            r += 1

    def update_array(self):
        array = []
        i = 0
        for row in self.array:
            array.append(self.shift_list(row, random.randint(2, i+2)))
            i += 1
        self.array = self.shift_list(array, 1)

    def build_array(self, len=5):
        chars = 'ã■²È3XWBqº0¾ÙÀ      '
        array = []
        i = 0
        for row in range(self.rows):
            _string = ''.join(random.choices(chars, k=self.cols//2))
            _string += (self.cols - len)*' '
            string_list = []
            for char in _string:
                string_list.append(char)
            _string = self.shift_list(_string, row*3)
            array.append(_string[:self.cols])
            i += 1
        self.array = array

    def draw_clock(self, posx, posy):
        print(self.set_cursor(posx, posy) + red_f +  datetime.now().strftime("%H:%M:%S")+ reset_f)

    def random_color(self,  i, range=5):
        value = self.get_sin(range-self.color, i)
        return self.colors_256(self.color + value)

    @staticmethod
    def set_cursor(row, col):
        return f'\033[{row};{col}H'

    @staticmethod
    def shift_list(_list, rotation):
        _deque = deque(_list)
        _deque.rotate(rotation)
        return list(_deque)

    @staticmethod
    def colors_256(color_):
        num1 = str(color_)
        if color_ % 16 == 0:
            return(f"\033[38;5;{num1}m")
        else:
            return(f"\033[38;5;{num1}m")

    @staticmethod
    def get_sin(max, i):
        return int(max*((np.sin(i)+1)/2))





if __name__ == '__main__':
    os.system('cls')
    # Thread(target=Canvas(3,10, rows=15,color=161).start, args=(7,)).start()
    Thread(target=Canvas(3,20, cols=100, rows=15,color=110).start,  args=(12,)).start()
    # Thread(target=Canvas(3, 105, rows=15).start, args=(7,)).start()
