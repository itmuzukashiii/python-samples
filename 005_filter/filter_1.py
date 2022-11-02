#!/usr/bin/env python3

input_list = [0, 1, 2, 3, 4, 5, 6, 7]

#--- 偶数だけを抜き出す
print(list(filter(lambda a: a%2==0, input_list)))

#--- 奇数のみを抜き出す
print(list(filter(lambda a: a%2==1, input_list)))

#--- 3の倍数のみを抜き出す
print(list(filter(lambda a: a%3==0, input_list)))


"""出力:
[0, 2, 4, 6]
[1, 3, 5, 7]
[0, 3, 6]
"""
