# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

def calculate_circle_properties(radius):
    # 計算圓周長
    circumference = 2 * math.pi * radius

    # 計算圓面積
    area = math.pi * radius ** 2

    return circumference, area

# 輸入半徑
radius = float(input("請輸入圓的半徑："))

# 呼叫函式計算圓周長和圓面積
circumference, area = calculate_circle_properties(radius)

# 輸出結果
print("圓周長為：", format(circumference, ".2f"))
print("圓面積為：", format(area, ".2f"))
