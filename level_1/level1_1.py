# -*- coding: utf-8 -*-
"""level1_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wp9EgJAiuMbGVYgErzSYBsdI9VZuTbnS
"""

def solution(participant, completion):
  temp = 0
  dic = {}
  
  for part in participant:
    dic[hash(part)] = part
    temp += int(hash(part))

  for com in completion:
    temp -= hash(com)

  answer = dic[temp]
  return answer