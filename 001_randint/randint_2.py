#!/usr/bin/env python3

#--- randint メソッドのみインポート
from random import randint

for _ in range(5):
    #--- randint とメソッド名のみで呼び出せる
    print(randint(0,5))
print("done")
