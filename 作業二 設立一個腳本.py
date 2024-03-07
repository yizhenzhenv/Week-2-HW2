# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 08:48:03 2024

@author: student
"""

# 收集用戶資料
name = input("請輸入您的姓名：")
age = int(input("請輸入您的年齡："))
height = float(input("請輸入您的身高（米）："))
favorite_color = input("請輸入您喜愛的顏色：")

# 將資料存儲在字典中
user_data = {
    "姓名": name,
    "年齡": age,
    "身高": height,
    "喜愛的顏色": favorite_color
}

# 格式化並輸出個人資料摘要
summary = "{}, {}歲, 身高{}米, 喜愛的顏色是{}。".format(
    user_data["姓名"],
    user_data["年齡"],
    user_data["身高"],
    user_data["喜愛的顏色"]
)

print("個人資料摘要：", summary)
