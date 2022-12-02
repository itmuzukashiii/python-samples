# Python いろいろテスト

## 001_randint

- `random.randint(a,b)` の使い方
- a <= int <= b が生成されることに注意

## 002_sort

- `sorted()` の使い方
- コレクションのソートは最初の異なる要素間の比較と等価

## 003_map

- map() の使い方
- メソッドの代わりにラムダ式を渡す

### 004_list_comprehension

- リスト内包表記のテスト

### 005_filter

- filter() の使い方

### 006_import

- import 文の使い方
- 直接実行するか import で呼ばれるかで `__name__` が変わる

### 007_pypdf2

- PyPDF2 で PDF のページ数を抽出する方法

### 008_matplotlib

- matplotlib を使って `tan` のグラフをウィンドウ描画，画像保存するサンプル

### 009_pygame_window

- PyGame を使ってウィンドウ上に文字列を描画するサンプル

### 010_sololearn_97_poker

- Sololearn 問題 97 poker の解答例

### 011_python_websvr

- `http.server.SimpleHTTPRequestHandler` を使った簡易 Web サーバ

### 012_paramiko

- paramiko を用いて Ubuntu に 公開鍵認証で SSH ログインし，`ls -l` を実行するサンプル

### 013_for_in_string

- python の str は iterable であることのテスト

### 014_class_static_method

- classmethod, staticmethod のテスト
- デフォルトで用意されているデコレータ `@classmethod`, `@staticmethod` を使う
- これらを指定しないとインスタンスメソッドと解釈され，インスタンス化が必要となる
