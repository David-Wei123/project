#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import sys

# 添加当前目录到Python路径
sys.path.append(os.getcwd())

# 导入read_frame函数
from read_frame import read_frame

import numpy as np

def test_score(test_image_path):
    """
    根据标准答案图像计算学生测试答案的得分
    """
    score = 0
    ans = read_frame('D:/Answer.png')
    test = read_frame(test_image_path)

    if ans.shape != test.shape:
        raise ValueError("The shape of the test image does not match the answer image.")

    for i in range(len(ans)):
        if (ans[i] == test[i]).all():
            score += 10
    return score

def test_score_with_wrong(test_image_path):
    """
    计算得分并返回错误的题目
    """
    score = 0
    wrong = [0 for _ in range(10)]  # 假设有10道题
    ans = read_frame('D:/Answer.png')
    test = read_frame(test_image_path)

    if ans.shape != test.shape:
        raise ValueError("The shape of the test image does not match the answer image.")

    for i in range(len(ans)):
        if (ans[i] == test[i]).all():
            score += 10
        else:
            wrong[i] += 1
    return score, wrong

# 测试代码
test_image_path = 'D:/David.png'

# 计算得分
score = test_score(test_image_path)
print(f"Total score: {score}")

# 计算得分并记录错误
score, wrong = test_score_with_wrong(test_image_path)
print(f"Total score: {score}")
print(f"Wrong answers: {wrong}")


# In[ ]:




