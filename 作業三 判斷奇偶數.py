# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 08:51:56 2024

@author: student
"""

# 讓使用者輸入一個整數
user_input = int(input("請輸入一個整數："))

# 判斷是否為偶數
if user_input % 2 == 0:
    print("{} 是偶數。".format(user_input))
else:
    print("{} 不是偶數。".format(user_input))
