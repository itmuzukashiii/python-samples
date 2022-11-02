#!/usr/bin/env python3

from pprint import pprint

"""help(pprint.pprint)

Help on function pprint in module pprint:

pprint(object, stream=None, indent=1, width=80, depth=None, *, compact=False, sort_dicts=True, underscore_numbers=False)
    Pretty-print a Python object to a stream [default is sys.stdout].
"""

#--- 2倍
print([x * 2 for x in range(5)])
"""出力
[0, 2, 4, 6, 8]
"""

#--- 2乗
print([x ** 2 for x in range(5)])
"""出力
[0, 1, 4, 9, 16]
"""
#--- 別のリストを作る
pprint(
    [ [x,x+1,x+2] for x in range(5) ]
    ,width=20
)
"""出力
[[0, 1, 2],
 [1, 2, 3],
 [2, 3, 4],
 [3, 4, 5],
 [4, 5, 6]]
"""

pprint(
    [ [x+y*2 for x in range(3)] for y in range(4) ]
    ,width=20
)
"""出力
[[0, 1, 2],
 [2, 3, 4],
 [4, 5, 6],
 [6, 7, 8]]
"""

#--- if によるフィルタリング
print( [x for x in range(6) if x%2==0] )
"""出力
[0, 2, 4]
"""
