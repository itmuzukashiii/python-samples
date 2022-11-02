#!/usr/bin/env python3

tuple_list = [(0,1),(5,3),(2,4)]

#--- 数値タプルのリストをソート
print(sorted(tuple_list))

"""出力:
[(0, 1), (2, 4), (5, 3)]

これを直感的に理解するのは厳しい
"""

"""
- Python の sorted() は安定ソート

The built-in sorted() function is guaranteed to be stable.

A sort is stable if it guarantees not to change the relative order of elements that compare equal —

this is helpful for sorting in multiple passes
(for example, sort by department, then by salary grade).
"""

"""
- ソート対象要素は __lt__() メソッドさえ実装していればソート可能

The sort algorithm uses only < comparisons between items.

While defining an __lt__() method will suffice for sorting,
PEP 8 recommends that all six rich comparisons be implemented.
"""

"""
- コレクション同士の比較は最初の異なる要素間の比較と等価

Collections that support order comparison are ordered the same as their first unequal elements
(for example, [1,2,x] <= [1,2,y] has the same value as x <= y).

If a corresponding element does not exist, the shorter collection is ordered first
(for example, [1,2] < [1,2,3] is true).
"""

#--- key に参照を指定してソート
print(sorted(tuple_list, key=lambda x: x[1]))

"""出力:
[(0, 1), (5, 3), (2, 4)]
"""

#--- いろいろな条件でソート
print(sorted(tuple_list, key=lambda x: x[0] - x[1]))

"""出力
[(2, 4), (0, 1), (5, 3)]
"""

print(sorted(tuple_list, key=lambda x: x[0] / x[1], reverse=True))

"""出力
[(5, 3), (2, 4), (0, 1)]
"""

