class MyClass:
    attribute = "x"

    @classmethod
    def my_class_method(cls):
        cls.attribute = "a"

    @staticmethod
    def my_non_class_method():
        MyClass.attribute = "b"

def main():

    print(MyClass.attribute)       # x
    MyClass.my_class_method()      # cls.attribute = 'a'
    print(MyClass.attribute)       # a
    MyClass.my_non_class_method()  # cls.attribute = 'b'
    print(MyClass.attribute)       # b
    
    mc = MyClass()
    print(mc.attribute)            # b
    mc.attribute = 'c'             # self.attribute = 'c' // 新しくインスタンス変数が割り当てられた
    print(mc.attribute)            # c
    print(MyClass.attribute)       # b
    print(mc.__class__.attribute)  # b

if __name__ == '__main__':
    main()

"""
<インスタンス変数>.<属性> = 'var' はインスタンス変数の生成と代入となる
<インスタンス変数>.<属性> はインスタンス変数が存在しない場合はクラス変数への参照となる
"""
