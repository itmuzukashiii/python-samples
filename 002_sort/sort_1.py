#!/usr/bin/env python3

num_list = [7,4,3,1,10,5]

#--- 数値ソート
print(sorted(num_list))
"""
出力:
[1, 3, 4, 5, 7, 10]
"""


#--- 数値逆順ソート
print(sorted(num_list, reverse=True))
"""
出力:
[10, 7, 5, 4, 3, 1]
"""


#--- 末尾に文字を追加してから文字ソートしてみる
str_list = num_list.copy()
str_list.append("A")
# [7, 4, 3, 1, 10, 5, 'A']

#--- このままでは型が混在しておりソートできないため，map() で各要素を str に変換
#--- map() は map オブジェクトを返すので list() で list に変換 
str_list = list(map(str, str_list))
print(sorted(str_list))
"""
出力:
['1', '10', '3', '4', '5', '7', 'A']
"""


#--- 上記リストを文字列を逆順ソート
print(sorted(str_list, reverse=True))
"""
出力:
['A', '7', '5', '4', '3', '10', '1']
"""


#--- lambda 関数を使って文字列長でソート
print(sorted(str_list, key=lambda x: len(x)))
"""
出力:
['7', '4', '3', '1', '5', 'A', '10']
"""

