#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""requirements
matplotlib
numpy
"""

import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#--- Windows 10 だと TkAgg だった
# print(mpl.get_backend())

# mpl.use('GTK3Agg')
# mpl.use('agg')    # (PNG) raster graphics - high quality images using the Anti-Grain Geometry engine.
# mpl.use('pdf')    # (PDF) vector graphics - Portable Document Format
# mpl.use('svg')    # (SVG) vector graphics - Scalable Vector Graphics

def main():
    #--- tangent のグラフを描画する
    
    #--- -π/2 ～ π/2 まで 0.01 刻みで等差数列を作成 (step が細かいほどグラフが滑らかになる)
    x = np.arange(-np.pi/2, np.pi/2, 0.01)
    y = np.tan(x)
    plt.ylim(-2, 2)
    plt.plot(x, y)

    #--- GUI 上に描画 (tkinter を使っている？)
    plt.show()

if __name__ == '__main__':
    main()
