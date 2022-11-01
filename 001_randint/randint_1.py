#!/usr/bin/env python3

"""
https://note.nkmk.me/en/python-random-randrange-randint/

random.randint(a, b) returns a random integer int in a <= n <= b
"""

#--- random モジュールをインポート
import random

for _ in range(5):
    #--- random.randint とモジュール名から指定する
    print(random.randint(0,5))
print("done")

"""
出力例:

$ ./randint_1.py
0
4
1
0
3
done
"""
