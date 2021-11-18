# coding:utf-8
import numpy as np


# ---------------------------------------------#
# 根据两点坐标及圆心的x0坐标，求圆心的y0和半径r的值
def calculate_y0_r(x0, x1, y1, x2, y2):
    y0 = ((x0 - x2) ** 2 - (x0 - x1) ** 2 - y1 ** 2 + y2 ** 2) / (2 * (y2 - y1))
    r = round(((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5)
    return [y0, r]
# ---------------------------------------------#


# ---------------------------------------------#
# 根据已知圆弧的圆心，起点、终点坐标，将圆弧进行分为 n 段，
# 计算各分段点的坐标整数，共 n+1 个坐标，返回列表类型
def cut_arc(x0, y0, x1, y1, x2, y2, n):
    list1 = [(round(x1), round(y1))]
    r = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
    ab = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    cos = (2 * r ** 2 - ab ** 2) / (2 * r * r)
    theta = np.arccos(cos)
    alpha = theta / n
    xlf = x1
    ylf = y1
    for i in range(n):
        con = (2 * r ** 2 * (1 - np.cos(alpha)) + x0 ** 2 - xlf ** 2 - r ** 2 - (y0 - ylf) ** 2) / 2
        a = (x0 - xlf) ** 2 + (y0 - ylf) ** 2
        b = 0 - 2 * con * (x0 - xlf) - 2 * x0 * (y0 - ylf) ** 2
        c = con ** 2 + (y0 - ylf) ** 2 * x0 ** 2 - (y0 - ylf) ** 2 * r ** 2
        if b ** 2 - 4 * a * c < 0:
            raise ValueError('b^2 * 4ac 小于 0')
        x01 = (0 - b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        x02 = (0 - b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        if x01 >= xlf >= x02:
            xlf = x01
            ylf = y0 - (r ** 2 - (xlf - x0) ** 2) ** 0.5
        else:
            raise ValueError('两个根结果不正确')
        list1.append((round(xlf), round(ylf)))

    return list1
# ---------------------------------------------#


limit = 20


# ---------------------------------------------#
# 判断像素点是不是某个已知颜色， limit用于误差范围
def is_color_pixel(pixel, color):
    if not isinstance(pixel, tuple) or len(pixel) != 3 or \
            not isinstance(color, tuple) or len(color) != 3:
        raise ValueError(f'{pixel} or {color} is not a tuple of 3 lengths')
    if (color[0] - limit <= pixel[0] <= color[0] + limit and
            color[1] - limit <= pixel[1] <= color[1] + limit and
            color[2] - limit <= pixel[2] <= color[2] + limit):
        return True
    else:
        return False
# ---------------------------------------------#
