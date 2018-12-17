#!/usr/bin/env python3

"""Foobar.py: Description of what foobar does.

__author__ = "Sunpengwei"
__pkuid__  = "1800011718"
__email__  = "1800011718@pku.edu.cn"
"""

import turtle

result = []

def pave(cell, l_w, w_w, l_b, w_b, result1):
    '''show how wall is praved by the brick'''
    # 所有的墙已经被铺满
    if 0 not in cell:
        if sorted(result1) in result:
            pass
        else:
            result.append(sorted(result1))
        return result
    # 墙未被铺满
    else:
        brick = cell.index(0)
        [x,y] = [brick // l_w , brick % l_w]
        # 横铺
        empty_y = cell[brick:((x + 1) * l_w)].count(0)
        if empty_y >= l_b and (w_w - x) >= w_b:
            b = [(l_w * j + k) for j in range(x, x + w_b) for k in range(y, y + l_b)]  # 包括了所有砖的位置
            a = tuple(b)
            result1.append(a)
            for i in b:
                cell[i] = 1  # 通过改变cell的状态来表示将砖铺在墙上
            pave(cell, l_w, w_w, l_b, w_b, result1)
            del result1[-1]
            for i in b:
                cell[i] = 0  # 通过改变cell的状态来表示将砖拆下来
        # 竖铺
        if (w_w - x) >= l_b and (l_w - y) >= w_b:
            d = [l_w * j + k for j in range(x, x + l_b) for k in range(y, y + w_b)]
            c = tuple(d)
            result1.append(c)
            for i in d:
                cell[i] = 1  # 通过改变cell的状态来表示将砖铺在墙上
            pave(cell, l_w, w_w, l_b, w_b, result1)
            del result1[-1]
            for i in d:
                cell[i] = 0  # 通过改变cell的状态来表示将砖拆下来


def draw_background(lenth,width):
    '''draw each cell of the wall'''
    a = turtle.Turtle()
    a.shape('circle')
    a.color('blue')
    a.up()
    a.speed(0)
    a.goto(-100, 100)
    # 绘制表格中的横线
    for i in range(width + 1):
        a.goto(-100, 100 - 30 * i)
        a.down()
        a.forward(30 * lenth)
        a.up()
    a.goto(-100, 100)
    a.right(90)
    # 绘制表格中的竖线
    for i in range(lenth + 1):
        a.goto(-100 + 30 * i, 100)
        a.down()
        a.forward(30 * width)
        a.up()
    a.hideturtle()


def draw_number(lw, ww):
    '''give the serial number of the cell of the wall'''
    a = turtle.Turtle()
    a.up()
    a.color('blue')
    for i in range(0, ww):
        a.goto(-115, 77 - 30 * i)
        for j in range(0, lw):
            a.forward(30)
            a.write(j + lw * i)
    a.hideturtle()


def draw_brick(brick, lb, wb, lw):
    '''draw each brick paved on the wall'''
    place = brick[0]
    (x, y) = (place // lw,place % lw)
    a = turtle.Turtle()
    a.shape('circle')
    a.pensize(3)
    a.up()
    a.speed(0)
    a.goto(-100 + 30 * y, 100 - 30 * x)
    a.down()
    # 横铺的砖
    if (brick[0] + lb - 1) in brick:
        a.forward(30 * lb)
        a.right(90)
        a.forward(30 * wb)
        a.right(90)
        a.forward(30 * lb)
        a.right(90)
        a.forward(30 * wb)
        a.right(90)
    # 竖铺的砖
    else:
        a.forward(30 * wb)
        a.right(90)
        a.forward(30 * lb)
        a.right(90)
        a.forward(30 * wb)
        a.right(90)
        a.forward(30 * lb)
        a.right(90)
    a.hideturtle()


def main():
    '''main module: to judge if the input is valid'''
    lw = input('please enter the lenth of the wall')
    ww = input('please enter the width of the wall')
    lb = input('please enter the lenth of the brick')
    wb = input('please enter the width of the brick')
    list = [lw, ww, lb, wb]
    # 判断是否为有效输入（整数）
    if lw.isdigit() != True:
        print('Your lw is invalid. Please enter a integer.')
    if ww.isdigit() != True:
        print('Your ww is invalid. Please enter a integer.')
    if lb.isdigit() != True:
        print('Your lb is invalid. Please enter a integer.')
    if wb.isdigit() != True:
        print('Your wb is invalid. Please enter a integer.')
    # 判断墙是否比砖大
    elif int(lw) * int(ww) <= int(lb) * int(wb): 
        print('Your brick is bigger than the wall!')
    # 判断墙是否能被砖铺满
    elif (int(lw) * int(ww)) % (int(lb) * int(wb)) != 0:
        print('Your wall can not be paved completely by your brick')
    else:
        l_w = int(lw)
        w_w = int(ww)
        l_b = max(int(lb), int(wb))      
        w_b = min(int(lb), int(wb))
        cell = [0] * l_w * w_w
        result1 = []
        pave(cell, l_w, w_w, l_b, w_b, result1)
        for i in result:
            print(i)
        # 绘制背景表格
        num = turtle.numinput('Select Plan', 'please choose the serial number of the path',
                              default = 0, minval = 0, maxval = len(result) - 1)
        draw_background(l_w, w_w)
        draw_number(l_w, w_w)
        # 绘制砖的铺法
        for i in result[int(num)]:
            draw_brick(i, l_b, w_b, l_w)
        turtle.done()

if __name__ == '__main__':
    main()
