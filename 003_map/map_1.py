#!/usr/bin/env python3

import sys

def main():
    num_list = [1,2,3]
    
    #--- ユーザ定義関数を渡す
    print(list(map(make_double, num_list)))

    #--- lambda を使って書き直す
    print(list(map(lambda x: x * 2, num_list)))

def make_double(n):
    return n * 2

if __name__ == '__main__':
    main()
    sys.exit(0)


"""出力
[2, 4, 6]
[2, 4, 6]
"""
