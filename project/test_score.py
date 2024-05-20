#!/usr/bin/env python
# coding: utf-8

# In[5]:


from read_frame import read_frame  

def test_score(test_path):
   
    score = 0
    ans = read_frame('answer/Answer.png')
    test = read_frame(test_path)  
    for i in range(len(ans)):
        if (ans[i] == test[i]).all():
            score += 10
    return score

def test_score_with_wrong(test_path):
    score = 0
    wrong = [0 for _ in range(10)]
    ans = read_frame('answer/Answer.png')
    test = read_frame(test_path)
    
    for i in range(len(ans)):
        if (ans[i] == test[i]).all():
            score += 10
        else:
            if i < len(wrong):  
                wrong[i] += 1
    return score, wrong

