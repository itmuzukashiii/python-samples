# pypdf2

## インストール

```sh
$ python3 -m pip install pypdf2
```

## get_num_pages_of_pdf.py

pdf のページ数を取得するサンプル

## ページ数を抽出できないときがある

上記スクリプトでとある pdf のページ数を取得しようとしたところエラー．
暗号化のかかっているファイルだと情報を取得できないことがあるらしい．

```sh
$ ./get_num_pages_of_pdf.py
Traceback (most recent call last):
  File "/usr/lib/python3.6/site-packages/PyPDF2/pdf.py", line 1147, in getNumPages
    self.decrypt('')
  File "/usr/lib/python3.6/site-packages/PyPDF2/pdf.py", line 1987, in decrypt
    return self._decrypt(password)
  File "/usr/lib/python3.6/site-packages/PyPDF2/pdf.py", line 1996, in _decrypt
    raise NotImplementedError("only algorithm code 1 and 2 are supported")
NotImplementedError: only algorithm code 1 and 2 are supported

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "./get_num_pages_of_pdf.py", line 22, in <module>
    get_num_pages(f)
  File "./get_num_pages_of_pdf.py", line 12, in get_num_pages
    print("{} {} pages".format(pdf_name, pdf_reader.numPages))
  File "/usr/lib/python3.6/site-packages/PyPDF2/pdf.py", line 1158, in <lambda>
    numPages = property(lambda self: self.getNumPages(), None, None)
  File "/usr/lib/python3.6/site-packages/PyPDF2/pdf.py", line 1150, in getNumPages
    raise utils.PdfReadError("File has not been decrypted")
PyPDF2.utils.PdfReadError: File has not been decrypted
```
