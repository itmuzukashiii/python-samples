#!/usr/bin/env python3

print("import_1 start.")
print("__name__ = {}".format(__name__))

def main():
    print("main executed.")

#--- 呼び出し側モジュールにおいては __name__ に '__main__' が格納される
if __name__ == '__main__':
    main()
