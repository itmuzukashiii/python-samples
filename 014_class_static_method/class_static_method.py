#!/usr/bin/env pyhon
import sys

class Base:
  class_var = "hoge"

  @classmethod           # クラスメソッド (必須なのだろうか？)
  def class_method(cls): # 第1引数にクラス(cls)が渡される
    print( "%s.%s, class_var: %s" % (cls.__name__, 'class_method', cls.class_var) )

  @staticmethod          # スタティックメソッド
  def static_method():   # 引数をとらない
    print( "%s.%s, class_var: %s" % ('Base', 'static_method', Base.class_var) )


class Derived(Base):
  class_var = "foo"

def main():

  #--- インスタンス化なしで実行
  
  Base.class_method()
  # -> Base.class_method, class_var: hoge
  Base.static_method()
  # -> Base.static_method, class_var: hoge
  Derived.class_method()
  # -> Derived.class_method, class_var: foo
  Derived.static_method()
  # -> Base.static_method, class_var: hoge
  print(Derived.static_method)
  # -> <function Base.static_method at 0x6fffffe8c430>
  
  #--- インスタンス化して実行
  
  b = Base()
  b.class_method()
  # -> Base.class_method, class_var: hoge
  b.static_method()
  # -> Base.static_method, class_var: hoge
  
  d = Derived()
  d.class_method()
  # -> Derived.class_method, class_var: foo
  d.static_method()
  # -> Base.static_method, class_var: hoge
  print(d.static_method)
  # -> <function Base.static_method at 0x6fffffe8c430>

if __name__ == '__main__':
  main()
  sys.exit(0)


"""
https://qiita.com/msrks/items/fdc9afd12effc2cba1bc

- インスタンス変数，インスタンスメソッドにアクセスしないとき
  (メソッド内で self を使わないとき) は classmethod, staticmethod を使う

- classmethod
  * 第一引数に cls を与える
  * クラス変数にアクセスすべきとき
  * 継承クラスで動作が変わるとき

- staticmethod
  * 継承クラスでも動作が変わらないとき
"""
