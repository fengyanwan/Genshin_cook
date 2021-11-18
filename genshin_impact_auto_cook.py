# coding:utf-8
import random
import time

import pyautogui

from commom.utils import calculate_y0_r, cut_arc, is_color_pixel

# 相关坐标点，以 1920 * 1080 尺寸得出，可通过鼠标位置py文件获取
x11, y11 = 696, 773
x21, y21 = 960, 718
x31, y31 = 1224, 773
x10, y10 = 714, 809
x20, y20 = 960, 759
x30, y30 = 1206, 809

cook_start_pos = (972, 1013)        # 手动烹饪坐标
# cook_start_pos = (972, 1013)      # 熟练度完成后的手动烹饪坐标
cook_stop_pos = (960, 938)          # 停止烹饪坐标
cook_complete_confirm = (965, 907)  # 完成确认坐标

# 计算3个点坐标，确保点在圆环内部，减少出错
x1 = (x11 + x10) // 2
y1 = (y11 + y10) // 2
x2 = (x21 + x20) // 2
y2 = (y21 + y20) // 2
x3 = (x31 + x30) // 2
y3 = (y31 + y30) // 2

x0 = x2
y0, r = calculate_y0_r(x0, x1, y1, x2, y2)      # 计算近视原点坐标y0
pos = cut_arc(x0, y0, x1, y1, x3, y2, 80)       # 获取等弧长的点坐标，确保各点均匀并一定在圆环内

# light_yellow_color =(237, 234, 180)           # 颜色值 rgb
deep_yellow_color = (254, 192, 63)
white_color = (255, 255, 255)

time.sleep(2)  # 准备开始时间
while True:                                     # 三次点击的循环
    deep_yellow_area = []
    is_good_chance = False

    pyautogui.moveTo(cook_start_pos, duration=random.uniform(0.1, 0.5))
    pyautogui.click()                           # 点击开始烹饪
    pyautogui.moveTo(cook_stop_pos, duration=random.uniform(0.1, 0.3))
    while True:                                 # 进行截图比较循环
        img = pyautogui.screenshot()            # 截图

        if not deep_yellow_area:                                    # 判断深黄区域列表是空的，就进入循环开始比较每个点
            for (x, y) in pos:
                pixel = img.getpixel((x, y))
                if is_color_pixel(pixel, deep_yellow_color):        # 判断圆弧分段上的点有没有深黄色，有就加入到列表中
                    deep_yellow_area.append((x, y))
        elif deep_yellow_area:                                      # 深黄列表非空，说明上次截图中有圆弧上的点是深黄色
            x_start = deep_yellow_area[0][0]
            y_start = deep_yellow_area[0][1]
            pixel = img.getpixel((x_start, y_start))
            if is_color_pixel(pixel, white_color):                  # 判断深黄列表第一个点的新截图颜色是不是白色，
                continue                                            # 白色说明可能勺子刚进入深黄区，直接跳出进行下次截图
            if is_color_pixel(pixel, deep_yellow_color):            # 深黄列表还是黄色，就对内部点查询一遍，
                for (x, y) in deep_yellow_area:                     # 有白色说明勺子已经完全进入，赶紧退出查询颜色循环
                    pixel = img.getpixel((x, y))
                    if is_color_pixel(pixel, white_color):
                        is_good_chance = True
                        break
                    else:
                        continue
        if is_good_chance:                                          # 判断是好的时机，退出截图循环
            break
        # time.sleep(0.1)

    pyautogui.click()                                               # 马不停蹄按下按键，完美烹饪成功
    time.sleep(1)
    pyautogui.moveTo(cook_complete_confirm, duration=random.uniform(0.2, 0.7))
    pyautogui.click()                                               # 移动到确认坐标点击，准备开始下次烹饪
    time.sleep(1)
