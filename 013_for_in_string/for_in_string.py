#!/usr/bin/env python3
# -*- coding: utf-8 -*-

my_courses = { 'course1': 'html', 'course2': 'css' }

def pyc(dict):
  result = []

  for kw in dict.keys():
    for i in dict[kw]:
      if i in 'python': # h == h
        result.append(dict[kw])
        break
  return result

print(pyc(my_courses))

"""出力:
['html']
"""

"""
for in in 'string'
は，char の リストに対するイテレーションとなる
"""
