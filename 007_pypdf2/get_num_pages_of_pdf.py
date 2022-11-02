#!/usr/bin/env python3

import os
import PyPDF2
import sys
import re

def main(*files):
    """
    可変長引数をリストで受ける
    それぞれを PDF ファイルパスとしてページ数を算出
    """
    for f in files:
        get_num_pages(f)

    # target_path = '.'
    # filedirs = os.listdir(target_path)
    # files = [f for f in filedirs if (os.path.isfile(os.path.join(target_path, f)) and re.match(".*\.pdf$", f))]
    # print(files)

def get_num_pages(pdf_name):
    #--- 読み取り専用＆バイトデータとして open
    pdf_file_obj = open(pdf_name, 'rb')
    #--- PDF 読み込み
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    #--- ファイルパスとページ数を出力
    print("{} {} pages".format(pdf_name, pdf_reader.numPages))

if __name__ == '__main__':
    """
    sys.argv[0] にはスクリプト名が入るため，argv[1] 以降を main に渡す
    sys.argv をそのまま渡すとリストになってしまうため，* を先頭に付与して unpack しておく
    """
    main(*(sys.argv[1:]))
