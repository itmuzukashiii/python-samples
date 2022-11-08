#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.locals import QUIT # QUIT定数のインポート

def main():
    
    #--- pygame モジュールの初期化
    pygame.init()

    #--- 使用できるフォントを表示
    # fo = pygame.font.get_fonts()
    # print(fo)

    #--- サイズを指定してウィンドウを作成し、変数SURFACEに格納
    SURFACE = pygame.display.set_mode((400, 300))
    #--- FPS管理用の clock オブジェクト作成
    FPSCLOCK = pygame.time.Clock()
    #--- Set the current window caption
    pygame.display.set_caption(("PyGame Window"))

    #--- システムフォントからフォントオブジェクト作成 (フォント名, フォントサイズ)
    sysfont = pygame.font.SysFont(name='bizudgothic', size=36)
    counter = 9728

    while True:
        #--- イベントキューからイベントを取得し，QUITイベント (Xボタン押下時等) なら終了する
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        counter += 1

        #--- 黒塗りつぶし
        SURFACE.fill((0, 0, 0))
        #--- フォントイメージ作成
        count_image = sysfont.render(
            "{} is {}".format(u"カウント", counter),
            True, # antialias
            (225, 225, 225) # color
        )
        #--- blit: bitmap 等を転送する
        SURFACE.blit(count_image, (50, 50))

        #--- 画面に描画
        pygame.display.update()
        #--- ループ速度調整
        # tick: 時を刻む; 1s 間に n回ループするよう適切なsleepを設けてくれる
        FPSCLOCK.tick(10)

if __name__ == '__main__':
    main()
