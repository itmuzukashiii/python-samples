#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import numpy as np
import matplotlib.pyplot as plt

def main():
    #--- tangent のグラフを描画する
    
    #--- -π/2 ～ π/2 まで 0.01 刻みで等差数列を作成 (step が細かいほどグラフが滑らかになる)
    x = np.arange(-np.pi/2, np.pi/2, 0.01)
    y = np.tan(x)
    plt.ylim(-2, 2)
    plt.plot(x, y)

    #--- 画像ファイルとして保存
    plt.savefig('graph_tan.pdf')
    plt.savefig('graph_tan.svg')
    plt.savefig('graph_tan.png')

if __name__ == '__main__':
    main()
