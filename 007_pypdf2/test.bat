@echo off

PowerShell.exe -NoProfile -Command python.exe .\get_num_pages_of_pdf.py (Get-Item *.pdf)
pause
exit 0

:COMMENT
出力:
C:\Data\repository\python-samples\007_pypdf2\PyPDF2によるPDFファイルの結合・分割と画像抽出する方法 _ Pythonでもっと自由を.pdf 19 pages
C:\Data\repository\python-samples\007_pypdf2\Pythonでコマンドライン引数を受け取る - Qiita.pdf 4 pages
